"""
local_time.py - the one place that says which clock the memory uses

WHAT THIS FILE IS
A Python helper file (a "module"): it is not a hook and never runs on its own.
Hook scripts load it with "import", so all of them use the same clock for the
time line, day folders, chat headings, subagent records and proof dates:
  .claude/hooks/shared/learning_state.py
  .claude/hooks/shared/raw_transcript_copy.py
  .claude/hooks/user-prompt/add-current-time.py
  .claude/hooks/user-prompt/find-missing-takeaways.py
  .claude/hooks/reply-end/save-user-agent-chat.py
  .claude/hooks/subagent-end/save-subagent-record.py
Its name uses an underscore, not a dash, because Python can only import files
whose names have no dashes.

WHY IT EXISTS
Claude Code writes times in UTC (the world standard time), but a "day" in the
notes must be the user's day. So every script asks this file for the time.

WHICH CLOCK IT USES
1. Normally the computer's own clock: the time zone set in the computer's
   settings, with summer time when that zone has it. This is right for almost
   everyone, so nothing has to be set up.
2. A fixed time zone from the user's profile, .claude/learning/profile.md, but
   only when its "Time zone" line holds one, such as "UTC+3" or "UTC-5:30"
   (hours ahead of UTC, or behind it with "-"). This is for a computer whose
   clock runs in another zone than the user's, for example a cloud computer
   that runs on UTC. A fixed zone does not change for summer time.
The /onboard skill shows the user the time and fills in that line only when
the time is wrong.
"""

import os        # works with files and folders
import re        # finds text patterns
from datetime import timedelta, timezone, datetime

# The profile. This file is in .claude/hooks/shared/, so the profile is found
# from this file's own place: two folders up, then learning/profile.md.
PROFILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "learning", "profile.md")

# A fixed zone in the profile, such as "- **Time zone:** UTC+3". The parts in
# brackets are the sign, the hours and, if present, the minutes.
FIXED = re.compile(r"\*\*Time zone:\*\*\s*UTC\s*([+-])\s*(\d{1,2})(?::(\d{2}))?", re.IGNORECASE)


def fixed_zone():
    """The fixed time zone written in the profile, or None when it has none."""
    try:
        with open(PROFILE, encoding="utf-8", errors="replace") as f:
            found = FIXED.search(f.read())
    except OSError:
        return None  # no profile yet
    if not found:
        return None
    sign = -1 if found.group(1) == "-" else 1
    return timezone(sign * timedelta(hours=int(found.group(2)), minutes=int(found.group(3) or 0)))


def now():
    """The current date and time on the user's clock."""
    zone = fixed_zone()
    # ".astimezone()" with nothing in the brackets means: the computer's zone.
    return datetime.now(zone) if zone else datetime.now().astimezone()


def to_local(moment):
    """A moment that carries its own time zone (such as a UTC time from
    Claude Code's records), shown on the user's clock."""
    zone = fixed_zone()
    return moment.astimezone(zone) if zone else moment.astimezone()
