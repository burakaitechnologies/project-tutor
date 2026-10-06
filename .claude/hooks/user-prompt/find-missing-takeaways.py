"""
find-missing-takeaways.py - finds finished days whose takeaways must be written

WHAT THIS FILE IS
A Python script. Python is a programming language; the program "python3" runs
this file from top to bottom. Text between three quote marks and lines that
start with "#" are explanations for people; Python skips them.

WHY IT EXISTS
Every finished day needs a "day takeaways" file: a summary of what the day
taught (see .claude/rules/keeping-memory.md). Writing a summary needs
thinking, so the main agent writes it. Finding WHICH days need one needs no
thinking, so this script does that part, and it never forgets.

WHO RUNS IT, AND WHEN
Claude Code runs it through a hook in .claude/settings.json on the moment
UserPromptSubmit: every time a message is sent. So it also catches a new day
that begins in the middle of a long session. It prints something ONLY when a
day needs takeaways; otherwise it stays silent, so it costs nothing.

WHAT COUNTS AS "NEEDS TAKEAWAYS"
Every day folder before today that has a process log, but either has no
day-takeaways.md, or its process log was changed after its takeaways were
written (so the takeaways are out of date). ALL day folders are checked.
"Today" is on the user's clock, from .claude/hooks/shared/local_time.py.
Known limit: it compares file change times. After a fresh copy from GitHub,
Git sets new times on all files, so past days may be listed once; writing or
touching their takeaways clears them.
"""

import json      # reads JSON text
import os        # works with files and folders
import re        # finds text patterns
import sys       # standard input, and where Python looks for files to import

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "shared"))
import local_time

MEM = ".claude/agent-memory/main-agent"  # the notes, as a path from the project folder

data = {}
if not sys.stdin.isatty():
    raw = sys.stdin.buffer.read().decode("utf-8")
    data = json.loads(raw) if raw.strip() else {}
project = os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd") or "."
notes = os.path.join(project, MEM)
if not os.path.isdir(notes):
    sys.exit(0)

today = local_time.now().date().isoformat()  # such as 2026-10-06

found = []
# The day folders (names that look like a date), oldest first.
for day in sorted(n for n in os.listdir(notes) if re.fullmatch(r"\d{4}-\d{2}-\d{2}", n)):
    # Only days before today. Comparing the text works here, because dates in
    # the shape YYYY-MM-DD sort in the same order as time.
    if day >= today:
        continue
    log = os.path.join(notes, day, "process-log.md")
    takeaways = os.path.join(notes, day, "day-takeaways.md")
    if not os.path.isfile(log):
        continue  # a day without a process log has nothing to summarize
    # "getmtime" is the time a file was last changed.
    if not os.path.isfile(takeaways) or os.path.getmtime(log) > os.path.getmtime(takeaways):
        found.append(f"  - {day} (from {MEM}/{day}/process-log.md)")

# Written as UTF-8 bytes with plain "\n" line ends: Python's normal "print"
# would end each line with "\r\n" on Windows.
if found:
    text = ["Day takeaways to write before other work (oldest first; "
            "see 'Day takeaways' in .claude/rules/keeping-memory.md):"] + found
    sys.stdout.buffer.write(("\n".join(text) + "\n").encode("utf-8"))
