# Terminal and files

One subject of the skill tree: everything a beginner can learn about the terminal and files, split into branches (topics) in learning order. Each row is one concept: its ID, its name, one plain sentence, what the learner must say or do to prove they know it, the concepts it needs first ("-" means none), and its level (1 first week, 2 soon, 3 advanced). This file is the same for every user; what one user has learned is in `.claude/learning/progress/overview.md`. How the tutor uses it: `.claude/rules/teaching-while-building.md`.

## Branch: Terminal basics
What a terminal is, how to open one, and how to type commands into it.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| term-what-is-terminal | What a terminal is | A terminal is a window where you control your computer by typing commands instead of clicking. | Explain what a terminal is, and how typing a command differs from clicking in a window. | - | 1 |
| term-opening-terminal | Opening a terminal | You can open a terminal from your system's app menu, from a folder, or inside a code editor. | Open a terminal in two different ways, and open one that starts inside a chosen project folder. | term-what-is-terminal | 1 |
| term-shell | Shell | The shell is the program inside the terminal that understands your commands. | Explain the difference between the terminal window and the shell, and say which shell you are using. | term-what-is-terminal | 1 |
| term-powershell-vs-bash | PowerShell vs bash | PowerShell is the usual shell on Windows and bash is common on Mac and Linux, and they use different command words. | Say which shell each system uses by default, and give one command that is written differently in each. | term-shell | 1 |
| term-stopping-program | Stopping a program (Ctrl+C) | Ctrl+C stops a program that is running in the terminal. | Stop a running program with Ctrl+C, and tell when the terminal is ready for a new command. | term-opening-terminal | 1 |
| term-copy-paste | Copying and pasting in the terminal | Copy and paste work a bit differently in a terminal, and Ctrl+C may stop a program instead of copying. | Copy text out of the terminal and paste text into it, and explain why Ctrl+C may not copy there. | term-stopping-program | 1 |
| term-tab-completion-history | Tab completion and history | Pressing Tab finishes names for you, and the up arrow brings back old commands. | Use Tab to finish a file name, and the up arrow to run an earlier command again. | term-opening-terminal | 1 |
| term-windows-terminals | Windows Terminal, Git Bash and WSL | These are ways on Windows to open terminals, including ones that work like Linux. | Say what each of the three is, and when you would choose a Linux-like shell on Windows. | term-powershell-vs-bash | 2 |

## Branch: Files, folders & paths
How files are organized on a computer, and how to point to them by their address.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| term-files-folders | Files, folders and extensions | Files live in folders, and the end of a file name, like .py or .md, shows what kind of file it is. | Explain files and folders, and say what kind of file a .py, .js, .md and .json file is. | - | 1 |
| term-working-directory | Current folder (working directory) | The terminal is always "inside" one folder, and commands work on that folder. | Explain what the current folder is, and why the same command can act differently in another folder. | term-files-folders, term-opening-terminal | 1 |
| term-cd-ls-pwd | cd, ls and pwd | These commands change folder, list what is in a folder, and show where you are. | Use pwd to see where you are, ls to list files, and cd to go into a folder and back up with "cd ..". | term-working-directory | 1 |
| term-paths | Absolute and relative paths | A path is the address of a file, either from the top of the disk or from where you are now. | Write the same file's path as absolute and as relative, and explain what . and .. mean. | term-cd-ls-pwd | 1 |
| term-home-folder | Home folder and ~ | Your home folder is your personal folder, and ~ is a short way to write it. | Say where your home folder is, and use ~ in a path or a cd command. | term-paths | 1 |
| term-windows-unix-paths | Windows paths vs Unix paths | Windows uses C:\ and backslashes, while other systems use forward slashes. | Read a Windows path and a Unix path, and write the same path both ways. | term-paths | 1 |
| term-file-commands | Making, copying, moving and deleting files | Commands like mkdir, cp, mv and rm create, copy, move and delete files and folders. | Make a folder, copy, rename and delete a file by command, and explain why rm cannot be undone. | term-cd-ls-pwd, term-paths | 1 |
| term-hidden-files | Hidden files and dot folders | Files whose names start with a dot, like .git or .claude, are hidden by default. | Explain why dot files are hidden, and show them in a terminal or a file window. | term-cd-ls-pwd | 1 |
| term-text-encoding | Text encoding (UTF-8) | Text is saved as numbers using an encoding, and UTF-8 is the usual one that works for all languages. | Explain what an encoding is, why UTF-8 is the safe choice, and how a wrong one shows broken letters. | term-files-folders | 2 |

## Branch: Running programs
How to start programs from the terminal, give them options, and understand what they print.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| term-running-programs | Running a program and arguments | You run a program by typing its name, followed by extra words that tell it what to do. | Run a program with an argument, and point to the program name and its arguments in a command. | term-cd-ls-pwd | 1 |
| term-flags | Flags and options | Flags are extra settings that start with - or --, like --help. | Use --help to see a program's flags, and run a command with one flag. | term-running-programs | 1 |
| term-quotes-spaces | Quotes and spaces | Names with spaces must be put in quotes so the shell reads them as one thing. | Explain what goes wrong with a space in a path, and fix the command with quotes. | term-running-programs, term-paths | 1 |
| term-command-not-found | "Command not found" errors | This error means the program is not installed or its folder is not in PATH. | Read this error and check its two causes: the program is missing, or the shell cannot find it. | term-running-programs | 1 |
| term-code-editors | Code editors (VS Code) | A code editor is a program for reading and writing code files with helpful colors and tools. | Open a project folder in a code editor, change and save a file, and open the editor's built-in terminal. | term-files-folders | 1 |
| term-output-errors-exit-codes | Output, errors and exit codes | Programs print normal results and error messages separately, and end with a number that says success or failure. | Explain normal output and error output, and that exit code 0 means success and other numbers mean failure. | term-running-programs | 2 |
| term-pipes-redirection | Pipes and redirection | You can send one command's output into another command or into a file. | Save a command's output to a file with >, and send output into another command with a pipe. | term-output-errors-exit-codes | 2 |
| term-package-managers | Package managers for your system | Tools like winget, Homebrew or apt let you install programs with one command. | Install or update a program with your system's package manager, and check that it worked. | term-running-programs, term-flags | 2 |
| term-scripts | Scripts (.ps1 and .sh) | A script is a file of commands that runs them all in order. | Write a small script with two commands, run it, and say which shell runs .ps1 files and which runs .sh files. | term-running-programs, term-powershell-vs-bash | 2 |
| term-execution-policy | PowerShell execution policy | Windows may block scripts from running until you allow them in a safe way. | Explain why Windows blocks a script, and allow scripts for your own user only, not the whole computer. | term-scripts | 2 |

## Branch: Your computer's setup
How your computer finds programs, keeps settings, and runs apps and servers.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| term-localhost | localhost | localhost is the name your computer uses for itself, so you can open apps you run on it in a browser. | Open an app running on your computer at an address like localhost:3000, and say who else can see it. | term-what-is-terminal | 1 |
| term-env-vars | Environment variables | An environment variable is a named value that programs on your computer can read. | Explain what an environment variable is, read one in your shell, and name one use, like a secret key. | term-running-programs | 2 |
| term-path | PATH | PATH is a list of folders where your computer looks for programs when you type their names. | Explain how the shell uses PATH to find a program, show your PATH, and use it to fix a "not found" error. | term-env-vars, term-command-not-found | 2 |
| term-windows-env-vars | Setting environment variables on Windows | You can set a value for one terminal session or save it for good in Windows settings. | Set a value for this session only and one that stays, and explain why a new terminal is needed after. | term-env-vars | 2 |
| term-processes-ports | Processes and ports | A running program is a process, and a server listens on a numbered port like 3000. | Explain process and port, find what is using a port, and stop a process that is blocking it. | term-stopping-program, term-localhost | 2 |
| term-admin-rights | Administrator rights | Some actions need admin rights, so be careful when a command asks for them. | Explain what admin rights allow, why to be careful, and notice when a command asks for them. | term-running-programs | 2 |
