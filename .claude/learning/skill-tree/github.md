# GitHub

One subject of the skill tree: everything a beginner can learn about GitHub, split into branches (topics) in learning order. Each row is one concept: its ID, its name, one plain sentence, what the learner must say or do to prove they know it, the concepts it needs first ("-" means none), and its level (1 first week, 2 soon, 3 advanced). This file is the same for every user; what one user has learned is in `.claude/learning/progress/overview.md`. How the tutor uses it: `.claude/rules/teaching-while-building.md`.

## Branch: GitHub basics
What GitHub is, how to put a project on it, and how to use it from the terminal.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| gh-what-is-github | What GitHub is | GitHub is a website that stores Git repositories online so you can back them up and work with others. | Explain the difference between Git and GitHub, and give two reasons to put a project on GitHub. | - | 1 |
| gh-account | GitHub account and profile | Your account is your identity on GitHub and shows your projects to others. | Open your GitHub account, and say what other people can see on your profile. | gh-what-is-github | 1 |
| gh-create-repo | Creating a repository on GitHub | You make a new empty repository on GitHub and connect your local project to it. | Create an empty repository on GitHub, add it as a remote, and push your local project to it. | gh-account, git-remotes, git-push | 1 |
| gh-public-private | Public and private repositories | A public repository can be seen by everyone, and a private one only by people you choose. | Explain who can see a public and a private repository, and change a repository's visibility. | gh-create-repo | 1 |
| gh-browsing-repository | Browsing a repository on GitHub | On the GitHub website you can look at files, past commits, and branches without downloading anything. | Find a file, the commit history, and the list of branches of a repository on the GitHub website. | gh-what-is-github, git-commit | 1 |
| gh-markdown | Markdown on GitHub | GitHub shows Markdown files, issues, and comments as nicely formatted text. | Write a comment or .md file on GitHub that shows a title, a list, and a code block correctly. | prog-markdown, gh-what-is-github | 1 |
| gh-readme | README | The README file is the front page of a repository that explains what the project is and how to use it. | Say what a good README contains, and write a short one with a title, what the project does, and how to run it. | gh-markdown | 1 |
| gh-cli | GitHub CLI (gh) | gh is a terminal program that lets you, or Claude, do GitHub work without opening the website. | Explain what gh is for, and run one gh command, like listing your repositories or pull requests. | gh-what-is-github, term-running-programs | 1 |
| gh-auth-login | gh auth login | This command logs the GitHub CLI into your account. | Log gh into your account with gh auth login, and check it with gh auth status. | gh-cli, gh-account | 1 |

## Branch: Pull requests & issues
How people suggest, discuss, check, and accept changes on GitHub.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| gh-pull-requests | Pull requests | A pull request asks to add the changes from one branch into another, so they can be checked first. | Explain what a pull request is for, and open one from a pushed branch on the website or with gh. | git-branches, git-push, gh-create-repo | 1 |
| gh-merging-prs | Merging a pull request | Merging adds the pull request's changes to the main branch, sometimes squashed into one commit. | Merge a pull request, explain what a squash merge does, and update your local main afterwards. | gh-pull-requests, git-pull | 1 |
| gh-issues | Issues | An issue is a note on GitHub about a bug, an idea, or a task to do. | Open an issue with a clear title and description, and close it when the work is done. | gh-browsing-repository | 1 |
| gh-reviewing-prs | Reviewing a pull request | Reviewers read the changes, leave comments, and approve or ask for fixes. | Read a pull request's changes, comment on a line, and approve it or ask for changes. | gh-pull-requests | 2 |
| gh-forks | Forks | A fork is your own copy of someone else's repository that you can change freely. | Fork a repository, explain how a fork differs from a clone, and how changes go back by pull request. | gh-pull-requests, git-clone | 2 |
| gh-collaborators | Collaborators and permissions | You can invite people to your repository and choose what they are allowed to do. | Invite someone to a repository, and choose a fitting permission level, like read or write. | gh-create-repo | 2 |
| gh-labels-projects | Labels, milestones and Projects | These help you sort and plan issues and pull requests. | Add a label to an issue, put it in a milestone, and explain what a Project board shows. | gh-issues | 3 |

## Branch: Automation & security
How GitHub runs checks by itself and protects your code and your secrets.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| gh-actions | GitHub Actions | GitHub Actions run jobs automatically, like tests, every time something happens in a repository. | Explain what an Action does and what starts it, and find a run's result in the Actions tab. | gh-create-repo, prog-testing | 2 |
| gh-workflow-files | Workflow files (YAML) | A workflow file in .github/workflows describes when an action runs and what it does. | Read a workflow file, and point to when it runs, on which machine, and which steps it does. | gh-actions, prog-yaml | 2 |
| gh-ci-checks | CI checks on pull requests | Checks are automatic tests that show a green tick or red cross on a pull request. | Find a pull request's checks, open a failed one, and read its log to see what broke. | gh-actions, gh-pull-requests | 2 |
| gh-repository-secrets | Repository secrets | Secrets are hidden values like API keys that GitHub Actions can use without showing them. | Add a repository secret, and use it in a workflow file without writing its value in the code. | gh-workflow-files, prog-api-keys-env | 2 |
| gh-github-apps | GitHub Apps | GitHub Apps, like the Claude app, are tools that you allow to work on your repositories. | Explain what a GitHub App is, install one on a repository, and check or remove what it can reach. | gh-create-repo | 2 |
| gh-branch-protection | Branch protection | Branch protection stops people from changing the main branch without a review or passing checks. | Set a rule so main needs a pull request and passing checks before changes are merged. | gh-ci-checks, gh-reviewing-prs | 3 |
| gh-dependabot | Dependabot | Dependabot warns you about old or unsafe packages and can open pull requests to update them. | Explain what Dependabot watches, read one of its alerts, and decide whether to merge its update. | gh-pull-requests, prog-packages | 3 |

## Branch: Sharing & publishing
How to share your project, publish versions and websites, and follow other projects.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| gh-licenses | Licenses | A license file tells others what they may and may not do with your code. | Explain why a public project needs a license, and name one common license, like MIT. | gh-public-private | 2 |
| gh-template-repositories | Template repositories | A repository marked as a template lets anyone start a new project as a copy of it with one click. | Mark a repository as a template, start a new project from one, and explain how this differs from a fork. | gh-create-repo, gh-forks | 2 |
| gh-pages | GitHub Pages | GitHub Pages puts a simple website online for free straight from a repository. | Turn on GitHub Pages for a repository, and open the live website address. | gh-create-repo, prog-html-css | 2 |
| gh-releases | Releases | A release is a named version of your project that people can download. | Make a release from a tag, add notes on what changed, and find where people download it. | git-tags, gh-create-repo | 3 |
| gh-gists | Gists | A gist is a quick way to share a small piece of code or text. | Create a gist and share its link, and say when a gist fits better than a repository. | gh-account | 3 |
| gh-codespaces | Codespaces | Codespaces gives you a ready coding computer in the browser for a repository. | Open a codespace for a repository, run a command in it, and explain that it runs in the cloud. | gh-create-repo, term-code-editors | 3 |
| gh-notifications-stars | Notifications, stars and watching | These help you follow projects you like and see when something needs your attention. | Star and watch a repository, and find your notifications for reviews or mentions. | gh-account | 3 |
