# Claude Code

One subject of the skill tree: everything a beginner can learn about Claude Code, split into branches (topics) in learning order. Each row is one concept: its ID, its name, one plain sentence, what the learner must say or do to prove they know it, the concepts it needs first ("-" means none), and its level (1 first week, 2 soon, 3 advanced). This file is the same for every user; what one user has learned is in `.claude/learning/progress/overview.md`. How the tutor uses it: `.claude/rules/teaching-while-building.md`.

## Branch: Getting started
What Claude Code is, how to start it, and the basic actions it takes in your project.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| cc-what-is-claude-code | What Claude Code is | Claude Code is an AI helper that reads your project, changes files, and runs commands for you when you ask in normal words. | Explain what Claude Code can do in a project, and how it differs from a normal chat with an AI. | - | 1 |
| cc-install-sign-in | Installing and signing in | You install Claude Code once and log in with your Claude account so it can work for you. | Install Claude Code, log in with your account, and check that it starts. | cc-what-is-claude-code | 1 |
| cc-surfaces | Surfaces (CLI, Desktop, IDE, web, mobile) | You can use the same Claude Code in a terminal, the desktop app, a code editor, a web browser, or your phone. | Name the places where you can use Claude Code, and say which one you use and why. | cc-what-is-claude-code | 1 |
| cc-desktop-code-tab | Desktop app Code tab | The Claude desktop app has a Code tab where you choose a project folder and chat with Claude about it in a friendly window. | Open the Code tab, choose a project folder, and start a chat about that folder. | cc-install-sign-in, cc-surfaces | 1 |
| cc-cli | CLI (terminal) version | You can also run Claude Code by typing `claude` in a terminal, which gives you every feature and works anywhere. | Start Claude Code by typing claude inside a project folder in a terminal, and close it again. | cc-install-sign-in, term-working-directory | 1 |
| cc-trust-dialog | Project trust dialog | The first time you open a folder, Claude Code asks if you trust it, because files in a project can change how Claude behaves. | Explain why Claude Code asks you to trust a folder, and when you should say no. | cc-install-sign-in | 1 |
| cc-sessions | Sessions | A session is one conversation with Claude about your project, from when you start it until you close it. | Explain what a session is, start a new one, and say what Claude does not remember from earlier sessions. | cc-install-sign-in, ai-statelessness | 1 |
| cc-good-request | Writing a good request | Telling Claude clearly what you want, why you want it, and how to check it is done gives much better results. | Write a request that says what you want, why, and how Claude can check that it is done. | cc-sessions, ai-prompt-writing | 1 |
| cc-tools | Tools overview | Tools are the actions Claude can take, like reading a file, changing a file, running a command, or searching the web. | Name four Claude Code tools and what each does, and spot when Claude uses a tool during its work. | cc-sessions, ai-agent-loop | 1 |
| cc-read-write-edit-tools | Read, Write and Edit tools | Claude uses these tools to open files, create new files, and change small parts of files that already exist. | Say which of Read, Write and Edit Claude uses to look at a file, create one, or change part of one. | cc-tools, term-files-folders | 1 |
| cc-bash-powershell-tools | Bash and PowerShell tools | These tools let Claude type commands into a terminal for you, like starting your program or installing something. | Explain that Claude runs real terminal commands with these tools, and read and explain one command it wants to run. | cc-tools, term-running-programs | 1 |
| cc-ask-user-question | AskUserQuestion tool | Claude can stop and give you a few choices to pick from when it needs you to decide something. | Answer a choice question from Claude, and know you can type your own answer instead. | cc-tools | 1 |
| cc-task-checklist | Claude's task checklist | For bigger jobs Claude keeps a checklist of steps, and you can show or hide it with Ctrl+T. | Read Claude's checklist to see what is done and what is next, and show or hide it with Ctrl+T. | cc-tools | 1 |
| cc-pasting-images | Pasting images | You can paste a screenshot into the chat so Claude can see what you see. | Paste a screenshot into the chat, and ask Claude a question about it. | cc-sessions | 1 |
| cc-glob-grep-tools | Glob and Grep tools | These tools let Claude find files by their names and find words inside files. | Say which tool finds files by name and which one finds words inside files. | cc-read-write-edit-tools | 2 |
| cc-websearch-webfetch-tools | WebSearch and WebFetch tools | These tools let Claude search the internet and read a web page. | Explain how searching the web differs from reading one page, and why web results can be wrong. | cc-tools, ai-knowledge-cutoff | 2 |

## Branch: Modes & permissions
How Claude asks before it acts, and how to choose how much it may do on its own.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| cc-permission-prompts | Permission prompts | Before Claude does something that could change your computer, it asks you to allow or refuse it. | Read a permission prompt, say what will happen if you allow it, and choose to allow or refuse. | cc-tools, ai-human-in-the-loop | 1 |
| cc-permission-modes | Permission modes | A mode decides how often Claude asks you before it acts, from asking every time to almost never asking. | Name the main modes, and put them in order from the most asking to the least asking. | cc-permission-prompts | 1 |
| cc-manual-mode | Manual mode (default) | In this mode Claude can only read on its own and asks you before every change or command. | Say what Claude may do alone in manual mode, and what it must ask you for. | cc-permission-modes | 1 |
| cc-accept-edits-mode | acceptEdits mode | In this mode Claude changes files without asking, but still asks before running most commands. | Say what acceptEdits allows without asking, what still needs your yes, and when it is a good choice. | cc-permission-modes | 1 |
| cc-plan-mode | Plan mode | In plan mode Claude only looks and thinks, then shows you a plan to approve before it changes anything. | Use plan mode for a task, read the plan, and approve it or ask for changes before any file changes. | cc-permission-modes | 1 |
| cc-auto-mode | Auto mode | In auto mode Claude works without asking, while a safety checker in the background blocks dangerous actions. | Explain what auto mode does, what the checker blocks, and why you still review the result. | cc-permission-modes | 1 |
| cc-switching-modes | Switching modes with Shift+Tab | Pressing Shift+Tab moves you between the permission modes. | Move between modes with Shift+Tab, and read which mode is on now. | cc-permission-modes | 1 |

## Branch: Session commands
The slash commands that start, find, name, and manage your conversations.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| cc-slash-commands | Slash commands | Typing / at the start of your message opens a menu of commands that control Claude Code itself. | Open the command menu with / and run one command, and explain how a command differs from a normal message. | cc-sessions | 1 |
| cc-help | /help | This command shows help and lists the commands you can use. | Run /help, and find a command you did not know. | cc-slash-commands | 1 |
| cc-clear | /clear | This command starts a fresh conversation so old talk no longer confuses Claude. | Use /clear before a new task, and explain that the chat is forgotten but your files stay. | cc-slash-commands, ai-context-window | 1 |
| cc-resume-continue | /resume and claude --continue | These let you go back to an earlier conversation and continue where you stopped. | Go back to your last session with claude --continue, and pick an older one with /resume. | cc-slash-commands | 1 |
| cc-status-config | /status and /config | These commands show your version, model and account, and let you change settings from a menu. | Use /status to see your version, model and account, and change one setting in /config. | cc-slash-commands | 1 |
| cc-powerup | /powerup lessons | This command gives short interactive lessons that teach you Claude Code features. | Start /powerup, and finish one lesson. | cc-slash-commands | 1 |
| cc-rename | /rename and session names | You can give a session a name so it is easy to find again later. | Give a session a clear name, and find it by that name in /resume. | cc-resume-continue | 2 |
| cc-branch | /branch | This command makes a copy of the conversation so you can try a different idea without losing the original. | Use /branch to try another idea, and explain that the original conversation stays as it was. | cc-resume-continue | 2 |
| cc-btw | /btw side questions | This command lets you ask a quick side question without adding it to the main conversation. | Ask a side question with /btw, and explain why this keeps the main conversation clean. | cc-slash-commands, ai-context-window | 2 |
| cc-export-copy | /export and /copy | These commands save the conversation as text or copy Claude's last answer. | Copy Claude's last answer with /copy, and save the whole conversation with /export. | cc-slash-commands | 2 |
| cc-recap | /recap | This command gives a one-line summary of what has happened in the session so far. | Use /recap after a break to see what happened so far. | cc-slash-commands | 2 |
| cc-feedback-bug | /feedback and /bug | These commands send a report about a problem or an idea to the Claude Code team. | Send a report with /feedback, and say what to write so the team can understand the problem. | cc-slash-commands | 2 |
| cc-updating | Updating Claude Code | Claude Code gets new features often, and `claude update` and /release-notes help you stay up to date. | Update Claude Code, check its version, and read what is new with /release-notes. | cc-status-config | 2 |

## Branch: Keyboard & screen
Keys and views that help you steer Claude while it works and see what it did.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| cc-esc-interrupt | Interrupting with Esc | Pressing Esc stops Claude in the middle of its work so you can give a new direction. | Stop Claude with Esc during a task, and give it a new direction without losing the conversation. | cc-sessions | 1 |
| cc-ctrl-c-ctrl-d | Ctrl+C and Ctrl+D | Ctrl+C stops work or clears your text, and pressing it twice or using Ctrl+D closes Claude Code. | Clear your typed text with Ctrl+C, and close Claude Code with Ctrl+C twice or with Ctrl+D. | cc-cli, term-stopping-program | 1 |
| cc-multiline | Writing on several lines | You can press Shift+Enter to start a new line in your message, and /terminal-setup can fix this key if it does not work. | Write a message on several lines with Shift+Enter, and know that /terminal-setup fixes it if it fails. | cc-sessions | 1 |
| cc-shell-mode | Shell mode with ! | Starting a message with ! runs that command yourself, and Claude sees the result and can respond to it. | Run a command with !, and explain how this differs from asking Claude to run it. | cc-sessions, term-running-programs | 1 |
| cc-shortcut-help | Shortcut help with ? | Typing ? on an empty line shows a list of keyboard shortcuts. | Open the shortcut list with ?, and find one shortcut you did not know. | cc-sessions | 1 |
| cc-queueing | Queueing messages | You can type a new message while Claude is still working and it will be sent when Claude is ready. | Send a message while Claude works, and explain when Claude will read it. | cc-esc-interrupt | 2 |
| cc-transcript-viewer | Transcript viewer (Ctrl+O) | Ctrl+O opens a detailed view that shows every action Claude took. | Open the detailed view with Ctrl+O, and find one action Claude took and its result. | cc-tools | 2 |
| cc-focus-view | /focus view | This view hides the details and shows only your last message, a short summary of actions, and Claude's final answer. | Turn the focus view on and off, and explain what it hides. | cc-slash-commands | 2 |
| cc-prompt-history | Prompt history and Ctrl+R | The up arrow and Ctrl+R let you find and reuse messages you typed before. | Bring back an earlier message with the up arrow, and search for one with Ctrl+R. | cc-sessions | 2 |
| cc-theme-color | /theme and /color | These commands change the colors of Claude Code to suit your eyes. | Change the look with /theme, and say what /color changes. | cc-slash-commands | 2 |
| cc-ctrl-g-editor | Ctrl+G open in editor | Ctrl+G opens your message in a normal text editor so long messages are easier to write. | Write a long message in an editor with Ctrl+G, and send it after the editor closes. | cc-multiline, term-code-editors | 3 |
| cc-tui-fullscreen | /tui fullscreen mode | This command switches to a smoother full-screen display with mouse support. | Switch to full screen with /tui, scroll with the mouse, and switch back. | cc-cli, cc-slash-commands | 3 |
| cc-voice-dictation | /voice dictation | This command lets you speak your message instead of typing it. | Turn on /voice, speak a message, and check the text before you send it. | cc-slash-commands | 3 |

## Branch: Apps, devices & extras
Other places where Claude Code can run, and extra powers like using a browser, using apps, and sharing pages.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| cc-desktop-panes | Desktop app panes and previews | The desktop app can show a terminal, a file editor, a diff view, and a live preview of your app next to the chat. | Open the terminal, diff and preview panes in the desktop app, and say what each one shows. | cc-desktop-code-tab | 2 |
| cc-vscode-extension | VS Code extension | A plug-in for the VS Code editor lets you chat with Claude next to your code and see its changes side by side. | Install the extension, open Claude in VS Code, and look at one change side by side. | cc-surfaces, term-code-editors | 2 |
| cc-jetbrains | JetBrains IDE plug-in | Claude Code can also work inside JetBrains editors like PyCharm or IntelliJ. | Say how to add Claude Code to a JetBrains editor, and what it shows there. | cc-surfaces | 3 |
| cc-remote-control | Remote Control | Remote Control lets you keep using a session that runs on your computer from your phone or another browser. | Turn on Remote Control for a session, and explain that the work still runs on your own computer. | cc-sessions, cc-surfaces | 2 |
| cc-mobile-app | Claude mobile app | The Claude phone app lets you start, watch, and guide coding tasks when you are away from your computer. | Open a coding task in the phone app, check its progress, and send it a new message. | cc-surfaces | 2 |
| cc-push-notifications | Push notifications | Claude Code can send a message to your computer or phone when it finishes or needs you. | Turn on notifications, and say the two moments they tell you about. | cc-permission-prompts | 2 |
| cc-claude-in-chrome | Claude in Chrome | Claude Code can connect to your Chrome browser to test web pages, read errors, and fill in forms. | Connect Claude to Chrome, and ask it to open a page of your app and report the errors it sees. | cc-tools, term-localhost | 2 |
| cc-artifacts | Artifacts | Claude can turn its work into a web page on claude.ai that you can keep private or share with others. | Ask Claude to make an artifact, open it, and say who can see it before you share it. | cc-sessions | 2 |
| cc-computer-use | Computer use | Claude can open apps, click, type, and look at your screen to test programs that have no command line. | Explain when computer use is needed, and why you watch closely and keep private things off the screen. | cc-claude-in-chrome, cc-permission-prompts | 3 |

## Branch: Context & memory
What Claude can see in a session, how to keep it focused, and how to give it lasting instructions.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| cc-file-mentions | @ file mentions | Typing @ and a file name points Claude straight to that file. | Point Claude to a file with @, and explain why this is faster than describing where the file is. | cc-sessions, term-files-folders | 1 |
| cc-context-command | /context | This command shows a colored picture of how full Claude's memory is and what is using the space. | Run /context, say how full the context is, and name the biggest thing using space. | ai-context-window, cc-slash-commands | 1 |
| cc-compaction | Compaction (automatic) | When the conversation gets too long, Claude Code shortens old parts into a summary so the work can continue. | Explain what automatic compaction does, and that small details from earlier can be lost. | ai-context-window, cc-sessions | 1 |
| cc-compact | /compact | This command lets you make that summary yourself, and you can say what is important to keep. | Run /compact with a note on what to keep, like the current goal and open problems. | cc-compaction, cc-slash-commands | 1 |
| cc-when-to-clear | When to clear or compact | Starting fresh for a new task and summarizing long tasks keeps Claude focused and saves cost. | Decide for a given case whether to use /clear, use /compact, or keep going, and explain why. | cc-clear, cc-compact | 1 |
| cc-claude-md | CLAUDE.md | CLAUDE.md is a text file in your project with rules and facts that Claude reads at the start of every session. | Explain what CLAUDE.md is for and when Claude reads it, and add one useful rule to it. | cc-sessions, ai-statelessness, prog-markdown | 1 |
| cc-init | /init | This command looks at your project and writes a first CLAUDE.md file for you. | Run /init in a project, read the CLAUDE.md it wrote, and fix one thing in it. | cc-claude-md, cc-slash-commands | 1 |
| cc-auto-memory | Auto memory | Claude can save useful things it learns about you and your project so it remembers them next time. | Explain what auto memory saves, and how it differs from a CLAUDE.md that you write yourself. | cc-claude-md | 1 |
| cc-memory-command | /memory | This command lets you open your CLAUDE.md files, turn auto memory on or off, and see what was saved. | Open a CLAUDE.md file and the saved memory through /memory, and turn auto memory on or off. | cc-auto-memory, cc-slash-commands | 1 |
| cc-claude-md-locations | Where CLAUDE.md files live | You can have a personal CLAUDE.md for all projects, one for a project, and extra ones in sub-folders. | Name the three places for a CLAUDE.md file, and say what kind of rule belongs in each. | cc-claude-md, term-home-folder | 2 |
| cc-claude-md-writing | Writing good CLAUDE.md instructions | Short, clear, and specific instructions in CLAUDE.md work better than long ones. | Rewrite a long, vague rule into a short, specific one, and explain why very long files hurt. | cc-claude-md, ai-context-engineering | 2 |
| cc-claude-md-imports | Importing files with @ in CLAUDE.md | CLAUDE.md can point to other files with @ so their content is included too. | Add an @ link to another file in CLAUDE.md, and explain that the other file's text then loads too. | cc-claude-md, cc-file-mentions | 2 |
| cc-claude-folder | The .claude folder | The .claude folder holds your settings, skills, agents, hooks, and memory for a project or for your user. | Find the .claude folder in a project and in your home folder, and say what kinds of files live there. | term-hidden-files, term-home-folder | 2 |
| cc-rules | Rules in .claude/rules | You can split instructions into small rule files, and some can apply only to certain files. | Make a small rule file, and explain how a rule can apply only to certain files. | cc-claude-md, cc-claude-folder | 2 |
| cc-agents-md | AGENTS.md | AGENTS.md is a shared instruction file that other AI coding tools also read, and Claude Code can read it too. | Explain what AGENTS.md is for, and how it relates to CLAUDE.md. | cc-claude-md | 2 |
| cc-add-dir-cd | /add-dir and /cd | These commands give Claude access to another folder or move the session to a new folder. | Give Claude access to a second folder with /add-dir, and move the session to another folder with /cd. | cc-slash-commands, term-paths | 2 |
| cc-system-reminders | System prompt and system reminders | Claude Code gives Claude hidden starting instructions and small notes during the session that help it work correctly. | Explain that Claude Code adds hidden instructions at the start and small reminders during the work, and why. | ai-system-prompt, cc-sessions | 2 |
| cc-autocompact | /autocompact | This command sets how full the memory gets before Claude Code shortens the conversation by itself. | Set the level with /autocompact, and explain what a higher or lower level changes. | cc-compaction, cc-slash-commands | 3 |
| cc-transcripts-storage | Where transcripts are stored | Every conversation is saved on your computer so it can be resumed or searched later. | Say that each session is saved as a file on your computer, and why that makes resuming possible. | cc-resume-continue, cc-claude-folder | 3 |
| cc-large-codebases | Large codebases | Big projects work better with CLAUDE.md files in each part and tools that help Claude stay focused. | Explain two ways to help Claude in a big project, like a CLAUDE.md per part and small, narrow tasks. | cc-claude-md-locations, ai-context-engineering | 3 |

## Branch: Models & cost
Which Claude model to use, how hard it thinks, and how to keep your usage under control.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| cc-models | Claude models (Fable, Opus, Sonnet, Haiku) | Claude comes in different models, from the strongest and slowest to the fastest and cheapest. | Put the Claude model families in order from strongest to cheapest, and say when to pick each. | ai-llm, cc-sessions | 1 |
| cc-model-command | /model | This command lets you pick which Claude model does the work. | Change the model with /model, and check which model is in use. | cc-models, cc-slash-commands | 1 |
| cc-plan-limits | Plan usage limits | Your plan lets you use Claude a certain amount, and the limit resets after some hours. | Explain that your plan has a usage limit that resets, and what uses it up faster. | ai-tokens, cc-models | 1 |
| cc-usage-command | /usage | This command shows how much you have used, your plan limits, and what is using the most. | Run /usage, and read how much of your limit is used and when it resets. | cc-plan-limits, cc-slash-commands | 1 |
| cc-model-aliases | Model aliases | Short names like `sonnet`, `opus`, `haiku`, `fable` and `best` always point to the newest model of that kind. | Explain what a short name like opus points to, and why it changes when a new model comes out. | cc-model-command | 2 |
| cc-effort | Effort levels and /effort | Effort controls how hard Claude thinks, from low and fast to max and slow. | Change the effort with /effort, and say when low or high effort fits a task better. | cc-model-command, ai-reasoning | 2 |
| cc-fast-mode | Fast mode and /fast | Fast mode makes answers from Opus come faster, but it costs more. | Turn fast mode on and off, and explain the trade between speed and cost. | cc-model-command | 2 |
| cc-limit-reset-wait | Waiting for a limit to reset | When you reach a limit, Claude Code can wait and continue by itself when the limit resets. | Explain what happens when you hit a limit, and how Claude Code can go on after the reset. | cc-plan-limits | 2 |
| cc-rate-limit-options | /rate-limit-options and usage credits | These show ways to keep working when you hit a limit, such as buying extra credits. | Open /rate-limit-options, and name the choices for working on after you hit a limit. | cc-plan-limits, cc-slash-commands | 2 |
| cc-saving-usage | Saving cost and usage | Clearing old conversations, using smaller models, and lower effort make your usage last longer. | Name three ways to make your usage last longer, and choose the best one for a given task. | cc-when-to-clear, cc-effort, cc-usage-command | 2 |
| cc-opusplan | opusplan | This setting uses a strong model for planning and a cheaper model for doing the work. | Explain what opusplan does, and why splitting planning and doing between two models saves cost. | cc-model-aliases, cc-plan-mode | 3 |
| cc-ultracode | Ultracode | Ultracode is a setting that lets Claude run many helper agents in an organized way for big tasks. | Explain when Ultracode is worth it, and that running many helpers uses much more of your limit. | cc-effort, cc-subagents | 3 |
| cc-advisor | Advisor tool | The advisor lets Claude ask a stronger model for advice at difficult moments in a task. | Explain what the advisor does, and why asking a stronger model only sometimes saves cost. | cc-models, cc-tools | 3 |
| cc-1m-context | Extended 1M context | Some models can hold a much bigger conversation, about one million tokens, for very long work. | Explain when a bigger context helps, and why it costs more and can still lose focus. | cc-model-command, ai-context-rot | 3 |
| cc-fallback-model | Fallback model | You can choose a backup model that Claude Code uses if your main model is busy or not available. | Explain what a backup model is for, and when Claude Code switches to it. | cc-model-command | 3 |
| cc-insights | /insights | This command makes a report about how you use Claude Code and what you could do better. | Run /insights, read the report, and pick one tip to try. | cc-usage-command | 3 |

## Branch: Settings & output styles
How to change the way Claude Code behaves and talks, and where those choices are saved.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| cc-output-styles | Output styles | An output style changes how Claude talks to you, for example shorter answers or more teaching. | Explain what an output style changes, and that it does not change what Claude is able to do. | cc-sessions | 1 |
| cc-learning-styles | Learning and Explanatory styles | These built-in styles make Claude explain what it does and sometimes ask you to write parts of the code yourself. | Say how the Learning and Explanatory styles differ, and what each one does for a learner. | cc-output-styles | 1 |
| cc-output-style-command | /output-style | This command shows the output styles and lets you switch to another one. | List the styles with /output-style, and switch to another one. | cc-output-styles, cc-slash-commands | 2 |
| cc-settings-json | settings.json | settings.json is a file where you save how Claude Code should behave. | Find a settings.json file, read one setting in it, and change it without breaking the JSON. | prog-json, cc-claude-folder | 2 |
| cc-settings-scopes | Settings scopes | Settings can be for you on every project, for a whole team project, only for you in one project, or set by your company. | Name the settings files for your user, the shared project, and your local project, and what belongs in each. | cc-settings-json | 2 |
| cc-config-key-value | /config key=value | You can change a setting quickly by typing it after /config. | Change one setting by typing it after /config, and check that it worked. | cc-status-config, cc-settings-json | 2 |
| cc-update-config | /update-config | You can describe a settings change in normal words and Claude edits the settings file for you. | Ask for a settings change in plain words with /update-config, and check what Claude changed. | cc-settings-json | 2 |
| cc-status-line | Status line and /statusline | The status line is a bar at the bottom that can show things like memory use, cost, and your git branch. | Set up a status line with /statusline, and say what each part of it shows. | cc-settings-json | 2 |
| cc-settings-precedence | Settings precedence | When the same setting is in several files, Claude Code has fixed rules about which one wins. | Explain which settings file wins when two disagree, and use this to find why a setting seems ignored. | cc-settings-scopes | 3 |
| cc-claude-code-env-vars | Environment variables for Claude Code | Some special named values on your computer can change how Claude Code works. | Explain how an environment variable can change Claude Code, and set one for one session. | term-env-vars, cc-settings-json | 3 |
| cc-custom-output-style | Custom output style | You can write your own output style file to make Claude answer the way you like. | Write a small output style file, switch to it, and check that Claude answers in the new way. | cc-output-style-command, cc-claude-folder, prog-markdown | 3 |
| cc-keybindings | /keybindings | This command opens a file where you can change keyboard shortcuts. | Open /keybindings, and change one shortcut to a key you like better. | cc-settings-json | 3 |
| cc-import-tools | /import from other tools | This command brings your settings and instructions from other AI coding tools into Claude Code. | Explain what /import brings over, and check the result after using it. | cc-settings-json, cc-agents-md | 3 |
| cc-managed-settings | Managed settings | A company can set rules for Claude Code that every worker must follow and cannot change. | Explain what managed settings are, and why they win over your own settings. | cc-settings-precedence | 3 |

## Branch: Hooks
Small scripts that run by themselves when certain things happen in Claude Code.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| cc-hooks | What hooks are | A hook is a small action, like a script, that runs by itself every time a certain thing happens in Claude Code. | Explain what a hook is, how it differs from asking Claude, and give one useful example. | cc-settings-json, term-scripts | 2 |
| cc-hooks-menu | /hooks menu | This command shows which hooks are set up and where they come from. | Open /hooks, and say which hooks are active and which settings file each one comes from. | cc-hooks | 2 |
| cc-hook-setup-matchers | Hook setup and matchers | You write hooks in a settings file and use a matcher to say which tools or events they react to. | Write a hook entry with an event, a matcher and a command, and explain what the matcher picks. | cc-hooks, prog-json | 2 |
| cc-hook-session-start | SessionStart event | This event fires when a session starts or resumes, so you can load useful information at the beginning. | Say when SessionStart fires, and give one thing a hook could load at that moment. | cc-hook-setup-matchers | 2 |
| cc-hook-user-prompt-submit | UserPromptSubmit event | This event fires when you send a message, before Claude reads it, so you can check it or add notes. | Say when UserPromptSubmit fires, and how a hook can add a note to your message. | cc-hook-setup-matchers | 2 |
| cc-hook-pre-tool-use | PreToolUse event | This event fires just before Claude uses a tool, so you can allow it, block it, or change it. | Say when PreToolUse fires, and how a hook can block a tool use, like deleting a folder. | cc-hook-setup-matchers, cc-tools | 2 |
| cc-hook-post-tool-use | PostToolUse event | This event fires after a tool finishes, for example to format code after Claude edits a file. | Say when PostToolUse fires, and give one use, like making a file neat after an edit. | cc-hook-setup-matchers, cc-tools | 2 |
| cc-hook-stop | Stop event | This event fires when Claude finishes its answer, for example to play a sound or check the work. | Say when Stop fires, and give one use, like a sound or a final check. | cc-hook-setup-matchers | 2 |
| cc-hook-notification | Notification event | This event fires when Claude Code wants your attention, for example when it waits for permission. | Say when Notification fires, and how it differs from Stop. | cc-hook-stop, cc-permission-prompts | 2 |
| cc-hook-exit-codes-json | Hook exit codes and JSON output | A hook tells Claude Code what to do through a number it ends with or a short message, for example to block an action. | Explain what exit code 0 and exit code 2 mean for a hook, and how a JSON answer can block or add notes. | cc-hook-pre-tool-use, term-output-errors-exit-codes | 3 |
| cc-hook-types | Hook types | A hook can be a command, a web request, a question to a model, an agent, or a tool from an MCP server. | Name the hook types, and say when a command hook is enough and when a model or agent hook helps. | cc-hook-setup-matchers | 3 |
| cc-hook-async | Async hooks | An async hook runs in the background so Claude does not have to wait for it. | Explain when to make a hook async, and why it cannot block an action. | cc-hook-exit-codes-json | 3 |
| cc-hook-permission-events | PermissionRequest and PermissionDenied events | These events fire when a permission window appears or when an action is refused. | Say when each of the two events fires, and give one use for each. | cc-hook-setup-matchers, cc-permission-prompts | 3 |
| cc-hook-tool-failure-batch | PostToolUseFailure and PostToolBatch events | These events fire when a tool fails or when a group of tool actions has finished. | Say when each of the two events fires, and how they differ from PostToolUse. | cc-hook-post-tool-use | 3 |
| cc-hook-subagent-events | SubagentStart and SubagentStop events | These events fire when a helper agent starts or finishes its job. | Say when each event fires, and give one use, like keeping a record of what helpers did. | cc-hook-setup-matchers, cc-subagents | 3 |
| cc-hook-compact-events | PreCompact and PostCompact events | These events fire just before and just after the conversation is shortened into a summary. | Say when each event fires, and give one use, like saving notes before details are lost. | cc-hook-setup-matchers, cc-compaction | 3 |
| cc-hook-session-end-events | SessionEnd and StopFailure events | These events fire when a session closes or when a turn ends because of an error. | Say when each event fires, and give one use for each. | cc-hook-stop | 3 |
| cc-hook-instructions-loaded | InstructionsLoaded event | This event fires when a CLAUDE.md or rule file is loaded into the conversation. | Say when this event fires, and how it helps check which instruction files really loaded. | cc-hook-setup-matchers, cc-rules | 3 |
| cc-hook-file-cwd-events | FileChanged, CwdChanged and DirectoryAdded events | These events fire when a watched file changes, when the working folder changes, or when a folder is added. | Say when each of the three events fires, and give one use for one of them. | cc-hook-setup-matchers, term-working-directory | 3 |
| cc-hook-task-events | TaskCreated, TaskCompleted and TeammateIdle events | These events fire when a task is created or finished, or when a team helper has nothing to do. | Say when each of the three events fires, and which one belongs to agent teams. | cc-hook-setup-matchers, cc-agent-teams | 3 |
| cc-hook-other-events | Other hook events | Less common events cover settings changes, worktrees, model switches, setup, command expansion, messages on screen, and MCP questions. | Know that these rarer events exist, and find the right one in the docs when you need it. | cc-hook-setup-matchers, prog-reading-docs | 3 |

## Branch: Skills
Saved sets of instructions that teach Claude how to do one kind of job.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| cc-skills | What skills are | A skill is a saved set of instructions for one kind of job that Claude can load when it needs it. | Explain what a skill is, how it differs from CLAUDE.md, and why it loads only when needed. | cc-claude-md | 1 |
| cc-using-skills | Using a skill with / | You can start a skill by typing / and its name, or Claude can choose it by itself. | Start a skill by typing / and its name, and explain how Claude can also pick one by itself. | cc-skills, cc-slash-commands | 1 |
| cc-bundled-skills | Bundled skills | Claude Code comes with ready-made skills for common jobs like code review, debugging, and running your app. | Name three skills that come with Claude Code, and say what job each one does. | cc-using-skills | 2 |
| cc-skills-command | /skills | This command lists your skills and shows how much memory space each one uses. | Run /skills, find a skill, and say how much context space it uses. | cc-using-skills, ai-tokens | 2 |
| cc-run-verify | /run and /verify | These skills start your app and check with real use that a change works, not only that tests pass. | Use /run to start your app and /verify to check a change, and explain why passing tests is not enough. | cc-bundled-skills, cc-verification-loop | 2 |
| cc-debug-skill | /debug | This skill turns on detailed logs and helps find out why something is going wrong. | Use /debug when something goes wrong, and read what the logs show. | cc-bundled-skills | 2 |
| cc-fewer-permission-prompts | /fewer-permission-prompts | This skill looks at your past sessions and adds safe commands to the allowed list so Claude asks you less. | Run it, read which commands it wants to allow, and keep only the ones you agree are safe. | cc-bundled-skills, cc-permission-rules | 2 |
| cc-creating-skills | Creating a skill (SKILL.md) | You make a skill by writing a SKILL.md file in a folder inside .claude/skills. | Create a skill folder with a SKILL.md file, and start the skill with /. | cc-using-skills, cc-claude-folder, prog-markdown | 2 |
| cc-skill-frontmatter | Skill frontmatter | The top part of a skill file holds its name, a short description, and options. | Write a skill's top part with a name and a description that tells Claude when to use it. | cc-creating-skills, prog-yaml | 2 |
| cc-skill-supporting-files | Skill supporting files | A skill folder can also hold scripts, examples, and longer notes that Claude reads only when needed. | Add an extra notes file or script to a skill, and point to it from SKILL.md. | cc-creating-skills | 3 |
| cc-skill-invocation | Who can start a skill | You can choose if only you, only Claude, or both can start a skill. | Set a skill so that only you can start it, and explain when that is wise. | cc-skill-frontmatter | 3 |
| cc-skill-arguments | Skill arguments | You can pass extra words after a skill's name, and the skill can use them. | Write a skill that uses the words typed after its name, and run it with such words. | cc-creating-skills | 3 |
| cc-skill-dynamic-context | Dynamic context in skills | A skill can run a command when it starts and put the result into its instructions. | Add a command to a skill whose result appears in its instructions, like the current git status. | cc-creating-skills, term-running-programs | 3 |
| cc-reload-skills | /reload-skills | This command makes Claude Code notice skills you added or changed without restarting. | Change a skill, and use /reload-skills so the change works without restarting. | cc-creating-skills | 3 |
| cc-skill-doctor | /skill-doctor | This command shows which skills cost the most space and which ones you never use. | Run /skill-doctor, and decide from the report which skill to shorten or remove. | cc-skills-command | 3 |
| cc-skill-creator | Testing skills with skill-creator | The skill-creator skill helps you build a skill and test if it really works well. | Use skill-creator to test a skill, and explain why a skill should be tested on real tasks. | cc-creating-skills, ai-evals | 3 |
| cc-design-slides | /design and /slides | These skills make screen designs or slide presentations as shareable pages. | Ask for a design or slides with these skills, and open the page they make. | cc-bundled-skills, cc-artifacts | 3 |
| cc-claude-api-skill | /claude-api | This skill gives Claude up-to-date facts for building your own programs with the Claude API. | Use /claude-api when building a program that talks to Claude, and say why fresh facts matter. | cc-bundled-skills, ai-claude-api | 3 |

## Branch: Subagents & parallel work
Helper agents and background work that let Claude do several jobs at once.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| cc-subagents | Subagents | A subagent is a helper Claude that does a side job in its own memory and gives back only a short report. | Explain what a subagent is, why it keeps the main context clean, and that only its report comes back. | ai-agents, ai-context-window, cc-tools | 2 |
| cc-builtin-subagents | Built-in subagents (Explore, Plan, general-purpose) | Claude Code has ready helpers for searching code, making plans, and general jobs. | Name the three built-in helpers, and say which job each is for. | cc-subagents | 2 |
| cc-custom-subagents | Custom subagents | You can create your own helper with its own instructions, tools, and model in .claude/agents. | Create a helper file in .claude/agents with a name, a description, tools and instructions. | cc-builtin-subagents, cc-claude-folder, prog-yaml | 2 |
| cc-background-subagents | Background subagents and /tasks | Helpers can work in the background while you keep chatting, and /tasks shows what is running. | Start a helper in the background, keep chatting, and check its progress with /tasks. | cc-subagents | 2 |
| cc-background-shell | Background shell commands (Ctrl+B) | A long command, like a server, can keep running in the background while Claude does other work. | Send a long command like a server to the background with Ctrl+B, and explain why this helps. | cc-bash-powershell-tools, term-processes-ports | 2 |
| cc-forked-subagents | Forked subagents and /subtask | A forked helper starts with a copy of your whole conversation and works on a side task. | Explain how a forked helper differs from a normal one, and when the full copy of the chat helps. | cc-subagents | 3 |
| cc-nested-subagents | Subagents that start subagents | A helper can start its own helpers to split a big job further. | Explain how helpers can start their own helpers, and why this can use a lot of your limit. | cc-subagents, ai-multi-agent | 3 |
| cc-background-sessions | Background sessions, /background and /fork | You can send a whole session to the background, or copy it into a new background session, and keep working. | Send a session to the background, fork a copy of it, and explain how the two differ. | cc-sessions, cc-background-subagents | 3 |
| cc-agent-view | Agent view (claude agents) | Agent view is one screen that shows all your background sessions and which ones need you. | Open agent view, find which background session needs you, and go into it. | cc-background-sessions | 3 |
| cc-agent-teams | Agent teams | An agent team is a group of Claude sessions with a leader, a shared task list, and messages between them. | Explain the leader, the shared task list and the messages in a team, and when a team is worth it. | cc-subagents, ai-multi-agent | 3 |
| cc-cross-session-messaging | Cross-session messaging and /list-agents | Claude can send messages to your other Claude Code sessions so they can share results. | List your running sessions with /list-agents, and explain how one session can send results to another. | cc-background-sessions | 3 |
| cc-workflows | Dynamic workflows and /workflows | A workflow is a script that Claude writes to run and check many helpers for very big jobs. | Explain what a workflow does, and when a job is big enough to need one. | cc-subagents, ai-multi-agent | 3 |
| cc-batch | /batch | This skill splits one large change into many small parts that helpers do at the same time. | Explain how /batch splits a large change, and what kind of change fits it. | cc-subagents, cc-using-skills | 3 |
| cc-deep-research | /deep-research | This workflow searches the web from many sides, checks the sources, and writes a report with links. | Start /deep-research on a question, and check some of the report's links yourself. | cc-workflows, cc-websearch-webfetch-tools | 3 |
| cc-claude-ai-projects | Projects on claude.ai | A project is one long conversation where Claude runs many related tasks for you in the cloud over days or weeks. | Explain what a claude.ai project is good for, and how it differs from one session on your computer. | cc-sessions, cc-cloud-sessions | 3 |

## Branch: MCP & connectors
How to connect Claude Code to other apps and services so it gets new tools.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| cc-mcp-add-server | Adding an MCP server | You add a server with `claude mcp add` or a config file, and its tools then appear for Claude. | Add an MCP server with claude mcp add, and check that its tools show up. | ai-mcp, cc-cli | 2 |
| cc-mcp-command | /mcp | This command shows your connected servers and lets you reconnect, turn them on or off, or log in. | Open /mcp, see which servers are connected, and reconnect or turn one off. | cc-mcp-add-server | 2 |
| cc-connectors | Connectors | Connectors are services you link to your claude.ai account, and they also appear in Claude Code. | Link a connector on claude.ai, and find its tools inside Claude Code. | ai-mcp, cc-install-sign-in | 2 |
| cc-mcp-scopes | MCP scopes and .mcp.json | A server can be for you only, for one project, or shared with your team in a .mcp.json file. | Name the three scopes, and read a .mcp.json file to see which servers a project shares. | cc-mcp-add-server, prog-json | 3 |
| cc-mcp-oauth | MCP login (OAuth) | Some servers need you to log in to your account before Claude can use them. | Log in to a server from /mcp, and explain that you sign in on the service's own page. | cc-mcp-command | 3 |
| cc-mcp-tool-search | MCP tool search | When there are many tools, Claude loads only the ones it needs so memory is not wasted. | Explain why loading every tool wastes context, and how tool search loads only the needed ones. | cc-mcp-add-server, ai-context-window | 3 |
| cc-mcp-resources-prompts | MCP resources and prompts | Besides tools, a server can offer files and ready prompts that you can use with @ or /. | Use a server's file with @ or its prompt with /, and say how these differ from tools. | cc-mcp-add-server, cc-file-mentions | 3 |
| cc-channels | Channels | A channel lets outside messages, like build results or chat messages, arrive in your running session. | Explain what a channel brings into a session, and give one example of a useful outside message. | cc-mcp-add-server | 3 |

## Branch: Plugins & mods
Packages that add skills, agents, hooks, and servers to Claude Code in one install.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| cc-plugins | Plugins | A plugin is a package that adds skills, agents, hooks, or servers to Claude Code in one install. | Explain what a plugin can contain, and why one install is easier than adding each part. | cc-skills | 2 |
| cc-plugin-install | /plugin install and manage | This command lets you find, install, turn on or off, and remove plugins. | Install a plugin with /plugin, turn it off, and remove it. | cc-plugins, cc-slash-commands | 2 |
| cc-plugin-marketplaces | Plugin marketplaces | A marketplace is a list of plugins that you add once and then install from. | Add a marketplace, and install a plugin from it. | cc-plugin-install | 2 |
| cc-anthropic-marketplaces | Anthropic's marketplaces | Anthropic runs official and community marketplaces with plugins you can browse. | Browse the official marketplace, and explain how official and community plugins differ in trust. | cc-plugin-marketplaces | 2 |
| cc-plugin-trust | Plugin trust and security | A plugin can run code on your computer, so install only plugins from sources you trust. | Explain why a plugin can be risky, and check who made a plugin before you install it. | cc-plugins | 2 |
| cc-lsp-plugins | Code intelligence (LSP) plugins | These plugins help Claude see code errors right after editing and jump to where things are defined. | Explain what a code intelligence plugin adds, and install one for your language. | cc-plugin-install, prog-linters-formatters | 3 |
| cc-creating-plugins | Creating a plugin | You can turn your own skills, hooks, and agents into a plugin to reuse or share. | Put one of your skills into a new plugin folder, and install the plugin from there. | cc-plugin-install, cc-creating-skills | 3 |
| cc-plugin-manifest | Plugin manifest (plugin.json) | plugin.json is the file that gives a plugin its name, version, and list of parts. | Write a plugin.json with a name, a version and a description. | cc-creating-plugins, prog-json, prog-semver | 3 |
| cc-reload-plugins | /reload-plugins | This command applies plugin changes without restarting Claude Code. | Change a plugin, and apply it with /reload-plugins without restarting. | cc-creating-plugins | 3 |
| cc-plugin-evals | Plugin evals | `claude plugin eval` tests whether a plugin really helps Claude do better. | Explain what a plugin eval measures, and run one on a plugin. | cc-creating-plugins, ai-evals | 3 |
| cc-mods | Mods | A mod is a special plugin written in JavaScript that can add panels, buttons, and commands inside Claude Code. | Explain how a mod differs from a normal plugin, and name one thing a mod can add to the screen. | cc-creating-plugins, prog-js-basics | 3 |

## Branch: Everyday coding workflow
A safe, step-by-step way to build with Claude, and how to go back when something goes wrong.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| cc-explore-plan-code-commit | Explore, plan, code, commit | A good way to work is to let Claude look around first, make a plan, write the code, and then save it with git. | Name the four steps in order, say what happens in each, and why the order matters. | cc-plan-mode, git-commit | 1 |
| cc-verification-loop | Verification loop | Giving Claude a way to check its own work, like tests or a screenshot, lets it keep fixing until it is right. | Give Claude a clear way to check its work for a task, and explain why this gives a better result. | cc-good-request, ai-verifying-output | 1 |
| cc-common-workflows | Common workflows | Claude Code has proven ways to fix bugs, add tests, clean up code, and understand a new project. | Pick the fitting way of working for a task, like a bug fix or learning a new project, and ask Claude for it. | cc-explore-plan-code-commit | 1 |
| cc-reviewing-changes | Reviewing Claude's changes | Before you keep a change, you read what Claude changed and ask about anything you do not understand. | Read a change Claude made, explain in your own words what it does, and ask about any unclear line. | cc-read-write-edit-tools | 1 |
| cc-checkpoints | Checkpoints | Claude Code saves a restore point before each change so you can go back if something goes wrong. | Explain what a checkpoint saves, and when Claude Code makes one. | cc-read-write-edit-tools | 1 |
| cc-rewind | /rewind and Esc Esc | This command, or pressing Esc twice, takes the code or the conversation back to an earlier point. | Use /rewind or Esc twice to go back, and choose to restore the code, the chat, or both. | cc-checkpoints | 1 |
| cc-git-through-claude | Git through Claude | You can ask Claude in plain words to save, explain, or undo changes with git for you. | Ask Claude in plain words to commit, explain or undo a change, and check which git command it ran. | git-commit, cc-bash-powershell-tools | 1 |
| cc-diff-command | /diff | This command shows all the changes in your files, including what Claude changed. | Open /diff, and read which files and lines changed. | cc-reviewing-changes, git-diff | 1 |
| cc-checkpoint-limits | Checkpoint limits | Changes made by terminal commands or outside Claude are not saved by checkpoints, so git is still needed. | Say which changes checkpoints cannot undo, and why you still commit with git. | cc-rewind, cc-bash-powershell-tools, git-commit | 2 |
| cc-worktree-flag | claude --worktree | This option starts Claude in a new worktree with one command. | Start a session in a new worktree with claude --worktree, and say where its files live. | git-worktree, cc-cli | 2 |
| cc-worktreeinclude | .worktreeinclude | This file lists files like secret settings that should be copied into each new worktree. | Explain why ignored files like .env are missing in a new worktree, and list them in .worktreeinclude. | cc-worktree-flag, git-gitignore | 3 |
| cc-monitor-tool | Monitor tool | The Monitor tool lets Claude watch a log or command output and react when something new appears. | Explain what the Monitor tool watches, and give one use, like reacting to a new error in a server log. | cc-background-shell | 3 |

## Branch: Reviews & pull requests
How Claude helps you check code and move work through pull requests on GitHub.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| cc-creating-prs | Creating pull requests with Claude | Claude can push your work to GitHub and open a pull request with a good description. | Ask Claude to push a branch and open a pull request, then read and improve its description. | gh-pull-requests, gh-cli, cc-git-through-claude | 2 |
| cc-pr-status | PR status in the prompt bar | Claude Code shows if your branch has a pull request and whether it passed checks and reviews. | Read the pull request status in Claude Code, and say if checks passed and reviews are done. | cc-creating-prs, gh-ci-checks | 2 |
| cc-code-review | /code-review | This skill reads your changes and looks for bugs, with an effort level you choose. | Run /code-review on your changes, pick an effort level, and decide which findings to fix. | cc-using-skills, cc-reviewing-changes | 2 |
| cc-simplify | /simplify | This skill looks at your changed code and makes it cleaner and simpler. | Run /simplify on your changes, and check that the cleaner code still works the same. | cc-using-skills, cc-reviewing-changes | 2 |
| cc-ultrareview | Ultrareview | Ultrareview is a very deep code review that many agents do in the cloud before you merge. | Explain how Ultrareview differs from /code-review, and when it is worth the extra cost. | cc-code-review, cc-cloud-sessions | 3 |
| cc-automated-code-review | Automated Code Review on GitHub | Claude can review every pull request on GitHub automatically and leave comments. | Explain how automatic reviews on pull requests work, and how you decide what to do with their comments. | gh-reviewing-prs, gh-github-apps | 3 |
| cc-autofix-pr | /autofix-pr | This command starts a cloud session that fixes your pull request when tests fail or reviewers comment. | Explain what /autofix-pr reacts to, and check the fixes it pushed. | cc-pr-status, cc-cloud-sessions | 3 |
| cc-from-pr | Resuming from a PR (--from-pr) | You can find and reopen the session that made a certain pull request. | Reopen the session behind a pull request with claude --from-pr. | cc-creating-prs, cc-resume-continue | 3 |

## Branch: Automation & cloud sessions
Ways to let Claude keep working by itself, on a schedule, or on Anthropic's computers.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| cc-goal | /goal | You set a finish condition and Claude keeps working by itself until it is met. | Set a /goal with a clear finish condition that can be checked, and explain why a vague one fails. | cc-verification-loop | 2 |
| cc-loop | /loop | This skill repeats a request again and again at a time interval while the session is open. | Start a /loop with a time interval, stop it, and explain that it ends when the session closes. | cc-using-skills | 2 |
| cc-desktop-scheduled-tasks | Desktop scheduled tasks | The desktop app can run Claude by itself every day or week for jobs like morning checks. | Create a scheduled task in the desktop app, and find the result of its last run. | cc-desktop-code-tab | 2 |
| cc-cloud-sessions | Cloud sessions (Claude Code on the web) | You can run Claude Code on Anthropic's computers from a browser, so it works even when your computer is off. | Start a cloud session in the browser, and explain how it differs from a session on your computer. | cc-surfaces, gh-create-repo | 2 |
| cc-github-cloud-setup | Connecting GitHub for cloud sessions | Cloud sessions need access to your GitHub repository, which you set up once with /web-setup or the website. | Connect GitHub for cloud sessions, and choose which repositories Claude may reach. | cc-cloud-sessions, gh-github-apps | 2 |
| cc-in-session-scheduled-tasks | In-session scheduled tasks | Claude can set reminders or repeating jobs inside a session, which stop when the session closes. | Ask Claude for a reminder in the session, and explain why it is gone after the session closes. | cc-loop | 3 |
| cc-cloud-environments | Cloud environments | A cloud environment decides what a cloud session can reach on the internet and what it installs first. | Explain what a cloud environment controls, like internet access and setup commands. | cc-cloud-sessions | 3 |
| cc-cloud-teleport | --cloud and /teleport | These move work between your computer and the cloud in both directions. | Send a task to the cloud with --cloud, and bring a cloud session back to your computer with /teleport. | cc-cloud-sessions | 3 |
| cc-routines | Routines and /schedule | A routine is a cloud job that runs Claude on a schedule or when something happens on GitHub. | Set up a routine with /schedule, and say what can start it: a time or a GitHub event. | cc-cloud-sessions, cc-desktop-scheduled-tasks | 3 |

## Branch: Scripts, SDK & GitHub Actions
Using Claude Code inside scripts, inside your own programs, and inside GitHub's automation.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| cc-print-mode | Print mode (claude -p) | This runs Claude with one request and prints the answer, so it can be used inside scripts. | Run claude -p with a request, and use its answer in a simple script. | cc-cli, term-scripts | 2 |
| cc-output-formats | Output formats (json, stream-json) | Print mode can give answers as data that other programs can read easily. | Get a JSON answer from claude -p, and pick out one field from it. | cc-print-mode, prog-json | 3 |
| cc-script-limits | Limits for scripts (--max-turns, --max-budget-usd) | These options stop a script run after a number of steps or a money limit. | Add a step limit and a money limit to a claude -p run, and explain why scripts need them. | cc-print-mode, term-flags | 3 |
| cc-bare-mode | Bare mode (--bare) | Bare mode starts Claude without your personal settings so a script gives the same result on every computer. | Explain why personal settings can change a script's result, and when to use --bare. | cc-print-mode, cc-settings-scopes | 3 |
| cc-setup-token | claude setup-token | This creates a long-lasting login key so scripts and automation can use your Claude account. | Explain what this login key is for, and why you keep it secret like a password. | cc-print-mode, cc-keeping-secrets | 3 |
| cc-agent-sdk | Agent SDK | The Agent SDK lets you build your own AI agent programs in Python or TypeScript using the same engine as Claude Code. | Explain what the Agent SDK is for, and how a program built with it differs from using Claude Code yourself. | ai-agents, ai-claude-api, prog-packages | 3 |
| cc-sdk-custom-tools | SDK custom tools | In the SDK you can give Claude your own functions to call as tools. | Explain how your own function becomes a tool Claude can use, and what Claude must be told about it. | cc-agent-sdk, prog-functions, ai-tool-use | 3 |
| cc-github-actions-claude | GitHub Actions with Claude | Claude can run inside GitHub's automation to answer @claude comments and turn issues into pull requests. | Explain how an @claude comment starts Claude in GitHub Actions, and what it can produce. | gh-actions, gh-issues, gh-pull-requests | 3 |
| cc-install-github-app | /install-github-app | This command connects the Claude GitHub app to a repository and helps set up GitHub Actions. | Run /install-github-app for a repository, and check the workflow file and the secret it adds. | cc-github-actions-claude, gh-repository-secrets, gh-github-apps | 3 |
| cc-deep-links | Deep links | A special link can open Claude Code in the right project with a ready request. | Explain what a deep link opens, and why you read the ready request before you send it. | cc-sessions | 3 |

## Branch: Safety
How to keep your computer, your code, and your secrets safe while Claude works.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| cc-safe-habits | Safe habits with Claude Code | Read what Claude wants to do before you allow it, and keep your work saved in git. | Name two safe habits, and explain how each one protects you from a bad change. | cc-permission-prompts, git-commit | 1 |
| cc-keeping-secrets | Keeping secrets safe | Passwords and keys should stay in private files that are never shared or uploaded. | Say where a secret key should live, keep it out of git and chats, and say what to do if one leaks. | prog-api-keys-env | 1 |
| cc-permission-rules | Permission rules (allow, ask, deny) | You can write rules that always allow, always ask, or always block certain actions. | Explain allow, ask and deny rules, and which one wins when two rules match. | cc-permission-modes, cc-settings-json | 2 |
| cc-permissions-command | /permissions | This command opens a window to see and change your permission rules. | Open /permissions, find a rule, and add or remove one. | cc-permission-rules | 2 |
| cc-permission-rule-syntax | Permission rule syntax | A rule names a tool and what it may touch, for example allowing only one test command. | Write a rule that allows only one exact command, and one that blocks reading a secret file. | cc-permission-rules | 2 |
| cc-auto-mode-checker | Auto mode safety checker | In auto mode a separate checker looks at each action and blocks risky ones, and you can tell it what you trust. | Explain what the checker looks at and what it blocks, and how to tell it what you trust. | cc-auto-mode, cc-permission-rules | 2 |
| cc-sandbox | Sandbox and /sandbox | The sandbox limits which files and websites Claude's commands can reach. | Turn on the sandbox with /sandbox, and explain what it stops a command from reaching. | cc-bash-powershell-tools, cc-permission-rules | 2 |
| cc-security-review | /security-review | This command checks your changes for security problems before you share them. | Run /security-review before sharing code, and decide which findings to fix. | cc-reviewing-changes, cc-keeping-secrets | 2 |
| cc-privacy-settings | Data use and /privacy-settings | You can see and choose how Anthropic may use your conversations. | Open /privacy-settings, and say what you allowed about how your conversations are used. | cc-slash-commands | 2 |
| cc-dontask-mode | dontAsk mode | This mode only runs actions you already allowed and refuses everything else, which suits automation. | Explain what dontAsk mode does with actions you did not allow, and why it suits scripts. | cc-permission-rules | 3 |
| cc-protected-paths | Protected and critical paths | Important folders and files get extra protection, and deleting them is never approved automatically. | Name kinds of files that get extra protection, and explain why deleting them always needs you. | cc-permission-rules | 3 |
| cc-sandbox-environments | Sandbox environments (containers, VMs) | For stronger safety you can run Claude inside a container or virtual machine that is separate from your real computer. | Explain what a container or virtual machine is, and why it keeps your real computer safe. | cc-sandbox | 3 |
| cc-bypass-permissions-mode | bypassPermissions mode | This mode skips almost all safety questions and should only be used in a closed test computer. | Explain what this mode skips, and why it is only safe inside a closed test computer. | cc-permission-modes, cc-sandbox-environments | 3 |
| cc-security-plugins | Security plugins | The security-guidance and Claude Security plugins help find and fix weak spots in your code. | Install a security plugin, and explain how it differs from running /security-review once. | cc-security-review, cc-plugin-install | 3 |

## Branch: Troubleshooting
How to find and fix problems when Claude Code does not work as expected.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| cc-install-login-problems | Install and login problems | Errors like "command not found" usually mean the program is not on your PATH or you are not logged in. | Fix a "command not found" error for claude and a login problem, and say the cause of each. | cc-install-sign-in, term-command-not-found | 1 |
| cc-doctor | /doctor | This skill checks your setup, finds problems, and can fix them. | Run /doctor, read what it found, and fix or ask about one problem. | cc-slash-commands | 2 |
| cc-why-settings-ignored | Finding why settings do not work | /context, /hooks, /mcp and /memory show what really loaded when something seems ignored. | Use /context, /hooks, /mcp or /memory to check if a setting, hook, server or rule really loaded. | cc-context-command, cc-hooks-menu, cc-mcp-command | 2 |
| cc-error-messages | Error messages | The error reference explains what each Claude Code error means and how to fix it. | Look up a Claude Code error in the error reference, and follow its fix. | prog-reading-errors, prog-reading-docs | 2 |
| cc-debug-logs | Debug logs (--debug) | Debug mode writes detailed notes about what Claude Code does so you can find a problem. | Start Claude Code with --debug, and find the line about a problem in the logs. | cc-cli, cc-error-messages | 3 |
