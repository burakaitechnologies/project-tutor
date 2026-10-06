---
name: quiz
description: A short review round - asks the user 3 to 5 quick questions about concepts they proved before and that are due for review, mixed across topics, and records the answers as proof. The user starts it by typing /quiz.
disable-model-invocation: true
---

<!--
WHAT THIS FILE IS
A skill: a set of instructions that Claude Code turns into a command. The user
types /quiz, and the main agent follows the steps below. The part between the "---" lines at the top is the frontmatter (settings for
Claude Code): "name" is the command, "description" says what it does, and
"disable-model-invocation: true" means only the user can start it; the agent
never starts it by itself. This text between "<!--" and "-->" is a comment
for people.
WHY IT EXISTS
Remembering something on purpose makes it last much longer than reading it
again (this is called "retrieval practice"). Questions about different topics
mixed together help more than several questions on one topic.
WORKS WITH
  .claude/learning/progress/overview.md - what is due for review
  .claude/learning/skill-tree/ - "Knowing it means", for the questions
  .claude/templates/proof-entry.md - how each answer is recorded
-->

# Quiz

1. **Choose 3 to 5 concepts** that are in progress or learned: first the ones in "Time to review" in `.claude/learning/progress/overview.md`, then others with the oldest proof. Mix the subjects and branches. Do not choose concepts first proved today.
2. **Ask one question at a time** and wait for the answer. Build each question from the concept's "Knowing it means" in `.claude/learning/skill-tree/`, so a correct answer is real proof. Short questions, answered in a sentence, tied to this project when possible.
3. **After each answer,** say in one line whether it was right, and correct the wrong part kindly. No long explanations; offer `/lesson <topic>` if they want more.
4. **Add an entry for every answer** to the proof log `.claude/learning/progress/proof-log.jsonl`: `answered` (all correct), `partial` (part correct) or `missed` (wrong), with their exact words as the quote (format: `.claude/templates/proof-entry.md`).
5. At the end, give the score in one line, and the tutor section with one point about the concept they found hardest.
