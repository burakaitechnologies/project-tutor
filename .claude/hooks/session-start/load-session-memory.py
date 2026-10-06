"""
load-session-memory.py - tells the main agent which memory files to read

WHAT THIS FILE IS
A Python script. Python is a programming language; the program "python3" runs
this file from top to bottom. Text between three quote marks and lines that
start with "#" are explanations for people; Python skips them.

WHY IT EXISTS
A new session starts with an empty conversation, and a compaction (Claude Code
shrinking a long conversation into a summary) loses details. The saved notes
in .claude/agent-memory/main-agent/ hold the history. This script gives the
main agent a reading list of the most recent notes, so it starts with a good
amount of history every time.

WHY A READING LIST, AND NOT THE NOTES THEMSELVES
Claude Code adds at most 10,000 characters of a hook's output to the agent's
context (the text the agent can see). Longer output is cut to a short preview.
30 days of notes are far longer than that. So this script prints only the
paths of the files, and the main agent reads them with its normal file-reading
tool, which has no such limit. (Source: the Claude Code hooks documentation.)

WHO RUNS IT, AND WHEN
Claude Code runs it automatically, through a "hook" in .claude/settings.json:
a rule that says "when this moment comes, run this command". The moment is
SessionStart: a new session, a resumed session, /clear, and every compaction.

WHAT IT PRINTS
  1. The reading list: the newest day-takeaways files, then the newest
     process logs (how many: see the two settings below)
  2. Subagent records with the status "stopped" (unfinished helper work)
  3. Files changed since the last Git commit (unsaved work)
What the agent must do with it is written in the section "At session start"
of .claude/rules/keeping-memory.md.

WORKS WITH
  .claude/rules/keeping-memory.md  - the rules for this memory
  .claude/settings.json            - the hook that starts this script
"""

import json        # reads JSON text
import os          # works with files and folders
import re          # finds text patterns
import subprocess  # runs another program (here: git) and reads its answer
import sys         # standard input and output

# ---- Settings: how much history to read ------------------------------------
# Change these two numbers to read more or less history. Each day-takeaways
# file is about 2,000 characters and each process log about 9,000, so 30 + 3
# files are roughly 87,000 characters (about 22,000 tokens) once 30 days of
# notes exist.
TAKEAWAYS_TO_READ = 30   # the newest day-takeaways files (one per finished day)
LOGS_TO_READ = 3         # the newest process logs (one per day, today included)

# The folder of the main agent's notes, as a path from the project folder.
MEM = ".claude/agent-memory/main-agent"

data = {}
if not sys.stdin.isatty():
    raw = sys.stdin.buffer.read().decode("utf-8")
    data = json.loads(raw) if raw.strip() else {}
project = os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd") or "."
notes = os.path.join(project, MEM)

out = ["=== Memory reading list from .claude/hooks/session-start/load-session-memory.py ==="]


def finish():
    """Prints everything at once, as UTF-8, and ends the script."""
    sys.stdout.buffer.write(("\n".join(out) + "\n").encode("utf-8"))
    sys.exit(0)


# If the notes folder does not exist yet, there is nothing to read.
if not os.path.isdir(notes):
    out.append("No saved notes yet.")
    finish()

# The day folders (names that look like a date, YYYY-MM-DD), oldest first.
days = sorted(n for n in os.listdir(notes) if re.fullmatch(r"\d{4}-\d{2}-\d{2}", n))


def newest(name, count):
    """The paths of the newest files with this name, one per day. They stay in
    date order (oldest first), so the agent reads the history in the order it
    happened."""
    found = [f"{MEM}/{day}/{name}" for day in days if os.path.isfile(os.path.join(notes, day, name))]
    return found[max(0, len(found) - count):]


# ---- Part 1: the reading list ------------------------------------------------
out += ["", "--- 1. Read all these files now, in this order (see 'At session start' in .claude/rules/keeping-memory.md) ---",
        f"Day takeaways (up to the newest {TAKEAWAYS_TO_READ}):"]
out += ["  " + path for path in newest("day-takeaways.md", TAKEAWAYS_TO_READ)]
out.append(f"Process logs (up to the newest {LOGS_TO_READ}):")
out += ["  " + path for path in newest("process-log.md", LOGS_TO_READ)]

# ---- Part 2: unfinished subagent work ---------------------------------------
# Every note in .claude/agent-memory with a line that starts with exactly
# "Status: stopped". The raw-record copies are skipped: they are not notes.
out += ["", "--- 2. Subagent records with status 'stopped' ---"]
stopped = []
for folder, subfolders, names in os.walk(os.path.join(project, ".claude", "agent-memory")):
    subfolders[:] = sorted(s for s in subfolders if s != "raw-transcripts")
    for name in sorted(names):
        if name.endswith(".md"):
            path = os.path.join(folder, name)
            with open(path, encoding="utf-8", errors="replace") as f:
                if re.search(r"^Status: stopped", f.read(), flags=re.M):
                    stopped.append(os.path.relpath(path, project).replace(os.sep, "/"))
out += stopped or ["None."]

# ---- Part 3: unsaved changes ------------------------------------------------
# Git is the tool that saves versions of the project ("commits"). This lists
# the files changed since the last commit, at most 30. Without Git, or outside
# a Git repository, the part stays empty.
out += ["", "--- 3. Changes not yet committed (git status --short) ---"]
try:
    result = subprocess.run(["git", "-C", project, "status", "--short"], capture_output=True)
    if result.returncode == 0:
        out += result.stdout.decode("utf-8", errors="replace").splitlines()[:30]
except OSError:
    pass  # Git is not installed

out += ["", "=== End of the reading list ==="]
finish()
