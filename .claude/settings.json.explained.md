# settings.json, explained

`.claude/settings.json` is Claude Code's settings file for this project. It is written in JSON, a format for storing settings as names and values. JSON cannot hold comments, so this file explains it. Git saves it, so the settings travel with the project. A second file, `.claude/settings.local.json`, holds settings for this computer only (see the end).

## "outputStyle": "project-tutor"

Chooses the output style: a set of instructions that becomes part of the main agent's system prompt (the base instructions it receives before anything else). Ours is `.claude/output-styles/project-tutor.md`. It makes the main agent the user's project tutor: it builds with them and teaches them in every answer. It applies to every answer and still applies after a compaction. Subagents do not receive it. A change to the output style takes effect in the next new session.

## "hooks"

A hook is a rule: "when this moment comes, run this command". The names inside `"hooks"` are the moments (Claude Code calls them "events"). Each moment holds a list of entries, and each entry can have:

- **`matcher`** (optional): a filter that says in which cases of the moment the entry runs. The sign `|` means "or". Without a matcher, the entry runs in every case. Some moments do not support a matcher.
- **`hooks`**: what to run. `"type": "command"` means "start a program". Other types exist, such as asking a Claude model a question, but we do not use them.

Every hook here starts the same program, `"command": "python3"` (Python 3.9 or newer), and gives it one script to run in `"args"` (the arguments: the extra words a program receives when it starts). This is called the exec form: Claude Code starts the program directly, without a shell (a program that runs typed commands, such as bash or PowerShell). So the hooks work the same way on Windows, macOS and Linux, also when the project's path contains spaces. `${CLAUDE_PROJECT_DIR}` is replaced by the path of the project folder, so every script is found from anywhere. Each script starts with a long explanation of what it does. They live in `.claude/hooks/`, in one folder per moment.

### SessionStart: when the conversation starts fresh

The matcher lists all four cases:

| Case | When it happens |
|---|---|
| `startup` | a new session is opened |
| `resume` | an older conversation is continued |
| `clear` | the user types `/clear` |
| `compact` | after every compaction, automatic or manual |

It runs two scripts. For this moment, everything a script prints is added to the main agent's context.

- `.claude/hooks/session-start/load-session-memory.py` prints the main agent's memory reading list.
- `.claude/hooks/after-file-change/update-learning-pages.py` rebuilds the user's progress pages, so "time to review" fits the new day (it prints nothing). It is the same script that runs after a file change (see PostToolUse).

### UserPromptSubmit: each time a message is sent

This moment has no matcher. It runs three scripts, and what they print is added to the main agent's context next to the message:

- `.claude/hooks/user-prompt/add-current-time.py` prints the current date and time, because Claude has no clock.
- `.claude/hooks/user-prompt/find-missing-takeaways.py` lists earlier days that still need their day takeaways. It prints nothing when no day needs them.
- `.claude/hooks/user-prompt/remind-tutor-role.py` prints a short reminder that the main agent is the user's tutor, plus today's learning details from the skill tree (the full list is in that script's header). Instructions read once at the start of a session get buried after hours of work; a fresh reminder with every message keeps the tutor role alive.

### PreToolUse: just before an agent uses a tool

The matcher `Write|Edit|NotebookEdit` limits it to the tools that change files. It runs `.claude/hooks/before-file-change/show-project-tree.py`. On the first file change of each answer, that script stops the change once and shows the agent the full project tree, so the agent looks at the whole project before it changes anything. The agent then repeats the change, and later changes in the same answer pass. It works this way because, for this moment, a hook's normal extra text reaches the agent only after the tool has run; stopping the call is the only way to show it before.

### PostToolUse: just after an agent used a tool

The matcher `Write|Edit` limits it to the tools that write or change files. It runs `.claude/hooks/after-file-change/update-learning-pages.py`. The script looks at which file was changed and works only when it is inside `.claude/learning/`: for example when the tutor adds a proof entry to `.claude/learning/progress/proof-log.jsonl`. Then it rebuilds the progress pages at once, with every percentage, so the pages always match the proof. When a new proof entry does not count (for example a quote that is not in the user's messages), it ends with exit code 2 and lists the problem, which Claude Code shows to the tutor at once. For every other file it ends at once.

### Stop: each time the main agent finishes an answer

This moment has no matcher. It runs five scripts at the same time. What they print is not shown to the main agent, except when one of the two checks finds a problem. The first three have `"async": true`: they run in the background, so nobody waits for them. The two checks run without it, because they must be able to stop the main agent.

- `.claude/hooks/reply-end/save-user-agent-chat.py` saves the user's messages and the main agent's answers in the day's chat file.
- `.claude/hooks/reply-end/update-project-tree.py` redraws the full file tree at the end of `README.md`.
- `.claude/hooks/reply-end/backup-raw-transcripts.py` copies Claude Code's raw session records into the project.
- `.claude/hooks/reply-end/check-broken-links.py` checks the guide files for broken file paths. If it finds any, it stops the main agent from finishing until they are handled.
- `.claude/hooks/reply-end/check-tutor-section.py` checks that the answer ends with the tutor section (the heading **Tutor**) and that the section has a **Next step:** point. If one is missing, it sends the main agent back once to add it.

### SubagentStop: each time a subagent finishes

This moment has no matcher, so it runs for every subagent. It runs `.claude/hooks/subagent-end/save-subagent-record.py`, which saves the subagent's prompt and answer as a record.

## .claude/settings.local.json

It holds one setting, `autoMemoryDirectory`. It tells Claude Code to keep its built-in auto memory (the file `MEMORY.md`, which Claude Code loads into every session and after every compaction) in `.claude/agent-memory/main-agent/memory/`, inside the project, instead of a hidden folder elsewhere. The path is written in full, because Claude Code accepts only full paths here. That path works only on this computer, so `.gitignore` keeps this file out of Git, and the `/onboard` skill creates it on each new computer.
