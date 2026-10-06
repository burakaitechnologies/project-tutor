"""
check-broken-links.py - finds file paths in the guide files that point to nothing

WHAT THIS FILE IS
A Python script. Python is a programming language; the program "python3" runs
this file from top to bottom. Text between three quote marks and lines that
start with "#" are explanations for people; Python skips them.

WHY IT EXISTS
The guide files point to each other by path, for example
`.claude/rules/keeping-memory.md`. When a file is moved or renamed, these paths
easily stay old and wrong. This script finds such broken paths after every
answer of the main agent, so they are fixed at once.

WHICH FILES IT CHECKS
Every Markdown file (a file ending in ".md") in the project, in every folder,
so new files are checked without changing this script. Two folders are
skipped: .git (Git's own storage) and .claude/agent-memory (the memory notes:
they are history, and may mention old paths on purpose).

WHAT COUNTS AS A FILE PATH
Text between backticks (`like this`) that contains a "/" and nothing that
marks it as an example or as something else:
- placeholders such as <role>, YYYY, HH or "..." (examples, not real files),
- web addresses, and paths outside the project (starting with "~" or "C:"),
- commands such as /plugin (they start with "/").
Code blocks (between ``` lines) and the generated tree in README.md are skipped.
A path counts as found if it exists from the project folder or from the folder
of the file that mentions it. A missing path that .gitignore lists is not
broken either: such files exist only on one computer, or are made later (for
example .claude/settings.local.json, which /onboard creates). Which paths these
are is decided in .claude/hooks/shared/ignored_paths.py.

WHO RUNS IT, AND WHEN
Claude Code runs it through a hook in .claude/settings.json on the moment
"Stop": each time the main agent finishes an answer. If it finds broken paths,
it lists them and ends with "exit code 2". For the Stop moment, exit code 2
means: "do not finish yet". Claude Code then shows the list to the main agent,
which must fix the paths (or ask the user) before it finishes. To avoid an endless
loop, it does not block a second time in a row ("stop_hook_active").

WORKS WITH
  .claude/rules/building-maintaining-project.md  - the rule this check enforces
"""

import json      # reads JSON text
import os        # works with files and folders
import re        # finds text patterns
import sys       # standard input, standard error and the exit code

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "shared"))
import ignored_paths

raw = sys.stdin.buffer.read().decode("utf-8")
data = json.loads(raw) if raw.strip() else {}

# If the main agent is already continuing because of this check, let it finish.
if data.get("stop_hook_active"):
    sys.exit(0)

project = os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd") or "."

# Collect every Markdown file. "os.walk" visits the project folder and every
# folder inside it. Changing the list "subfolders" in place tells os.walk not
# to go into the skipped folders.
SKIPPED = {os.path.normpath(os.path.join(project, *parts)) for parts in
           [(".git",), (".claude", "agent-memory"), ("node_modules",), (".venv",), ("venv",)]}
files = []
for folder, subfolders, names in os.walk(project):
    subfolders[:] = [s for s in subfolders
                     if os.path.normpath(os.path.join(folder, s)) not in SKIPPED]
    files += [os.path.join(folder, n) for n in names if n.endswith(".md")]

# Signs that a text in backticks is an example or not a project path.
NOT_A_PATH = ("<", ">", "*", "{", "}", "$", " ", "YYYY", "HH", "...", "://", "\\")

broken = []
for path in files:
    if not os.path.exists(path):
        continue
    with open(path, encoding="utf-8", errors="replace") as f:
        text = f.read()  # errors="replace": a file with broken text never stops the check
    # Remove the generated tree and the code blocks: they are not references.
    text = re.sub(r"<!-- tree:start -->.*?<!-- tree:end -->", "", text, flags=re.S)
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    # Every text between single backticks.
    for ref in re.findall(r"`([^`\n]+)`", text):
        if "/" not in ref or ref.startswith(("/", "~")) or ":" in ref:
            continue
        if any(sign in ref for sign in NOT_A_PATH):
            continue
        first_part = ref.split("/")[0]
        if "." in first_part and not first_part.startswith("."):
            continue  # a web address such as code.claude.com/docs
        from_project = os.path.join(project, ref)
        from_file = os.path.join(os.path.dirname(path), ref)
        if not os.path.exists(from_project) and not os.path.exists(from_file):
            broken.append((os.path.relpath(path, project), ref))

# Leave out the paths that .gitignore lists: they are missing on purpose.
local_only = ignored_paths.ignored(project, {ref for _, ref in broken})
broken = [f"{where}: `{ref}`" for where, ref in broken if ref not in local_only]

if broken:
    # "stderr" (standard error) is where Claude Code reads the reason from.
    print("Broken file paths found. Fix moved or renamed paths yourself; "
          "ask the user if the fix needs a decision "
          "(see .claude/rules/building-maintaining-project.md):", file=sys.stderr)
    for item in sorted(set(broken)):
        print("  " + item, file=sys.stderr)
    sys.exit(2)
