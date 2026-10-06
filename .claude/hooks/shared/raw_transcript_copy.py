"""
raw_transcript_copy.py - the one place that says where a raw-record copy is kept

WHAT THIS FILE IS
A Python helper file (a "module"): it is not a hook and never runs on its own.
Three hook scripts load it with "import", so they all follow the same rule:
  .claude/hooks/reply-end/backup-raw-transcripts.py   makes the copies
  .claude/hooks/reply-end/save-user-agent-chat.py     writes a session's copy path
  .claude/hooks/subagent-end/save-subagent-record.py  writes a subagent's copy path
It lives in "shared/" and not in a folder named after a moment, because it is
used by hooks of two different moments. Its name uses underscores, not dashes,
because Python can only import files whose names have no dashes.

THE RULE
Claude Code keeps a raw record ("transcript") of every session, named after the
session ID (a random code that names one session, for example
"1a2b3c4d-5e6f-4a1b-8c2d-3e4f5a6b7c8d"). It keeps a session's subagents in a
folder with the same ID:
    <session-id>.jsonl                          the main conversation
    <session-id>/subagents/agent-<id>.jsonl     one record per subagent
In the project, every session gets one folder of its own, inside a folder for
the day it started (on the user's clock, from .claude/hooks/shared/local_time.py). The session
folder's name is its start time (hours and minutes) and the first 8 characters
of its ID:
    raw-transcripts/2026-10-06/0931_1a2b3c4d/<session-id>.jsonl
    raw-transcripts/2026-10-06/0931_1a2b3c4d/subagents/agent-<id>.jsonl
Because the names start with the date and the time, sorting by name also sorts
by time. A session that goes on for several days stays in its one folder, under
the day it started. The record inside keeps the full ID, so a search for an ID
from a chat file finds it.

WHY IT STAYS CORRECT OVER YEARS
- The start is the first time written in a record, and a record only grows at
  its end, so a session's folder name never changes.
- Folders are created only when a record is copied into them, so there is never
  an empty day folder.
- Claude Code deletes its own records after 30 days, so the backup hook only
  ever looks at about one month of records, however old the project gets. The
  copies here are never deleted.
"""

import json      # reads JSON text (a format of names and values)
import os        # works with files and folders
from datetime import datetime

from local_time import to_local  # the user's clock, from .claude/hooks/shared/local_time.py

# Where the copies are kept, as a path from the project folder.
RAW_COPIES = ".claude/agent-memory/main-agent/raw-transcripts"



def session_start(record):
    """Returns the moment a raw record starts, as the day folder and the time,
    such as "2026-10-06/0031" (on the user's clock), or None when it cannot be known
    yet. Each line of the
    record is one JSON entry; most entries carry a "timestamp" in UTC, such as
    "2026-10-05T18:20:33.123Z". The first one is the start.
    It never guesses with the current time: a guess would give the same session
    a second folder later, once the record has its real start."""
    if record and os.path.exists(record):
        with open(record, encoding="utf-8", errors="replace") as f:
            for line in f:
                try:
                    stamp = json.loads(line).get("timestamp")
                except (ValueError, AttributeError):
                    continue  # a line that is not a JSON entry: skip it
                if stamp:
                    moment = datetime.fromisoformat(stamp.replace("Z", "+00:00"))
                    return to_local(moment).strftime("%Y-%m-%d/%H%M")
    return None


def copy_path(claude_folder, relative):
    """Returns where the copy of one raw record is kept, as a path from the
    project folder, or None when the session's start is not known yet.
    claude_folder: Claude Code's folder that holds this project's records.
    relative: the record's path inside that folder, for example
    "<session-id>.jsonl" or "<session-id>/subagents/agent-<id>.jsonl"."""
    parts = relative.replace("\\", "/").split("/")
    # The first part is always the session ID ("removesuffix" drops ".jsonl").
    session_id = parts[0].removesuffix(".jsonl")
    # The start comes from the main conversation's record. If that record is
    # missing, the record itself is used.
    main_record = os.path.join(claude_folder, session_id + ".jsonl")
    if not os.path.exists(main_record):
        main_record = os.path.join(claude_folder, relative)
    start = session_start(main_record)
    if start is None:
        return None
    # Inside the session's folder: the main record keeps its own name; for a
    # subagent, the session-ID part of the path is dropped ("subagents/...").
    inside = parts[0] if len(parts) == 1 else "/".join(parts[1:])
    return f"{RAW_COPIES}/{start}_{session_id[:8]}/{inside}"
