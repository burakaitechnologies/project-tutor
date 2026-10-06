---
name: progress
description: Shows the user's learning progress as a skill tree - what they know, what is ready to learn next, and what is still locked. The user starts it by typing /progress.
disable-model-invocation: true
---

<!--
WHAT THIS FILE IS
A skill: a set of instructions that Claude Code turns into a command. The user
types /progress, and the main agent follows the steps below. The part between the "---" lines at the top is the frontmatter (settings for
Claude Code): "name" is the command, "description" says what it does, and
"disable-model-invocation: true" means only the user can start it; the agent
never starts it by itself. This text between "<!--" and "-->" is a comment
for people.
WHY IT EXISTS
The progress pages are always up to date, but a short spoken summary with a
recommendation for what to learn next helps the user decide.
WORKS WITH
  .claude/learning/progress/overview.md and the subject pages next to it
  .claude/hooks/after-file-change/update-learning-pages.py - rebuilds the pages
  .claude/learning/progress/proof-log.jsonl - the proof
-->

# Progress report

1. Bring the tree up to date by running `python3 .claude/hooks/after-file-change/update-learning-pages.py`, then read `.claude/learning/progress/overview.md`.
2. Show, in at most 15 lines:
   - the totals line, and each subject's bar (copy them from the file);
   - the newest proof, from the subject pages in `.claude/learning/progress/` (at most 3 lines);
   - 3 ready concepts you recommend next, and why each fits the current work.
3. If the file lists proof entries that did not count, correct those lines first in `.claude/learning/progress/proof-log.jsonl` (how: `.claude/learning/progress/proof-log.jsonl.explained.md`).
4. Tell the user they can open `.claude/learning/progress/overview.md`, and from there each subject's page.
5. End with the tutor section, as in every answer. Make one point a quick check on a concept due for review.
