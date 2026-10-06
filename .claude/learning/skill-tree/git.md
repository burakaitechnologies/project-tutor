# Git

One subject of the skill tree: everything a beginner can learn about Git, split into branches (topics) in learning order. Each row is one concept: its ID, its name, one plain sentence, what the learner must say or do to prove they know it, the concepts it needs first ("-" means none), and its level (1 first week, 2 soon, 3 advanced). This file is the same for every user; what one user has learned is in `.claude/learning/progress/overview.md`. How the tutor uses it: `.claude/rules/teaching-while-building.md`.

## Branch: Saving your work
How Git keeps a history of your project by saving snapshots called commits.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| git-version-control | Version control | Version control keeps a history of every change to your files so you can go back at any time. | Explain what version control keeps, and two ways it helps, like going back and seeing what changed. | - | 1 |
| git-install-setup | Installing and setting up Git | You install Git once and tell it your name and email so your saved changes show who made them. | Check that Git is installed with git --version, and set your name and email with git config. | git-version-control, term-running-programs | 1 |
| git-repository | Repository | A repository is a project folder that Git watches and keeps a history for. | Explain what a repository is, and that its history lives in the hidden .git folder. | git-version-control, term-hidden-files | 1 |
| git-init | git init | This command turns a normal folder into a Git repository. | Run git init in a new folder, and explain what it created. | git-repository, git-install-setup | 1 |
| git-status | git status | This command shows which files changed and which are ready to be saved. | Run git status and read it: which files are new, which are changed, and which are staged. | git-repository | 1 |
| git-staging | Staging and git add | Staging means choosing which changes go into your next save. | Explain what staging is for, stage one file with git add, and see it as staged in git status. | git-status | 1 |
| git-commit | Commit | A commit is a saved snapshot of your project with a short message about what changed. | Make a commit with a message, and explain that it saves a snapshot of the staged changes. | git-staging | 1 |
| git-commit-messages | Good commit messages | A good message says clearly and briefly what changed and why. | Write a short, clear commit message for a change that says what changed and why. | git-commit | 1 |
| git-log | git log | This command shows the list of past commits. | Run git log, read a commit's ID, author, date and message, and use a short one-line view. | git-commit | 1 |
| git-diff | git diff | This command shows exactly which lines were added or removed. | Run git diff, read which lines were added and removed, and see staged changes with --staged. | git-staging | 1 |
| git-gitignore | .gitignore | This file lists files Git should never save, like secrets or big generated folders. | Add a file and a folder to .gitignore, and explain why secrets and big generated folders go there. | git-status | 1 |

## Branch: Working with remotes
How to connect your project to an online copy, and send and get changes.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| git-remotes | Remotes and origin | A remote is a copy of your repository on another computer, like GitHub, and origin is its usual name. | Explain what a remote and origin are, and list your remotes with git remote -v. | git-repository | 1 |
| git-authentication | Authentication (HTTPS and SSH keys) | Git needs to prove who you are before it can push to GitHub, using a login token or an SSH key. | Explain why Git must prove who you are, name the two ways, and set up one of them. | git-remotes, gh-account | 1 |
| git-clone | git clone | This command downloads a copy of an existing repository to your computer. | Clone a repository from a link, and explain that it brings the full history and sets origin. | git-remotes | 1 |
| git-push | git push | This command uploads your commits to the remote. | Push commits to the remote, and explain that only committed work is sent. | git-commit, git-remotes, git-authentication | 1 |
| git-fetch | git fetch | This command downloads new commits from the remote but does not change your files yet. | Run git fetch, and explain that it only downloads, so you can look before you add the changes. | git-remotes | 1 |
| git-pull | git pull | This command downloads new commits from the remote and adds them to your work. | Run git pull, and explain that it fetches and then merges the new commits into your branch. | git-fetch, git-commit | 1 |

## Branch: Branches & merging
How to work on separate lines of changes and bring them together again.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| git-branches | Branches | A branch is a separate line of work where you can try changes without breaking the main version. | Explain what a branch is for, and list branches with git branch to see which one you are on. | git-commit | 1 |
| git-main-branch | main branch | main is the usual name for the main, working version of a project. | Explain what main is for, and why new work usually happens on another branch. | git-branches | 1 |
| git-switch-checkout | git switch and git checkout | These commands move you to another branch or create a new one. | Create a branch and move between branches with git switch, and know the older git checkout does this too. | git-branches | 1 |
| git-head | HEAD | HEAD is a pointer that shows which commit you are looking at right now. | Explain that HEAD marks where you are now, and how it moves when you switch branch or commit. | git-switch-checkout | 2 |
| git-merge | git merge | This command brings the changes from one branch into another. | Merge one branch into another, and say which branch receives the changes. | git-switch-checkout | 2 |
| git-merge-conflicts | Merge conflicts | A conflict happens when two branches change the same lines and you must choose what to keep. | Read the conflict markers in a file, choose what to keep, and finish the merge with a commit. | git-merge, git-diff | 2 |
| git-detached-head | Detached HEAD | Detached HEAD means you are looking at an old commit and not on any branch. | Explain what detached HEAD means, why new commits there can get lost, and how to get back to a branch. | git-head | 3 |
| git-rebase | git rebase | Rebase moves your commits on top of newer work to keep history in a straight line. | Explain how rebase differs from merge, and why you should not rebase commits others already have. | git-merge | 3 |

## Branch: Undoing mistakes
How to go back, fix, or put aside changes without losing work.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| git-restore | Undoing changes with git restore | This command throws away changes in a file that you have not saved yet. | Throw away unsaved changes in one file with git restore, and explain that they cannot come back. | git-status | 2 |
| git-amend | git commit --amend | This changes your last commit, for example to fix its message. | Fix your last commit's message or add a forgotten file, and explain why not to do it after pushing. | git-commit, git-push | 2 |
| git-revert | git revert | This makes a new commit that undoes an older commit safely. | Undo an older commit with git revert, and explain why it is safe even after pushing. | git-log | 2 |
| git-reset | git reset | This moves your branch back to an earlier commit and can throw away work, so use it carefully. | Explain the difference between a soft and a hard reset, and when reset is dangerous. | git-head, git-log | 2 |
| git-stash | git stash | This puts your unsaved changes aside for a moment so you can do something else. | Put changes aside with git stash, switch branch, and bring them back with git stash pop. | git-switch-checkout, git-status | 2 |
| git-reflog | git reflog | This shows every place HEAD has been, which helps you find lost work. | Use git reflog to find a lost commit after a reset, and get it back. | git-reset | 3 |

## Branch: More Git tools
Extra Git features for versions, parallel work, files across systems, and looking into history.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| git-tags | Tags | A tag is a name you stick on an important commit, like a version number. | Add a tag like v1.0 to a commit, list tags, and push a tag to the remote. | git-commit, git-push | 2 |
| git-worktree | Worktrees (git worktree) | A worktree is a second folder of the same project on its own branch, so two jobs or AI sessions can work at once without touching the same files. | Explain what a worktree is, make one for a new branch, and say why two AI sessions should not share one folder. | git-branches, git-switch-checkout | 2 |
| git-line-endings | Line endings on Windows | Windows and other systems end lines differently, and Git can convert them to avoid fake changes. | Explain why line endings differ, how this shows up as fake changes, and that a Git setting or .gitattributes fixes it. | git-diff | 2 |
| git-blame | git blame | This shows who last changed each line of a file and when. | Run git blame on a file, and find who last changed a line and in which commit. | git-log | 3 |
| git-cherry-pick | git cherry-pick | This copies one chosen commit from another branch into your branch. | Copy one commit from another branch into yours with git cherry-pick, and say when this is useful. | git-branches, git-log | 3 |
