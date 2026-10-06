"""
add-current-time.py - adds the current date and time to every message

WHAT THIS FILE IS
A Python script. Python is a programming language; the program "python3" runs
this file from top to bottom. Text between three quote marks and lines that
start with "#" are explanations for people; Python skips them.
It prints one line, for example: 2026-10-04 20:14 Sunday

WHY IT EXISTS
Claude does not have a clock. The main agent needs the real time to write the
time of each process-log entry (see .claude/rules/keeping-memory.md).

WHO RUNS IT, AND WHEN
Claude Code runs it through a hook in .claude/settings.json on the moment
UserPromptSubmit: every time a message is sent. What it prints is added to
Claude's context next to the message.

HOW IT WORKS
The time comes from .claude/hooks/shared/local_time.py, the one place that
says which clock the memory uses, so this line always matches the day folders
and the chat headings. "strftime" writes it in the shape given in quotes:
%Y-%m-%d = year-month-day, %H:%M = hours:minutes, %A = the day's name.
"""

import os        # works with files and folders
import sys       # where Python looks for files to import

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "shared"))
import local_time

# Written as UTF-8 bytes with a plain "\n" at the end: Python's normal "print"
# would end the line with "\r\n" on Windows.
sys.stdout.buffer.write((local_time.now().strftime("%Y-%m-%d %H:%M %A") + "\n").encode("utf-8"))
