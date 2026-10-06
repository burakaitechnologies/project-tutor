# Building and maintaining the project

**For:** every agent.

The project keeps growing, so it is never finished. Every change has two sides: build what is new, and maintain everything that already exists, so it stays correct, consistent and aimed at the goal.

## The discipline of always ready to show

The project is private on GitHub, but treat it as public: at any moment, anyone may look at it. Whoever looks must find it organized, explained and consistent. That means:

- every file is in the right place, with a clear name and a clear purpose;
- no leftovers: no unused, temporary, half-finished or replaced files;
- no two files that say different things about the same subject;
- `README.md` describes the project as it is right now.

Leave the project in this state after every answer, not only at the end of a task.

## Before every change: look at the whole

Before the first file change of each answer, the hook `.claude/hooks/before-file-change/show-project-tree.py` stops that change once and shows you the full project tree. Then think, and only then repeat the change:

1. **Does something with the same purpose already exist?** It may be an earlier attempt that was wrong, or built in a different way. If it exists, improve it to the new logic instead of building a second one next to it. If a new version replaces an old one, delete the old one in the same step.
2. **What else states or depends on what you are about to change?** Search the whole project for every place that mentions the behavior, name or fact you change: rules, the output style, `CLAUDE.md`, `README.md`, settings, scripts and their explanations. Plan to update all of them.
3. **If nothing exists yet,** prefer a feature of Claude Code or a standard tool over building your own, and choose the simplest solution that works.

If two existing files already contradict each other, ask the user which one is right before you change either.

Change files with the file tools (Write and Edit), not with shell commands. Then the hook sees every change, and Claude Code shows the user each change.

## After every change: leave it consistent

- Update every place found in step 2 in the same step, so that every file says the same thing.
- Update the tables in `README.md` whenever a folder or an important file is added, moved, renamed or deleted. They say what each part is for, and writing that needs understanding. The full tree at the end of `README.md` is drawn by a hook after every answer; never edit it by hand.
- After every answer of the main agent, a hook looks for file paths in the project's Markdown files (except the memory notes) that point to files which do not exist. When it finds one, handle it before you finish: if a file was moved or renamed, fix the path yourself; if the fix needs a decision, ask the user. Write file references as full paths from the project folder, in backticks, so the check can find them.

## How things are shaped

- **One purpose each.** Every file, folder, rule and hook has exactly one purpose. If something has two, split it. If two things have the same purpose, merge them.
- **Names.** A name says the purpose, in up to 3 words joined with dashes, for example `keeping-memory.md` or `update-project-tree.py`. A longer, clear name is better than a short, unclear one. Exceptions: names Claude Code requires (such as `SKILL.md` and `MEMORY.md`), and Python helper files that other scripts import, which use underscores (such as `learning_state.py`), because Python cannot import names with dashes.
- **`.claude/` stays reusable.** The `.claude/` structure is a template that anyone may copy into their own projects, so files there never contain the project's name, facts about the project itself, or facts about the user. The project's name and facts about the project belong in `CLAUDE.md`, `README.md` and the project's own folders outside `.claude/`. Facts about the user belong only in `.claude/learning/profile.md` (including their time zone, when the computer's clock is not theirs) and in their learning record in `.claude/learning/progress/` (the proof log, any copied messages it quotes, and the pages a hook builds from them). Memory notes are the exception: they record what happened.
- **One fact, one place.** Write each fact in one file only. Other files point to it by its full path from the project folder, with a short reason to read it, because copies drift apart over time.
- **Only what the reader needs.** Leave out the obvious. Explain the important things fully, with an example when they are easy to misunderstand.
- **Hooks or agents.** A hook (a script that Claude Code runs automatically at a fixed moment) never forgets, but it cannot think. Use a hook for every repeated job that needs no judgment, and an agent for jobs that need judgment. Hooks live in `.claude/hooks/`, in one folder per moment they run at (a hook that runs at several moments stays in the folder of its main moment), and helper files that several hooks load live in `.claude/hooks/shared/`; `.claude/settings.json.explained.md` explains when each one runs.
