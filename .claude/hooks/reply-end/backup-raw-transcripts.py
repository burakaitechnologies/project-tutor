"""
backup-raw-transcripts.py - copies Claude Code's raw session records into the project

WHAT THIS FILE IS
A Python script. Python is a programming language; the program "python3" runs
this file from top to bottom. Text between three quote marks and lines that
start with "#" are explanations for people; Python skips them.

WHY IT EXISTS
Claude Code saves a raw record ("transcript") of every session and every
subagent: every message, every command and every result. It keeps them in a
folder outside the project (under ~/.claude/projects/, where "~" is the user's
home folder) and deletes them after 30 days. The project's notes point to these records for
deeper detail, so this script copies them into the project, where they are
never deleted:
    .claude/agent-memory/main-agent/raw-transcripts/
These files are large and contain everything that was read, so .gitignore keeps
them out of Git: they stay on this computer only.

HOW THE COPIES ARE SORTED
Claude Code keeps all records in one folder, named only by session ID (a random
code that names one session), with no date. In the project, every session gets
one folder of its own, named after its start time, inside a folder for the day
it started, so they sort by time and are easy to find:
    2026-10-06/0931_1a2b3c4d/<session-id>.jsonl                the main session
    2026-10-06/0931_1a2b3c4d/subagents/agent-<id>.jsonl        its subagents
The rule itself is in .claude/hooks/shared/raw_transcript_copy.py, because two
other hooks write these paths too. To find the session of a conversation, look
for its session ID in the day's chat file (user-agent-chat.md).

WHO RUNS IT, AND WHEN
Claude Code runs it through a hook in .claude/settings.json on the moment
"Stop": each time the main agent finishes an answer. Claude Code gives it the
path of the current session's record as JSON on its standard input (the place
a program reads its input from).

HOW IT WORKS
It looks at every ".jsonl" file in Claude Code's folder for this project, and
copies a file only when the copy is missing or older than the original. So
after the first run, each run copies only what changed.
"""

import json      # reads JSON text (a format of names and values)
import os        # works with files and folders
import shutil    # copies files
import sys       # reads the standard input

# Load the shared rule. "sys.path" is the list of folders where Python looks
# for files to import; the "shared" folder next to this script's folder is
# added to it first.
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "shared"))
from raw_transcript_copy import copy_path

raw = sys.stdin.buffer.read().decode("utf-8")
data = json.loads(raw) if raw.strip() else {}

transcript_path = data.get("transcript_path", "")
project = os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd") or "."
if not transcript_path:
    sys.exit(0)  # nothing to copy; "exit(0)" means finished without error

# Claude Code's folder for this project is the folder of the session's record.
source = os.path.dirname(transcript_path)

# "os.walk" visits a folder and every folder inside it.
for folder, _subfolders, files in os.walk(source):
    for name in files:
        if not name.endswith(".jsonl"):
            continue
        original = os.path.join(folder, name)
        # The path from Claude Code's folder to the file, for example
        # "<session-id>.jsonl" or "<session-id>/subagents/agent-<id>.jsonl".
        relative = os.path.relpath(original, source)
        # Where its copy goes; the shared rule decides it.
        place = copy_path(source, relative)
        if place is None:
            continue  # the session's start is not in the record yet: copy it next time
        copy = os.path.join(project, place)
        # Copy only if the copy is missing or older ("getmtime" = time of the
        # last change).
        if not os.path.exists(copy) or os.path.getmtime(copy) < os.path.getmtime(original):
            os.makedirs(os.path.dirname(copy), exist_ok=True)
            shutil.copy2(original, copy)  # copy2 also keeps the file's times
