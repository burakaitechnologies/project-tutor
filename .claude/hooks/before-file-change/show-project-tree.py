"""
show-project-tree.py - shows the project tree before the first file change of each answer

WHAT THIS FILE IS
A Python script. Python is a programming language; the program "python3" runs
this file from top to bottom. Text between three quote marks and lines that
start with "#" are explanations for people; Python skips them.

WHY IT EXISTS
The project must always be ready to show (see
.claude/rules/building-maintaining-project.md). So before an agent changes any
file, it must look at the whole project: does something with the same purpose
already exist, and what else depends on what it is about to change? Deciding
that needs thinking, so the agent does it. Showing the agent the whole project
at the right moment needs no thinking, so this script does it, every time.

WHO RUNS IT, AND WHEN
Claude Code runs it through a hook in .claude/settings.json on the moment
"PreToolUse": just before an agent uses a tool. The hook's matcher limits it to
the tools that change files: Write (create or replace a file), Edit (change part
of a file) and NotebookEdit (change a notebook). Claude Code gives the script,
as JSON on its standard input, the session ID, the path of the session's raw
record and, inside a subagent, the subagent's ID.

WHAT IT DOES
- On the FIRST file change of each answer, it stops that change ("exit code 2")
  and gives the agent the full project tree from README.md as the reason. For
  this moment, exit code 2 means: do not run this tool call; show the message
  to the agent. The agent reads the tree, thinks, and then repeats the change.
  (The docs say a hook's normal extra text arrives only after the tool has run,
  which would be too late; stopping the call is the only way to show it before.)
- Every later file change in the same answer passes without a stop.

HOW IT KNOWS "THE SAME ANSWER"
Each message the user sends has a unique ID in the raw record. The script reads
the end of the raw record, finds the ID of the user's latest message, and keeps it
in a small note file in the computer's temporary folder (one note per session
and per agent). If the note already holds that ID, the tree was shown in this
answer, and the change passes.

WORKS WITH
  README.md                                          - holds the tree
  .claude/hooks/reply-end/update-project-tree.py     - draws the tree after each answer
  .claude/rules/building-maintaining-project.md      - what the agent does with it
"""

import json      # reads JSON text (a format of names and values)
import os        # works with files and folders
import re        # finds text patterns
import sys       # standard input, standard error and the exit code
import tempfile  # finds the computer's temporary folder

# The shared test for "a message the user typed" lives in learning_state.py.
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "shared"))
from learning_state import is_user_message

raw = sys.stdin.buffer.read().decode("utf-8")
data = json.loads(raw) if raw.strip() else {}

project = os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd") or "."
session_id = data.get("session_id", "unknown")
agent = data.get("agent_id") or "main"          # "main" = the main agent
transcript_path = data.get("transcript_path", "")

# Find the ID of the user's latest message. The raw record can be several
# megabytes, so only its last 2 MB are read ("seek" jumps to a position).
latest_message = ""
if transcript_path and os.path.exists(transcript_path):
    with open(transcript_path, "rb") as f:
        f.seek(0, os.SEEK_END)
        f.seek(max(0, f.tell() - 2_000_000))
        tail = f.read().decode("utf-8", errors="replace")
    for line in tail.splitlines():
        try:
            entry = json.loads(line)
        except ValueError:
            continue  # the first line may be cut in half; skip it
        if is_user_message(entry):
            latest_message = entry.get("uuid", "")

# If the latest message cannot be found, do not block: a missing tree must
# never stop the work.
if not latest_message:
    sys.exit(0)

# The note file that remembers for which message the tree was already shown.
note = os.path.join(tempfile.gettempdir(), f"project-tree-shown-{session_id}-{agent}.txt")
if os.path.exists(note):
    with open(note, encoding="utf-8") as f:
        if f.read().strip() == latest_message:
            sys.exit(0)  # already shown in this answer: let the change run

# Take the tree out of README.md: the part between the two marker lines.
tree = "(README.md has no tree yet)"
readme = os.path.join(project, "README.md")
if os.path.exists(readme):
    with open(readme, encoding="utf-8") as f:
        found = re.search(r"<!-- tree:start -->(.*?)<!-- tree:end -->", f.read(), flags=re.S)
    if found:
        tree = found.group(1).strip()

# Remember that the tree is now shown for this message.
with open(note, "w", encoding="utf-8") as f:
    f.write(latest_message)

# Stop this first change and give the tree as the reason ("stderr", standard
# error, is where Claude Code reads the reason from). The text is written as
# UTF-8 bytes, because on Windows Python would otherwise use an old text format
# that cannot show the tree's line characters (such as "├──").
message = ("Before the first file change of this answer, look at the whole project "
           "(section 'Before every change' in .claude/rules/building-maintaining-project.md). "
           "Then repeat your change; it will not be stopped again in this answer.\n\n"
           "Project tree from README.md:\n" + tree + "\n")
sys.stderr.buffer.write(message.encode("utf-8"))
sys.exit(2)
