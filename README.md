<!-- starter-kit:start -->
# Project tutor

A starter kit for [Claude Code](https://code.claude.com/docs/en/overview) that turns Claude into your personal tutor while you build real projects. Claude does the work with you, teaches you something in every answer, keeps notes of everything you decide, and tracks what you have learned, with proof in your own words.

It is made for beginners who want to learn Claude Code, Git, GitHub, the terminal and programming by doing, not by watching courses. It is free and open (MIT license).

## What you get

- **A tutor in every answer.** Every answer ends with a short "Tutor" part: one new tool to try next, the idea behind what just happened, and often a small question or task for you.
- **Proof, not guesses.** The tutor never decides by itself that you "know" something. Only your own words count: a quote from your messages, checked word for word by a script. Progress pages show what you have learned in each subject, with percentages.
- **A skill tree.** Over 400 concepts in 6 subjects (Claude Code, Git, GitHub, the terminal, programming, AI and agents), each with what you must be able to say or do to prove it, and what to learn first.
- **Memory across sessions.** Notes of every day (decisions, what was built, what was rejected, and why) and a readable copy of your chats. Every new session starts by reading them.
- **Commands to learn on purpose:** `/onboard` (setup), `/progress`, `/lesson` and `/quiz`.
- **A tidy project.** Every file explains itself in plain words, and this README always shows the full file tree.

## Start in 3 steps

1. **Get your own copy.** Press "Use this template" at the top of this page, then "Create a new repository", and make it **private** (see "Your privacy" below). Then put it on your computer: clone it with Git, or download it as a ZIP file and unpack it.
2. **Open the folder in Claude Code** (the desktop app or the terminal), and trust the folder when Claude Code asks.
3. **Type `/onboard`.** The tutor checks your computer, asks what you want to build and who you are, and finds your level with a few short questions (about 15 minutes). Then start a new session once, and start building.

Already have a project? Copy the `.claude` folder and `CLAUDE.md` into it (if it already has a `CLAUDE.md`, add the lines of this one to yours), then type `/onboard`.

## What you need

- [Claude Code](https://code.claude.com/docs/en/setup), and a Claude account that can use it.
- **Python 3.9 or newer, started as `python3`.** To check, type `python3 --version` in a terminal. On Windows, install Python with the "Python install manager" from python.org, which provides `python3`.
- Git is recommended, to save versions of your work, but not required.

Tested on Windows. macOS and Linux should work, because every hook is a Python script that Claude Code starts without a shell, but they are not tested yet. If something breaks, please open an issue.

## What it costs

Every message carries a short reminder for the tutor (about 400 tokens), and every session starts by reading the newest notes (up to about 22,000 tokens after a month of daily use). Tokens are the units Claude's usage is counted in, so expect somewhat more usage than with plain Claude Code.

## Your privacy

Your copy keeps your chats, your profile and your learning record as files inside the project, in `.claude/agent-memory/` and `.claude/learning/`. Keep your copy **private** on GitHub. The kit's scripts never send anything over the internet.

## Updating

To get a newer version, copy its `.claude` folder over yours, but keep your own files: `.claude/learning/profile.md`, the folder `.claude/learning/progress/`, the folder `.claude/agent-memory/`, and `.claude/settings.local.json`.

## License

MIT: you may use, copy, change and share this kit, also in paid work, as long as you keep the copyright notice in `LICENSE`. This is a community project; it is not made or endorsed by Anthropic.

Started by Burak: https://github.com/burakaitechnologies/project-tutor
<!-- starter-kit:end -->

## Map of the project

This file is the map of the project. It says what every folder and important file is for and when to read it, and at the end it shows a full tree of all files. Other files point here instead of repeating the map. What the project is, and who it is for, is explained in `CLAUDE.md`.

**Claude Code** is an AI coding tool: Claude reads and writes the files in this folder and runs commands, while the user guides it in a chat. The Claude session the user talks to is the **main agent**; here it works as the user's **project tutor**, building with them and teaching them in every answer. It can start **subagents**: helper Claude sessions that each do one job and report back.

## Files at the top

| File | What it is | Read it when |
|---|---|---|
| `README.md` | this map | you need to find something |
| `CLAUDE.md` | what the project is, the clarity standard, and the agents; it loads the learner profile; every agent reads it | you want to know what every agent is told |
| `.gitignore` | the list of files that Git (the tool that saves versions of the project) must never save | a file must stay on this computer only |
| `.gitattributes` | keeps every text file in Linux line endings (LF) on every computer, the style the hooks write | rarely |
| `LICENSE` | the MIT license: anyone may use, copy, change and share this kit, as long as they keep its copyright notice | you want to reuse the kit |

## The project's own work

Nothing yet. When you build something here, add each folder or important file of your own work to this section: what it is, and when to read it.

## How Claude works here: `.claude/`

Everything in `.claude/` is a reusable template: anyone can copy it into their own project. Which files hold one person's data is written in `.claude/rules/building-maintaining-project.md`. To give `.claude/` to a new user, copy it and run `/onboard`: its first step clears the earlier user's data.

| Path | What it is | Read it when |
|---|---|---|
| `.claude/output-styles/project-tutor.md` | makes the main agent the user's project tutor: how it builds, teaches and talks; part of its base instructions. Subagents do not see it | you want to change the main agent's behavior |
| `.claude/rules/teaching-while-building.md` | main agent: the teaching method, proof of learning, the tutor section at the end of every answer, and the reminder a hook repeats with every message | you want to change how you are taught |
| `.claude/rules/checking-facts.md` | every agent: never present something unchecked as a fact; where to check | you want to know how facts are checked |
| `.claude/rules/explaining-files.md` | every agent: how files are explained so a beginner understands them fully | you want to change how files are explained |
| `.claude/rules/building-maintaining-project.md` | every agent: the discipline of always ready to show; what to do before and after every change | you want to change how the project is built and kept in order |
| `.claude/rules/keeping-memory.md` | every agent: what is remembered, where, and when | you want to understand the memory |
| `.claude/rules/using-subagents.md` | main agent: when and how to use helper agents | you want to understand delegation |
| `.claude/skills/` | commands the user can type: `/progress` (the skill tree and what comes next), `/lesson` (a short hands-on lesson), `/quiz` (a short review round), `/onboard` (setup for a new user). Each skill is a folder with a `SKILL.md` file | you want to learn on purpose, not only while building |
| `.claude/settings.json` | project settings: the output style and the hooks (scripts that run automatically). Explained in `.claude/settings.json.explained.md` | you want to change how Claude Code behaves here |
| `.claude/settings.local.json` | settings for this computer only (not in Git) | rarely |
| `.claude/hooks/` | the hook scripts, in one folder per moment they run at (for example `.claude/hooks/before-file-change/`, `.claude/hooks/after-file-change/` and `.claude/hooks/reply-end/`); each script explains itself at the top. `.claude/hooks/shared/` holds helper files that several hooks load. All of them are Python scripts, started as `python3` (Python 3.9 or newer) | you want to see what happens automatically |
| `.claude/templates/` | blank templates, each with a short header: a process-log entry, a day's takeaways, one proof entry, and the learner profile | a new note, proof entry or profile is created |

`CLAUDE.md` and the files in `.claude/rules/` load into every agent automatically.

## What the user learns: `.claude/learning/`

| Path | What it is | Read it when |
|---|---|---|
| `.claude/learning/profile.md` | who the user is and how they like to learn; loaded into every session | you want to change how the tutor treats you |
| `.claude/learning/skill-tree/` | everything there is to learn, one file per subject (Claude Code, Git, GitHub, terminal, programming, AI and agents), split into branches and concepts, with what each concept needs first. The same for every user | you want to see or change what can be learned |
| `.claude/learning/progress/` | what this user has learned. A hook rebuilds the pages the moment the proof changes | you want to see your progress |
| `.claude/learning/progress/overview.md` | one short page: a progress bar per subject, what to learn next, what to review | you want to see where you stand |
| `.claude/learning/progress/<subject>.md` | one page per subject: each branch with its bar, your own words under every concept you proved, what is ready next, and how many concepts are locked | you want to see the details of one subject |
| `.claude/learning/progress/proof-log.jsonl` | the tutor's raw record: one line of JSON per piece of proof, each with the timestamp, the concept and the user's own words; all statuses are calculated from it | rarely; the pages above show the same proof, sorted |
| `.claude/learning/progress/proof-log.jsonl.explained.md` | what every field and kind of the proof log means, when a line may be corrected, and how to reset the folder for a new user | you want to understand or check the proof |

## The memory: `.claude/agent-memory/`

| Path | What it is |
|---|---|
| `.claude/agent-memory/main-agent/memory/MEMORY.md` | an inbox for small lessons; loaded automatically |
| `.claude/agent-memory/main-agent/raw-transcripts/` | copies of Claude Code's raw session records, one folder per session, inside a folder for the day it started (on this computer only, not in Git) |
| `.claude/agent-memory/main-agent/<date>/` | one folder per day, with the files below |
| `process-log.md` | the settled events of the day: decisions, actions, verified facts, rejected ideas |
| `day-takeaways.md` | what the day taught; written after the day is over |
| `user-agent-chat.md` | the user's messages and the main agent's answers, saved automatically |
| `.claude/agent-memory/main-agent/<date>/documents/` | things the main agent produced that day, such as proposals and reports |
| `.claude/agent-memory/main-agent/<date>/subagents/` | records of helper jobs done that day (prompt and answer), saved automatically |

**Where to start reading:** the newest `day-takeaways.md`, then the newest `process-log.md`.

## Full tree of all files

Drawn automatically by `.claude/hooks/reply-end/update-project-tree.py`; do not edit it by hand. A folder with more than 10 items shows 10 and how many more; folders named by date show the newest first. Every item that Git ignores (listed in `.gitignore`) is shown once as "(local only, not in Git)", and the contents of such a folder are not listed.

<!-- tree:start -->
```text
project-tutor/
├── .claude/
│   ├── agent-memory/
│   │   └── main-agent/
│   │       └── memory/
│   │           └── MEMORY.md
│   ├── hooks/
│   │   ├── after-file-change/
│   │   │   └── update-learning-pages.py
│   │   ├── before-file-change/
│   │   │   └── show-project-tree.py
│   │   ├── reply-end/
│   │   │   ├── backup-raw-transcripts.py
│   │   │   ├── check-broken-links.py
│   │   │   ├── check-tutor-section.py
│   │   │   ├── save-user-agent-chat.py
│   │   │   └── update-project-tree.py
│   │   ├── session-start/
│   │   │   └── load-session-memory.py
│   │   ├── shared/
│   │   │   ├── ignored_paths.py
│   │   │   ├── learning_state.py
│   │   │   ├── local_time.py
│   │   │   └── raw_transcript_copy.py
│   │   ├── subagent-end/
│   │   │   └── save-subagent-record.py
│   │   └── user-prompt/
│   │       ├── add-current-time.py
│   │       ├── find-missing-takeaways.py
│   │       └── remind-tutor-role.py
│   ├── learning/
│   │   ├── profile.md
│   │   ├── progress/
│   │   │   ├── ai-agents.md
│   │   │   ├── claude-code.md
│   │   │   ├── git.md
│   │   │   ├── github.md
│   │   │   ├── overview.md
│   │   │   ├── programming.md
│   │   │   ├── proof-log.jsonl
│   │   │   ├── proof-log.jsonl.explained.md
│   │   │   └── terminal.md
│   │   └── skill-tree/
│   │       ├── ai-agents.md
│   │       ├── claude-code.md
│   │       ├── git.md
│   │       ├── github.md
│   │       ├── programming.md
│   │       └── terminal.md
│   ├── output-styles/
│   │   └── project-tutor.md
│   ├── rules/
│   │   ├── building-maintaining-project.md
│   │   ├── checking-facts.md
│   │   ├── explaining-files.md
│   │   ├── keeping-memory.md
│   │   ├── teaching-while-building.md
│   │   └── using-subagents.md
│   ├── settings.json
│   ├── settings.json.explained.md
│   ├── skills/
│   │   ├── lesson/
│   │   │   └── SKILL.md
│   │   ├── onboard/
│   │   │   └── SKILL.md
│   │   ├── progress/
│   │   │   └── SKILL.md
│   │   └── quiz/
│   │       └── SKILL.md
│   └── templates/
│       ├── day-takeaways.md
│       ├── process-entry.md
│       ├── profile.md
│       └── proof-entry.md
├── .gitattributes
├── .gitignore
├── CLAUDE.md
├── LICENSE
└── README.md
```
<!-- tree:end -->
