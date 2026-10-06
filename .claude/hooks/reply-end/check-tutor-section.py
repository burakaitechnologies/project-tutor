"""
check-tutor-section.py - sends the main agent back when an answer has no tutor section

WHAT THIS FILE IS
A Python script. Python is a programming language; the program "python3" runs
this file from top to bottom. Text between three quote marks and lines that
start with "#" are explanations for people; Python skips them.

WHY IT EXISTS
The user wants to be taught in every answer, like by a personal tutor. Agents
tend to let the teaching disappear during long stretches of building and
debugging, and only report their work. A reminder alone can be ignored.
So this script checks every final answer of the main agent for the tutor
section, which .claude/rules/teaching-while-building.md requires at the end of
every answer. Checking for a fixed mark needs no thinking, so a hook does it.
Whether the teaching is GOOD needs thinking; that stays the agent's job.

THE MARK IT LOOKS FOR
The tutor section starts with the heading "**Tutor**" (the word Tutor in bold)
on a line of its own, and always contains a point that starts with
"**Next step:**". The script looks for both anywhere in the answer.

WHO RUNS IT, AND WHEN
Claude Code runs it through a hook in .claude/settings.json on the moment
"Stop": each time the main agent finishes an answer. (Subagents finish on a
different moment, "SubagentStop", so they are never checked.) Claude Code gives
the script, as JSON on its standard input, the final answer
("last_assistant_message") and "stop_hook_active", which is true when the agent
is already continuing because a Stop hook sent it back.

WHAT IT DOES
- If the answer has both marks, or is empty, it ends quietly.
- If a mark is missing, it ends with "exit code 2" and a reason. For the Stop
  moment, exit code 2 means "do not finish yet": Claude Code shows the reason
  to the agent, which then adds the tutor section in a short extra message.
- It never sends the agent back twice in a row ("stop_hook_active"), so it can
  never cause an endless loop. Known limit: when another Stop check (such as
  the broken-links check) sent the agent back, the next answer is not checked.

WORKS WITH
  .claude/rules/teaching-while-building.md        - what the tutor section contains
  .claude/hooks/user-prompt/remind-tutor-role.py  - the reminder before each answer
"""

import json      # reads JSON text (a format of names and values)
import re        # finds text patterns
import sys       # standard input, standard error and the exit code

raw = sys.stdin.buffer.read().decode("utf-8")
data = json.loads(raw) if raw.strip() else {}

# Already sent back once: let the agent finish.
if data.get("stop_hook_active"):
    sys.exit(0)

answer = data.get("last_assistant_message") or ""
has_heading = re.search(r"(?m)^\s*\*\*Tutor\*\*\s*$", answer)
has_next_step = re.search(r"\*\*Next step:\*\*", answer)
if not answer.strip() or (has_heading and has_next_step):
    sys.exit(0)

# "stderr" (standard error) is where Claude Code reads the reason from. It is
# written as UTF-8 bytes, so every sign shows correctly on Windows.
missing = "no tutor section" if not has_heading else "a tutor section without a **Next step:** point"
reason = (f"Your answer has {missing}. Add it now in a short extra message: a separator line, "
          "the heading **Tutor** on its own line, a **Next step:** point (one sentence: a feature or "
          "tool the user has never met that they can use next), and 1-2 more one-sentence points "
          "(see 'The tutor section' in .claude/rules/teaching-while-building.md). "
          "Do not repeat the answer itself.\n")
sys.stderr.buffer.write(reason.encode("utf-8"))
sys.exit(2)
