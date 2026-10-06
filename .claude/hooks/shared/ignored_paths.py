"""
ignored_paths.py - the one place that says which paths exist only on one computer

WHAT THIS FILE IS
A Python helper file (a "module"): it is not a hook and never runs on its own.
Two hook scripts load it with "import":
  .claude/hooks/reply-end/update-project-tree.py   shows such items once, with a note
  .claude/hooks/reply-end/check-broken-links.py    never counts a path to one as broken
Its name uses an underscore, not a dash, because Python can only import files
whose names have no dashes.

WHY IT EXISTS
.gitignore lists the files and folders that Git must never save. Some exist
only on one computer (such as .claude/settings.local.json), and some are made
later (such as the copies of raw records). In a fresh copy of the project they
are missing, and that is correct, so both scripts must know which paths these are.

HOW IT DECIDES
- When Git is installed and the project is a Git repository, it asks Git,
  which knows every rule of .gitignore exactly.
- Otherwise (for example a project downloaded as a ZIP file, without Git), it
  reads .gitignore itself, with the simple rules this project uses:
    a line ending with "/" names a folder; a line with another "/" in it is a
    path from the project folder; a line without "/" is a name anywhere; "*"
    stands for any letters. Lines starting with "#" (comments) or "!" (an
    exception, which these simple rules do not support) are skipped.
"""

import fnmatch     # compares names with patterns that use "*"
import os          # works with files and folders
import subprocess  # runs another program (here: git) and reads its answer

# Git writes names with letters such as "ö" as codes unless this is off.
GIT = ["git", "-c", "core.quotepath=off"]


def run_git(project, arguments, given=""):
    """Runs Git in the project folder and returns its output lines, or None
    when Git is missing or cannot answer (for example: not a repository).
    Exit code 1 means "nothing found", which is a normal answer.
    The text is sent and read as raw UTF-8 bytes: in text mode, Python on
    Windows would add an invisible "\\r" to every line it sends, and Git would
    then look for names that end with it."""
    try:
        result = subprocess.run(GIT + ["-C", project] + arguments, input=given.encode("utf-8"),
                                capture_output=True)
    except OSError:
        return None  # Git is not installed
    if result.returncode not in (0, 1):
        return None
    return result.stdout.decode("utf-8", errors="replace").splitlines()


def read_rules(project):
    """The lines of .gitignore as (pattern, folder only, from the project folder)."""
    try:
        with open(os.path.join(project, ".gitignore"), encoding="utf-8", errors="replace") as f:
            lines = f.read().splitlines()
    except OSError:
        return []
    rules = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith(("#", "!")):
            continue
        folder_only = line.endswith("/")
        line = line.rstrip("/")
        rules.append((line.lstrip("/"), folder_only, "/" in line))
    return rules


def matches(rules, path, is_folder):
    """True when one of the rules covers a path (from the project folder, with
    "/" between its parts), either the path itself or one of its folders."""
    parts = path.strip("/").split("/")
    for i, name in enumerate(parts):
        so_far = "/".join(parts[:i + 1])
        folder = i < len(parts) - 1 or is_folder
        for pattern, folder_only, anchored in rules:
            if folder_only and not folder:
                continue
            if fnmatch.fnmatchcase(so_far if anchored else name, pattern):
                return True
    return False


def ignored(project, paths):
    """Which of these paths .gitignore covers, whether they exist or not.
    Each path is written from the project folder, with "/" between its parts."""
    paths = [p for p in paths if p]
    if not paths:
        return set()
    answer = run_git(project, ["check-ignore", "--stdin"], "\n".join(paths) + "\n")
    if answer is not None:
        return set(answer)
    rules = read_rules(project)
    return {p for p in paths if matches(rules, p, p.endswith("/"))}


def checker(project):
    """For drawing a tree of items that exist: returns a test, used as
    test(path, is_folder), that says whether .gitignore covers that item.
    Git is asked once for the whole list: "--others --ignored" lists what Git
    does not save, "--exclude-standard" uses .gitignore, and "--directory"
    lists a fully ignored folder as one line ending with "/"."""
    listed = run_git(project, ["ls-files", "--others", "--ignored", "--exclude-standard", "--directory"])
    if listed is not None:
        found = set(listed)
        return lambda path, is_folder: path in found or path + "/" in found
    rules = read_rules(project)
    return lambda path, is_folder: matches(rules, path, is_folder)
