# Explaining files

**For:** every agent that creates or edits a file.

The user can open any file of the project next to the chat and read it. Every file must be understandable to them on its own, following the clarity standard in `CLAUDE.md`.

## First time, last time

- **First time:** when the user opens a file for the first time, the file itself teaches them everything they need to understand it. They do not need a search engine, another file, or a question to you.
- **Last time:** after reading it once, they understand it fully. They never need to open it again to understand it, and they could explain it to someone else.

Example. A script line `cd "$DIR" || exit 0` with no explanation fails this test. The explained version says what `cd` does (it moves into a folder), what `$DIR` holds (the path of that folder), what `||` means (run the next part only if the first part fails), and why the script stops quietly at this point.

Clarity is more important than file size. Explanations are never extra weight; never remove them to save space.

## What every file contains

1. A header at the top: what the file is, what it is for, and which other files it works with.
2. An explanation of every term where it first appears in the file: what it is in general, and what it does here.
3. An explanation of how it works: how the parts connect, why each part is there, and what would break without it.

## How to write the explanations

- Use the comment format of the file's own language. Every file type that allows comments gets them.
- A file type that cannot hold comments (for example JSON) gets a separate file next to it, with the same name plus `.explained.md`. A local-only settings file is explained in the `.explained.md` of its main settings file.
- When you edit a file that has no explanations, explain the parts you touched.
- When the user asks you to explain a file, add the explanations, change nothing else, and tell them in at most 3 lines what the file does.

## Not covered

Memory notes in `.claude/agent-memory/` (they follow `.claude/rules/keeping-memory.md`), and generated files such as lock files. Markdown documents explain their own terms in plain text.
