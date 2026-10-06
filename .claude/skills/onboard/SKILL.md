---
name: onboard
description: Sets up the tutor for a new user - prepares this computer and this project, fills in the learner profile with a few questions, then finds their starting level in the skill tree with a short placement check. The user starts it by typing /onboard.
disable-model-invocation: true
---

<!--
WHAT THIS FILE IS
A skill: a set of instructions that Claude Code turns into a command. A new
user types /onboard once, at the start, and the main agent follows the steps
below. The part between the "---" lines at the top is the frontmatter (settings for
Claude Code): "name" is the command, "description" says what it does, and
"disable-model-invocation: true" means only the user can start it; the agent
never starts it by itself. This text between "<!--" and "-->" is a comment
for people.
WHY IT EXISTS
The tutor system is meant for anyone, on any computer. A new user starts with
an empty profile and no proof, so the tutor would explain things they already
know, and a few settings depend on their computer. This short setup fixes all
of it in about fifteen minutes. It is also the one place that says how to
start fresh when .claude/ was copied from another user (step 0).
WORKS WITH
  .claude/templates/profile.md        - the blank profile
  .claude/learning/profile.md         - filled in here
  .claude/learning/skill-tree/        - the placement questions
  .claude/templates/proof-entry.md    - how each answer is recorded
  .claude/hooks/shared/local_time.py  - which clock the notes use
-->

# Onboarding

Keep it friendly and quick: one question at a time, short answers welcome. Before each step, say in one sentence what it does and why.

0. **Start fresh, if another person's data is here.** If the profile already has a name, or the proof log has entries, and they belong to someone else, ask the user before you delete anything. Then:
   - copy everything below the comment in `.claude/templates/profile.md` into `.claude/learning/profile.md`;
   - empty `.claude/learning/progress/proof-log.jsonl` (keep the file and its explanation);
   - delete the other person's notes: the day folders (named like 2026-10-06) in `.claude/agent-memory/main-agent/`, and any file of their copied messages in `.claude/learning/progress/`;
   - in `.claude/agent-memory/main-agent/memory/MEMORY.md`, keep only the title and the first paragraph.
1. **This computer.**
   - **Python.** Run `python3 --version`. Every hook runs with Python 3.9 or newer, started as `python3`. If the command fails or shows an older version, stop here and help them install Python from python.org (on Windows, its "Python install manager" also provides `python3`): without it, the reminders, checks and notes do not work.
   - **Memory setting.** If `.claude/settings.local.json` does not exist, create it with one setting, `autoMemoryDirectory`: the full path of the folder `.claude/agent-memory/main-agent/memory` on this computer, with forward slashes, for example `{"autoMemoryDirectory": "C:/Users/sam/my-app/.claude/agent-memory/main-agent/memory"}`. Claude Code accepts only a full path there, so every computer needs its own file (`.claude/settings.json.explained.md` explains it). It takes effect in the next session.
   - **Time.** Show the date and time from the time line of their last message, and ask whether it is their local time. If it is wrong (for example on a cloud computer, which runs on UTC), ask for their time zone and write it in the profile's "Time zone" line, as `UTC+3` or `UTC-5:30`.
2. **This project.** Ask what they want to build here, in one or two sentences ("not decided yet" is fine). Write it under "## The project" in `CLAUDE.md`. In `README.md`, replace the starter kit's welcome text (everything from the line `<!-- starter-kit:start -->` to the line `<!-- starter-kit:end -->`, including both) with a title, that description, and one line saying the project was started from the project-tutor starter kit, with the link given in the welcome text.
3. **Profile.** Ask, one at a time: their name; what they want to become or build; their experience with coding, the terminal, Git and AI tools; which language they prefer for answers and files, and how simple it should be; whether they type or dictate by voice; how they like to learn (short or detailed answers, doing or reading). Write the answers into `.claude/learning/profile.md`, keeping its headings, in plain sentences.
4. **Placement check.** For each subject in `.claude/learning/skill-tree/`, ask two or three short questions about level 1 concepts, starting with the first branch. Build each question from the concept's "Knowing it means". If they clearly know it, move further along the branch; if not, stop that subject there.
5. **Record the proof** in the proof log `.claude/learning/progress/proof-log.jsonl`: `answered` or `partial` with their exact words as the quote (format: `.claude/templates/proof-entry.md`), and `missed` for wrong answers. Do not record concepts they only claim to know; a claim is not proof.
6. **Show the result.** Run `python3 .claude/hooks/after-file-change/update-learning-pages.py`, show the totals and the ready concepts from `.claude/learning/progress/overview.md`, and suggest where to start. Ask them to start a new session once, so the memory setting takes effect.
7. End with the tutor section: one point explains how the tutor will teach from now on (a tutor section in every answer, proof from their own words, the commands `/progress`, `/lesson` and `/quiz`).
