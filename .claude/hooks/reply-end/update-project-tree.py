"""
update-project-tree.py - writes the full file tree of the project into README.md

WHAT THIS FILE IS
A Python script. Python is a programming language; the program "python3" runs
this file from top to bottom. Text between three quote marks and lines that
start with "#" are explanations for people; Python skips them.

WHY IT EXISTS
README.md is the map of the project. Part of the map is a "tree": a picture
made of text that shows every folder and file, and which folder each one is
in. Writing that picture by hand would be forgotten often. This script draws
it automatically, so it is always correct.

WHO RUNS IT, AND WHEN
Claude Code runs it, not a person. In .claude/settings.json, a "hook" (a rule
"when event X happens, run this command") on the event "Stop" runs it each
time Claude finishes a reply. Its output is not shown to Claude. It can also
be run by hand:
    python3 .claude/hooks/reply-end/update-project-tree.py

WHAT IT CHANGES
Only the part of README.md between the two marker lines
  <!-- tree:start -->   and   <!-- tree:end -->
Everything else in README.md is left exactly as it is. The markers are HTML
comments: notes that are hidden when README.md is shown as a formatted page.

THE SHAPE OF THE TREE
- Lines connect each item to its folder, like a family tree:
    ├── an item that has more items below it in the same folder
    └── the last item in its folder
    │   a line that continues down to the next item of an upper folder
- A folder name ends with "/", and its contents are drawn under it.
- A folder with more than 10 items shows only 10, then "... +N more".
- Names that start with a date (like 2026-10-03) are listed newest first,
  so the most recent days are the ones shown.
- The .git folder is skipped: it is Git's own storage, not project content.
- Items listed in .gitignore exist only on this computer. They are shown once
  with the note "(local only, not in Git)", and their contents are not listed.
  Which items these are is decided in .claude/hooks/shared/ignored_paths.py.
"""

import json      # reads JSON text
import os        # works with files and folders
import re        # finds text patterns
import sys       # standard input

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "shared"))
import ignored_paths

LIMIT = 10                                   # the most items shown per folder
DATED = re.compile(r"^\d{4}-\d{2}-\d{2}")   # a name that starts with a date

# Claude Code sends information about the moment as JSON on standard input;
# run by hand, there is none.
data = {}
if not sys.stdin.isatty():
    raw = sys.stdin.buffer.read().decode("utf-8")
    data = json.loads(raw) if raw.strip() else {}
project = os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd") or "."

readme = os.path.join(project, "README.md")
if not os.path.exists(readme):
    sys.exit(0)  # there is nowhere to write
with open(readme, encoding="utf-8", newline="") as f:
    text = f.read()
if "<!-- tree:start -->" not in text:
    sys.exit(0)

is_local_only = ignored_paths.checker(project)


def draw_folder(folder, relative, prefix, lines):
    """Adds the lines of one folder's contents to "lines".
    folder:   the folder's path on the computer
    relative: its path from the project folder ("" for the project folder)
    prefix:   the lines of the upper folders ("│   " or "    ") that must be
              drawn before each item of this folder.
    For each subfolder it runs itself again with a longer prefix. A function
    that runs itself like this is called "recursive"; it is how the tree
    reaches every level, however deep."""
    names = os.listdir(folder)
    # First the date-named items, newest first, then all other names in
    # alphabetical order (capital letters before small ones). ".git" is left out.
    names = (sorted((n for n in names if DATED.match(n)), reverse=True)
             + sorted(n for n in names if not DATED.match(n) and n != ".git"))
    # "total" is how many lines this folder draws: at most LIMIT names, plus
    # one "... +N more" line when names are hidden. The last line gets "└──".
    total = LIMIT + 1 if len(names) > LIMIT else len(names)
    for shown, name in enumerate(names, 1):
        if shown > LIMIT:
            lines.append(f"{prefix}└── ... +{len(names) - LIMIT} more")
            break
        # Under the last item no line continues ("    "); under the others the
        # vertical line "│" continues down to the next item.
        if shown == total:
            branch, below = "└── ", prefix + "    "
        else:
            branch, below = "├── ", prefix + "│   "
        path = os.path.join(folder, name)
        item = f"{relative}/{name}" if relative else name
        is_folder = os.path.isdir(path)
        if is_local_only(item, is_folder):
            lines.append(f"{prefix}{branch}{name}{'/' if is_folder else ''} (local only, not in Git)")
        elif is_folder:
            lines.append(f"{prefix}{branch}{name}/")      # a folder: show it ...
            draw_folder(path, item, below, lines)        # ... then its contents
        else:
            lines.append(f"{prefix}{branch}{name}")       # a file: just its name


# The first line is the name of the project folder itself.
tree = [os.path.basename(os.path.abspath(project)) + "/"]
draw_folder(project, "", "", tree)

# Build the new README.md: copy every line, but replace the lines between the
# markers with the new tree inside a code block (``` lines, which keep the
# spaces of the picture).
out, inside = [], False
for line in text.splitlines():
    if "<!-- tree:start -->" in line:
        out += [line, "```text"] + tree + ["```"]
        inside = True
        continue
    if "<!-- tree:end -->" in line:
        inside = False
    if not inside:
        out.append(line)
new = "\n".join(out) + "\n"

# Replace README.md only if something changed, so it is not touched after
# every reply for nothing. newline="\n" keeps Linux line endings everywhere.
if new != text:
    with open(readme, "w", encoding="utf-8", newline="\n") as f:
        f.write(new)
