"""
remind-tutor-role.py - reminds the main agent, with every message, that it is the user's tutor

WHAT THIS FILE IS
A Python script. Python is a programming language; the program "python3" runs
this file from top to bottom. Text between three quote marks and lines that
start with "#" are explanations for people; Python skips them.

WHY IT EXISTS
The main agent's tutor instructions are read once, at the start of a session.
After an hour of work they are buried under thousands of lines of newer
conversation, and the agent slowly falls back to acting like a plain assistant.
Studies of long conversations show that a short reminder, placed next to each
new message and aimed at the exact behavior, prevents this far better than a
general one. So this script puts such a reminder next to EVERY message the user
sends, together with today's specifics from the user's skill tree: what is due
for review, what is ready to learn, and proof entries that need fixing.
Choosing what to teach from that list needs thinking, so the agent does that.

WHO RUNS IT, AND WHEN
Claude Code runs it through a hook in .claude/settings.json on the moment
"UserPromptSubmit": every time a message is sent. For this moment, everything
the script prints is added to the agent's context next to the message. The user
does not see it in the chat.

WHAT IT PRINTS (about 1,000 characters, about 250 tokens; it stays in the
conversation every time, so it must stay short)
1. The user's name, from .claude/learning/profile.md.
2. The reminder: the text between the marker lines "<!-- reminder:start -->"
   and "<!-- reminder:end -->" in .claude/rules/teaching-while-building.md.
   The text lives only there (one fact, one place); this script copies it.
3. How many concepts have each status.
4. Up to 2 concepts due for review.
5. Ideas for the "Next step" point: 5 concepts the user has no proof of yet
   and is ready for, Claude Code first, rotating with every message.
6. The newest proved concepts (for the learning line at the start of a session).
7. Up to 3 proof entries that did not count, so the agent fixes them.
The statuses are calculated by .claude/hooks/shared/learning_state.py.

WORKS WITH
  .claude/rules/teaching-while-building.md          - the reminder text and the rules
  .claude/hooks/shared/learning_state.py            - calculates the statuses
  .claude/hooks/reply-end/check-tutor-section.py    - checks that answers follow the reminder
"""

import json      # reads JSON text
import os        # works with files and folders
import re        # finds text patterns
import sys       # standard input and output

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "shared"))
import learning_state as ls

raw = sys.stdin.buffer.read().decode("utf-8") if not sys.stdin.isatty() else ""
data = json.loads(raw) if raw.strip() else {}
project = os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd") or "."

out = ["=== Tutor reminder (from .claude/hooks/user-prompt/remind-tutor-role.py) ==="]
name = ls.user_name(project)
out.append(f"The user's name: {name}." if name else
           "The user's profile is empty: offer the /onboard skill to set it up.")

rule = ls.read(os.path.join(project, ".claude", "rules", "teaching-while-building.md"))
found = re.search(r"<!-- reminder:start -->(.*?)<!-- reminder:end -->", rule, flags=re.S)
if found:
    out.append(found.group(1).strip())

subjects, concepts, state, problems = ls.compute(project, data.get("transcript_path"))
if concepts:
    c = ls.counts(state)
    out.append("")
    out.append(f"Skill tree now: {c['learned']} learned, {c['in progress']} in progress, "
               f"{c['not started']} not started. Pages: .claude/learning/progress/")
    def describe(cid):
        concept = concepts[cid]
        return f"{cid} {concept['name']} ({concept['subject']} › {concept['branch']})"
    due = ls.due_for_review(concepts, state, 2)
    if due:
        out.append("Due for a quick check: " + "; ".join(map(describe, due)) + ".")
    # Ideas for the "Next step" point: concepts the user has no proof of yet
    # and is ready for, Claude Code first (it matters most). What the tutor
    # suggests is not recorded, so the list would repeat; instead it ROTATES:
    # the number of messages the user has sent so far decides where in the pool
    # the list starts, so each message shows other ideas. The tutor still picks
    # the idea that fits what the user will do next.
    pool = [cid for b in subjects[0]["branches"] for cid in b["ids"]
            if ls.is_ready(cid, concepts, state) and concepts[cid]["level"] in ("1", "2")] if subjects else []
    pool += ls.ready_next(subjects[1:], concepts, state, 8) if len(subjects) > 1 else []
    if pool:
        # Count the messages the user has sent in this session.
        turn = 0
        for line in ls.read(data.get("transcript_path") or "").splitlines():
            try:
                turn += ls.is_user_message(json.loads(line))
            except (ValueError, AttributeError):
                pass  # a line that is not a JSON object
        start = (turn * 5) % len(pool)
        ideas = (pool[start:] + pool[:start])[:5]
        out.append("Next step ideas (no proof yet, ready): " + "; ".join(map(describe, ideas)) + ".")
    # The newest proved concepts, for the learning line at the start of a session.
    proved = sorted(((s["last"], cid) for cid, s in state.items()
                     if s["status"] in ("in progress", "learned")), reverse=True)[:3]
    if proved:
        out.append("Latest proof: " + "; ".join(f"{concepts[cid]['name']} ({state[cid]['status']}, {d})"
                                                for d, cid in proved) + ".")
    if problems:
        out.append("Proof entries that did not count; correct those lines: " + " | ".join(problems[:3]))

# Write as UTF-8 bytes, so every sign shows correctly on Windows.
sys.stdout.buffer.write(("\n".join(out) + "\n").encode("utf-8"))
