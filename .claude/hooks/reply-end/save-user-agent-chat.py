"""
save-user-agent-chat.py - saves the user's messages and the main agent's answers

WHAT THIS FILE IS
A Python script. Python is a programming language; the program "python3" reads
this text file and runs its commands from top to bottom. Lines that start with
"#", and text between three quote marks like this one, are explanations for
people; Python skips them.

WHY IT EXISTS
Claude Code keeps a raw record of every conversation, but in a format people
cannot read easily, and outside the project. This script keeps a readable copy
of the conversation inside the project: one file per day, at
.claude/agent-memory/main-agent/YYYY-MM-DD/user-agent-chat.md
It is the archive of every discussion, including ideas that were never agreed.

WHO RUNS IT, AND WHEN
Claude Code runs it through a hook in .claude/settings.json on the moment
"Stop": each time the main agent finishes an answer. Claude Code gives the
script information about that moment as JSON (a text format of names and
values) on its "standard input" (the place a program reads its input from).

WHAT IT DOES
1. Reads that information: the session ID, the path of the raw record, and the
   main agent's final answer.
2. Reads the raw record and finds the user's messages from today, and every piece
   of text the main agent wrote in answer to each one, that are not yet in the
   chat file. The user's own messages are marked there with the origin "human";
   system messages are not saved.
3. Adds them, then the answer that just finished if it is not saved yet, to
   the end of today's file.
Every saved message and answer piece gets a hidden marker <!-- message ID -->
or <!-- answer ID --> so it is never saved twice. Hidden markers are HTML comments: they do not show when the file
is displayed as a formatted page.

WORKS WITH
  .claude/rules/keeping-memory.md                    - the rules for memory
  .claude/hooks/reply-end/backup-raw-transcripts.py  - copies the raw records
  .claude/hooks/shared/raw_transcript_copy.py        - where each copy is kept
"""

# "import" loads ready-made tools from Python's standard library.
import json                                          # reads JSON text
import os                                            # works with files and folders
import re                                            # finds and changes text patterns
import sys                                           # reads the standard input
from datetime import datetime                        # dates and times

NEW_LINE = "\n"

# Load two shared helpers. "sys.path" is the list of folders where Python looks
# for files to import; the "shared" folder next to this script's folder is
# added to it first.
#   copy_path:  the rule for where raw-record copies are kept
#   user_name:  the user's name for the chat headings, from
#               .claude/learning/profile.md ("User" when it has no name yet)
#   local_time: the user's clock
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "shared"))
from raw_transcript_copy import copy_path
from learning_state import user_name, is_user_message
import local_time


def text_of(content):
    """Returns the plain text of a message (some messages are split in parts)."""
    if isinstance(content, list):
        content = NEW_LINE.join(
            part.get("text", "") for part in content
            if isinstance(part, dict) and part.get("type") == "text"
        )
    return content.strip() if isinstance(content, str) else ""


def lower_headings(text):
    """Moves every heading inside a message two levels down ("# A" becomes
    "### A"), so a message never looks like a new message in the chat file,
    where each message starts with a level-2 heading, such as "## 14:24 Sam"
    (the user's name from the learner profile)."""
    return re.sub(r"^(#{1,4}) ", lambda found: "#" * (len(found.group(1)) + 2) + " ",
                  text, flags=re.M)


def time_of(entry):
    """Returns the time of a record entry on the user's clock, or None if it has none."""
    try:
        return local_time.to_local(datetime.fromisoformat(
            entry.get("timestamp", "").replace("Z", "+00:00")))
    except ValueError:
        return None


# Read the JSON that Claude Code sends. ".buffer.read().decode('utf-8')" reads
# the raw bytes and turns them into text with UTF-8, a text encoding that
# supports every language (Windows would otherwise use an older one).
raw = sys.stdin.buffer.read().decode("utf-8")
data = json.loads(raw) if raw.strip() else {}

project = os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd") or "."
session_id = data.get("session_id", "unknown")
transcript_path = data.get("transcript_path", "")
answer = (data.get("last_assistant_message") or "").strip()

now = local_time.now()
user = user_name(project) or "User"
today = now.strftime("%Y-%m-%d")  # for example 2026-10-04

# Today's folder and chat file. "os.makedirs(..., exist_ok=True)" creates the
# folder if it is missing, and does nothing if it already exists.
day_folder = os.path.join(project, ".claude", "agent-memory", "main-agent", today)
os.makedirs(day_folder, exist_ok=True)
chat_path = os.path.join(day_folder, "user-agent-chat.md")

# What the file already contains, so nothing is saved twice.
existing = ""
if os.path.exists(chat_path):
    with open(chat_path, encoding="utf-8") as f:
        existing = f.read()

new_text = []  # a "list": pieces of text to add, in order

# A new file starts with a title and one line about where it comes from.
if not existing:
    new_text.append(
        f"# User-agent chat {today}\n\n"
        "The user's messages and the main agent's answers, saved automatically by "
        "`.claude/hooks/reply-end/save-user-agent-chat.py`.\n"
    )

# The first time a session writes to this file, add a line with its ID and the
# path of its raw-record copy, so anyone can go deeper. The shared rule gives
# the path from the record's folder and file name; it gives None only when the
# record has no time in it yet, which does not happen after an answer.
session_marker = f"<!-- session {session_id} -->"
if session_marker not in existing:
    copy = None
    if transcript_path:
        copy = copy_path(os.path.dirname(transcript_path), os.path.basename(transcript_path))
    new_text.append(
        f"\n{session_marker}\n"
        f"**Session** `{session_id}` - raw transcript copy: "
        + (f"`{copy}`" if copy else "not known yet") + "\n"
    )

# Read the raw record. It is "JSONL": one JSON object per line, each describing
# one event of the session. We split it into "turns": one message from the user,
# followed by the main agent's work until their next message. During a turn the
# main agent often writes several pieces of text between its tool calls (for
# example "Testing the hook now:" and then the final answer). The user sees all
# of them, so all of them are saved, in order.
turns = []  # each turn: [the user's entry, their text, [(answer entry, answer text), ...]]
if transcript_path and os.path.exists(transcript_path):
    with open(transcript_path, encoding="utf-8", errors="replace") as f:
        for line in f:
            try:
                entry = json.loads(line)
            except ValueError:
                continue  # skip a damaged line
            kind = entry.get("type")
            text = text_of(entry.get("message", {}).get("content"))
            if is_user_message(entry) and text:
                turns.append([entry, text, []])
            elif kind == "assistant" and text and turns:
                turns[-1][2].append((entry, text))


def already_saved(piece, marker):
    """True when a piece of text is already in the file, or about to be added:
    found by its hidden marker, or by its full text (the final answer may have
    been saved from what Claude Code sent, before it appeared in the record)."""
    saved = existing + "".join(new_text)
    return marker in saved or lower_headings(piece) in saved


for entry, text, pieces in turns:
    sent = time_of(entry)
    if sent is None or sent.strftime("%Y-%m-%d") != today:
        continue  # messages of other days belong to other files
    marker = f"<!-- message {entry.get('uuid', '')} -->"
    if marker not in existing:
        new_text.append(f"\n{marker}\n## {sent:%H:%M} {user}\n\n{lower_headings(text)}\n")
    # The answer pieces of this turn that are not saved yet. Each gets its own
    # hidden marker; new pieces in a row share one "Main agent" heading.
    heading_written = False
    for piece_entry, piece in pieces:
        piece_marker = f"<!-- answer {piece_entry.get('uuid', '')} -->"
        if already_saved(piece, piece_marker):
            heading_written = False  # a saved piece ends a group of new pieces
            continue
        if not heading_written:
            new_text.append(f"\n## {(time_of(piece_entry) or sent):%H:%M} Main agent\n")
            heading_written = True
        new_text.append(f"\n{piece_marker}\n{lower_headings(piece)}\n")

# The answer that just finished, as Claude Code sent it. It is usually already
# saved above from the record; if the record did not have it yet, it is added
# here, and the full-text check above stops it from being saved twice later.
if answer and not already_saved(answer, "<!-- no marker -->"):
    new_text.append(f"\n## {now:%H:%M} Main agent\n\n{lower_headings(answer)}\n")

# "a" opens the file to add at the end; newline="\n" keeps one line-ending style.
with open(chat_path, "a", encoding="utf-8", newline="\n") as f:
    f.write("".join(new_text))
