# Programming

One subject of the skill tree: everything a beginner can learn about programming, split into branches (topics) in learning order. Each row is one concept: its ID, its name, one plain sentence, what the learner must say or do to prove they know it, the concepts it needs first ("-" means none), and its level (1 first week, 2 soon, 3 advanced). This file is the same for every user; what one user has learned is in `.claude/learning/progress/overview.md`. How the tutor uses it: `.claude/rules/teaching-while-building.md`.

## Branch: Code basics
The building blocks that almost every programming language shares.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| prog-what-is-program | What a program is | A program is a list of exact instructions that a computer follows. | Explain that a computer follows steps exactly and in order, and why unclear steps give wrong results. | - | 1 |
| prog-languages | Programming languages | Languages like Python and JavaScript are different ways to write instructions for a computer. | Name two languages, say what each is often used for, and that the same idea can be written in both. | prog-what-is-program | 1 |
| prog-comments | Comments | A comment is a note in the code for people, which the computer skips. | Find a comment in a file, say who it is for, and write one in Python or JavaScript. | prog-languages | 1 |
| prog-variables | Variables | A variable is a named box that holds a value you can use and change. | Make a variable, change its value, and explain which part is the name and which is the value. | prog-languages | 1 |
| prog-data-types | Data types | Values have types, like text, numbers, true or false, and lists. | Name four basic types with an example of each, and explain why "5" and 5 are different. | prog-variables | 1 |
| prog-operators | Operators | Operators are symbols like +, == and "and" that do math, compare values, or join checks. | Use operators to add numbers, compare two values, and join two checks, and say the result. | prog-data-types | 1 |
| prog-print-output | Printing output | A program can show text on the screen, which is the easiest way to see what it is doing. | Print a value in Python or JavaScript, and use printing to look inside a running program. | prog-variables | 1 |
| prog-conditions | Conditions (if/else) | A condition lets a program do one thing or another depending on a check. | Read and write an if/else, and say which part runs for a given value. | prog-operators | 1 |
| prog-lists-dicts | Lists and dictionaries | Lists hold items in order, and dictionaries hold values you find by a name. | Make a list and a dictionary, get one item from each, and say when to use which. | prog-data-types | 1 |
| prog-loops | Loops | A loop repeats the same steps many times. | Read and write a loop over a list, and say how many times it runs and when it stops. | prog-conditions, prog-lists-dicts | 1 |
| prog-functions | Functions | A function is a named group of steps you can use again and again. | Write a function that takes inputs and gives back a result, call it, and explain why functions help. | prog-variables | 1 |
| prog-imports | Importing code | Importing lets one file use code from another file or from a package. | Read an import line, say where the code comes from, and import one thing in Python or JavaScript. | prog-functions | 2 |
| prog-objects-classes | Objects and classes | A class is a plan for making objects that keep data and actions together. | Explain class and object with an example, and point to the data and the actions in a small class. | prog-functions, prog-lists-dicts | 2 |
| prog-file-io | Reading and writing files in code | Programs can open files, read them, and save new content. | Read a text file and write a new one in code, and say what happens when the file is missing. | prog-functions, term-files-folders | 2 |
| prog-async | Async code | Async code lets a program wait for slow things, like the internet, without freezing. | Explain why a program must wait for slow work, what async avoids, and read a simple line that uses await. | prog-functions | 3 |
| prog-regex | Regular expressions | A regular expression is a pattern for finding text that matches a rule. | Read a simple pattern, say what text it matches, and name one common use, like finding email addresses. | prog-data-types | 3 |

## Branch: Fixing problems
How to find out why code does not work, and how to check that it does.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| prog-reading-errors | Reading error messages | Error messages and stack traces tell you what went wrong and in which line. | Find the error type, the message, and the file and line in an error, and say what it means. | prog-what-is-program | 1 |
| prog-debugging | Debugging | Debugging is finding and fixing the cause of a problem step by step. | Describe the steps: make the problem happen again, find where it starts, fix the cause, and check it is gone. | prog-reading-errors, prog-print-output | 1 |
| prog-reading-docs | Reading documentation | Docs are the official guides for a tool, and reading them is a key skill. | Find the official docs for a tool, look up one command or function, and use what you found. | prog-what-is-program | 1 |
| prog-testing | Testing | Tests are small programs that check your code works and keeps working. | Explain what a test checks, read one test, and run a project's tests and read which passed or failed. | prog-functions, prog-debugging | 2 |
| prog-linters-formatters | Linters and formatters | These tools find mistakes and make code look neat in the same style. | Say how a linter differs from a formatter, and run one of them on a file. | prog-packages | 2 |

## Branch: Data & text formats
Common ways to write down data, settings, and formatted text, and to store data.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| prog-markdown | Markdown | Markdown is a simple way to write formatted text with symbols like # for titles and * for lists. | Write a short Markdown note with a title, a list, bold text, a link, and a code block. | - | 1 |
| prog-json | JSON | JSON is a simple text format for storing and sending data with names and values. | Read and write a small JSON object with text, a number, a list, and a nested object, with correct quotes and commas. | prog-lists-dicts | 1 |
| prog-yaml | YAML | YAML is another text format for settings that uses spaces to show structure. | Read a small YAML file, say what each line sets, and explain why the spaces at the start of a line matter. | prog-json | 2 |
| prog-databases-sql | Databases and SQL | A database stores data in an organized way, and SQL is a language for asking it questions. | Explain tables, rows and columns, and read a simple SELECT query and say what it returns. | prog-lists-dicts | 2 |
| prog-sqlite | SQLite | SQLite is a small database that lives in a single file, good for beginners. | Explain why SQLite needs no server, where its data lives, and when it is a good choice. | prog-databases-sql | 2 |

## Branch: Tools & packages
How to install a language, run code, and use code that other people wrote.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| prog-python-basics | Python basics | Python is an easy-to-read language that is popular for scripts, data, and AI. | Read a short Python file and say what it does, noticing how spaces at the start of lines group the code. | prog-languages | 1 |
| prog-installing-python | Installing and running Python | You install Python and run a file with a command like `python app.py`. | Check that Python is installed, run a .py file from the terminal, and fix a "not found" error. | prog-python-basics, term-running-programs | 1 |
| prog-packages | Packages and dependencies | Packages are ready-made code from others that your project uses. | Explain what a package and a dependency are, why projects use them, and one risk of adding many. | prog-languages | 1 |
| prog-pip-venv | pip and virtual environments | pip installs Python packages, and a virtual environment keeps each project's packages separate. | Make and turn on a virtual environment, install a package with pip, and say why each project gets its own. | prog-installing-python, prog-packages | 2 |
| prog-js-basics | JavaScript basics | JavaScript is the language of web pages and also runs on computers with Node.js. | Read a short JavaScript file and say what it does, and name the two places JavaScript can run. | prog-languages | 1 |
| prog-node-npm | Node.js and npm | Node.js runs JavaScript outside the browser, and npm installs JavaScript packages. | Run a .js file with node, install a package with npm, and say what each of the two tools does. | prog-js-basics, prog-packages, term-running-programs | 1 |
| prog-package-json | package.json | This file lists a JavaScript project's name, packages, and handy commands. | Read a package.json, find its packages and scripts, and run one script with npm run. | prog-node-npm, prog-json | 2 |
| prog-semver | Semantic versioning | Version numbers like 2.1.3 show if a change is big, small, or only a fix. | Read a version like 2.1.3, say what each number means, and which kind of change may break your code. | prog-packages | 2 |
| prog-lock-files | Lock files | A lock file records the exact package versions so the project works the same everywhere. | Explain what a lock file stores, why it is saved in git, and why you do not edit it by hand. | prog-semver | 2 |
| prog-typescript | TypeScript | TypeScript is JavaScript with types that help catch mistakes before the code runs. | Explain what types add to JavaScript, and read a simple type in a line of TypeScript. | prog-js-basics, prog-data-types | 2 |
| prog-cli-programs | Command-line programs | Some programs have no windows and are used only by typing in the terminal. | Name one command-line program, run it with an option, and explain how it differs from an app with windows. | term-running-programs, term-flags | 2 |

## Branch: Web apps
How websites and web apps are built, how programs talk over the internet, and how apps go online.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| prog-html-css | HTML and CSS basics | HTML builds the parts of a web page and CSS makes it look nice. | Explain the job of HTML and the job of CSS, and change a heading's text and color in a simple page. | prog-languages | 1 |
| prog-frontend-backend | Frontend and backend | The frontend is what users see, and the backend is the hidden part that stores data and does the work. | Split a simple app into its frontend and backend parts, and say how the two talk to each other. | prog-html-css | 1 |
| prog-apis | APIs | An API is a way for one program to ask another program for data or actions. | Explain what an API is with an example, and what is sent in a request and what comes back. | prog-frontend-backend, prog-json | 1 |
| prog-api-keys-env | API keys and .env files | An API key is a secret password for a service, often kept in a private .env file. | Explain what an API key is, put one in a .env file, keep that file out of git, and read the key from code. | prog-apis, git-gitignore | 1 |
| prog-http | HTTP requests and status codes | Programs talk over the web with requests like GET and POST, and get answers with codes like 200 or 404. | Say what GET and POST do, and what the codes 200, 404 and 500 mean. | prog-apis | 2 |
| prog-web-frameworks | Web frameworks | Frameworks like React or Flask give you ready building blocks for making web apps. | Explain what a framework gives you, and name one for the frontend and one for the backend. | prog-frontend-backend, prog-packages | 2 |
| prog-deployment | Deployment and hosting | Deployment means putting your app on a server on the internet so others can use it. | Explain how running an app on localhost differs from hosting it online, and name one hosting service. | prog-frontend-backend, term-localhost | 2 |
