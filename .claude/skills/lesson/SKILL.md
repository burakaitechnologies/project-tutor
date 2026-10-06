---
name: lesson
description: Gives the user a short, hands-on lesson on one concept of the skill tree, tied to this project. With a topic (for example /lesson hooks) it teaches that topic; without one, it picks the best ready concept. The user starts it by typing /lesson.
argument-hint: "[topic, optional]"
disable-model-invocation: true
---

<!--
WHAT THIS FILE IS
A skill: a set of instructions that Claude Code turns into a command. The user
types /lesson, optionally followed by a topic, and the main agent follows the
steps below. Claude Code replaces the word ARGUMENTS with a dollar sign in
front (in the line "Topic the user asked for") with whatever the user typed
after /lesson. The part between the "---" lines at the top is the frontmatter (settings for
Claude Code): "name" is the command, "description" says what it does,
"argument-hint" is the grey hint shown while the user types, and
"disable-model-invocation: true" means only the user can start it; the agent
never starts it by itself. This text between "<!--" and "-->" is a comment
for people.
WHY IT EXISTS
Learning while building covers what the work touches; a lesson lets the user
learn one concept on purpose, by doing it and explaining it back.
WORKS WITH
  .claude/learning/skill-tree/ - the concepts and "Knowing it means"
  .claude/learning/progress/ - the user's status and what is ready
  .claude/templates/proof-entry.md - how the proof is recorded
-->

# Lesson

Topic the user asked for: $ARGUMENTS

1. **Choose the concept.** If a topic is given above, find it in `.claude/learning/skill-tree/` (add a row if it is missing). If no topic is given, choose from the ready concepts in `.claude/learning/progress/overview.md` the one that fits the current work best, preferring Claude Code. If the chosen concept is locked, teach first the concept it needs that the user has not met. Say in one line which concept and why.
2. **Check the facts** if it is a Claude Code feature: look it up in the official docs (`.claude/rules/checking-facts.md`), because features change often.
3. **Ask first.** One short question: what do they already think it is, or what do they predict it does? Wait for the answer before you go on.
4. **Teach it in a few short steps,** each with an example from this project, not a general one. Simple version first. At most about 15 lines in total.
5. **Your turn.** Give them one small, safe thing to do themselves that uses the concept, with the exact thing to type or click. Wait, then look at the result together, and add a `did` entry with their message as the quote.
6. **Explain it back.** Ask them to explain the concept in one or two sentences, as if to a friend. Compare the answer with "Knowing it means": all of it is `explained`, part of it is `partial`, wrong is `missed`. Add the entry with their exact words as the quote, and correct the wrong part in one line.
7. End with the tutor section, with one point that names the concept this one unlocks.
