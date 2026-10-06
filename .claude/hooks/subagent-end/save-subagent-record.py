"""
save-subagent-record.py - saves a record of each finished subagent job

WHAT THIS FILE IS
A Python script. Python is a programming language; the program "python3" runs
this file from top to bottom. Text between three quote marks and lines that
start with "#" are explanations for people; Python skips them.

WHY IT EXISTS
A subagent is a helper Claude session that the main agent starts for one job.
When it ends, its prompt (the job it was given) and its answer should stay
readable in the project. This script writes that record automatically, so it is
never forgotten.

WHERE THE RECORD GOES
    .claude/agent-memory/main-agent/YYYY-MM-DD/subagents/<agent-type>/<topic>.md
The day is the day the job finished. The agent type is the kind of subagent,
for example the built-in "general-purpose". The topic is made from the first
words of the prompt.

WHAT THE RECORD CONTAINS
The agent type, the subagent's ID, its status, the path of the copy of its raw
record (made by .claude/hooks/reply-end/backup-raw-transcripts.py), the prompt
and the answer. When the same subagent is resumed and finishes again, its new
answer is added to the same file, when that happens on the same day (the
search looks only in the day's folder).

WHO RUNS IT, AND WHEN
Claude Code runs it through a hook in .claude/settings.json on the moment
"SubagentStop": each time a subagent finishes. Claude Code gives it, as JSON on
its standard input: the subagent's type ("agent_type"), its ID ("agent_id"),
the path of its raw record ("agent_transcript_path") and its final answer
("last_assistant_message").
"""

import glob      # finds files by a name pattern
import json      # reads JSON text
import os        # works with files and folders
import re        # finds and replaces text patterns
import sys       # reads the standard input

# Load the shared rule for where raw-record copies are kept. "sys.path" is the
# list of folders where Python looks for files to import; the "shared" folder
# next to this script's folder is added to it first.
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "shared"))
from raw_transcript_copy import copy_path
from local_time import now as local_now  # the user's clock

raw = sys.stdin.buffer.read().decode("utf-8")
data = json.loads(raw) if raw.strip() else {}

agent_type = (data.get("agent_type") or "").strip()
# Claude Code also runs small internal agents for its own features; they have
# no type. They are not our subagents, so nothing is saved for them.
if not agent_type:
    sys.exit(0)

agent_id = data.get("agent_id", "unknown")
agent_transcript = data.get("agent_transcript_path", "")
main_transcript = data.get("transcript_path", "")
answer = (data.get("last_assistant_message") or "").strip()
project = os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd") or "."
now = local_now()
today = now.strftime("%Y-%m-%d")

# The prompt is the first message in the subagent's raw record (JSONL: one JSON
# object per line). A subagent started by a workflow first gets a fixed
# message that begins with "[Workflow harness"; its real job comes in the next
# message, so that fixed message is skipped.
prompt = ""
if agent_transcript and os.path.exists(agent_transcript):
    with open(agent_transcript, encoding="utf-8", errors="replace") as f:
        for line in f:
            try:
                entry = json.loads(line)
            except ValueError:
                continue
            if entry.get("type") != "user":
                continue
            content = entry.get("message", {}).get("content")
            if isinstance(content, list):
                content = "\n".join(
                    part.get("text", "") for part in content
                    if isinstance(part, dict) and part.get("type") == "text"
                )
            if isinstance(content, str) and content.strip():
                if content.lstrip().startswith("[Workflow harness"):
                    continue
                prompt = content.strip()
                break  # only the first message is the prompt

# The path of the raw-record copy, for example
#     raw-transcripts/2026-10-06/0931_1a2b3c4d/subagents/agent-<id>.jsonl
# The folders are named after the day and time the session started; the
# shared rule decides it. "relative" is the subagent's path inside Claude Code's folder.
raw_copy = ""
if agent_transcript and main_transcript:
    relative = os.path.relpath(agent_transcript, os.path.dirname(main_transcript))
    raw_copy = copy_path(os.path.dirname(main_transcript), relative) or ""

# The topic: the first 6 words of the prompt, in small letters, joined with
# dashes, with every other sign removed. Many prompts start with "Goal:", so a
# first word "goal" is dropped; it would start every name the same way.
words = re.findall(r"[a-z0-9]+", prompt.lower())
if words[:1] == ["goal"]:
    words = words[1:]
words = words[:6]
topic = "-".join(words) or "job"

# The folder: today's day folder, then one folder per agent type.
folder = os.path.join(project, ".claude", "agent-memory", "main-agent", today, "subagents", agent_type)
file_name = f"{topic}.md"
os.makedirs(folder, exist_ok=True)

# If a record of this same subagent (same ID) already exists, add to it.
id_line = f"ID: `{agent_id}`"
for path in glob.glob(os.path.join(folder, "*.md")):
    with open(path, encoding="utf-8") as f:
        if id_line in f.read():
            with open(path, "a", encoding="utf-8", newline="\n") as out:
                out.write(f"\n## Answer after resume ({today} {now:%H:%M})\n\n{answer}\n")
            sys.exit(0)

# A workflow subagent returns its result through a tool, not as text, so its
# answer can be empty. Then the record says where the result is.
if not answer:
    answer = "No text answer. The result is in the raw transcript copy above."

# Otherwise write a new record. If the name is taken, add a number.
path = os.path.join(folder, file_name)
number = 2
while os.path.exists(path):
    path = os.path.join(folder, file_name[:-3] + f"-{number}.md")
    number += 1

with open(path, "w", encoding="utf-8", newline="\n") as f:
    f.write(
        f"# {topic}\n\n"
        f"Agent type: `{agent_type}`\n"
        f"{id_line}\n"
        f"Status: finished\n"
        f"Saved: {today} {now:%H:%M}\n"
        f"Raw transcript copy: `{raw_copy}`\n\n"
        f"## Prompt\n\n{prompt}\n\n"
        f"## Answer\n\n{answer}\n"
    )
