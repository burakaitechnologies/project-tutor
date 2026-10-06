"""
learning_state.py - the one place that calculates what the user has learned

WHAT THIS FILE IS
A Python helper file (a "module"): it is not a hook and never runs on its own.
Hook scripts load it with "import":
  .claude/hooks/user-prompt/remind-tutor-role.py           tells the tutor what to teach next
  .claude/hooks/after-file-change/update-learning-pages.py checks new proof and writes the progress pages
  .claude/hooks/reply-end/save-user-agent-chat.py          takes the user's name for the chat headings
Its name uses underscores, not dashes, because Python can only import files
whose names have no dashes.

THE IDEA: STATUS COMES ONLY FROM THE USER'S OWN WORDS
The tutor (the main agent) never writes "the user knows X". It only adds proof
entries to one file, .claude/learning/progress/proof-log.jsonl. Every entry
must quote the user's own words, and a quote counts only if it is found, word
for word, in the user's real messages (the chat files, or the raw record of the
current session). This module reads the file and CALCULATES each concept's
status. What the tutor explains is never recorded: only the user can prove.
The entry template, with every field explained: .claude/templates/proof-entry.md

THE THREE STATUSES, AND WHICH ENTRY RAISES A CONCEPT TO EACH
  not started  no proof yet
  in progress  "did": the user did it themselves
               "partial": the user explained part of it correctly
  learned      "explained" or "answered": the user explained it fully in their
               own words, or answered a check question correctly
  "missed" (a wrong answer, or the user showed they forgot) moves it one step
  down. Entries are applied in timestamp order, so the newest one decides.

THE TREE AND THE PERCENTAGES
.claude/learning/skill-tree/ holds one file per subject (for example Git).
Each subject has branches (topics), and each branch has concepts (the leaves,
each with an ID such as git-commit). Percentages are counted for every branch
and every subject: a concept in progress gives 1 point, a learned one 2 points,
out of 2 per concept. A concept can "need" other concepts first: a concept not
started is "ready" when every concept it needs has proof, and "locked" otherwise.

WHEN A CONCEPT IS DUE FOR REVIEW
Memory fades unless it is recalled, and each successful recall makes it last
longer ("spaced repetition"). So the wait before a review grows with the
status: see REVIEW_AFTER_DAYS below.
"""

import glob      # finds files by a name pattern
import json      # reads JSON text (the proof log, and the raw record)
import os        # works with files and folders
import re        # finds text patterns
from datetime import date

import local_time  # the user's clock, from .claude/hooks/shared/local_time.py

# ---- Settings ----------------------------------------------------------------
LEARNING = os.path.join(".claude", "learning")
TREE_DIR = os.path.join(LEARNING, "skill-tree")
PROFILE = os.path.join(LEARNING, "profile.md")
PROGRESS = os.path.join(LEARNING, "progress")
PROOF_LOG = os.path.join(PROGRESS, "proof-log.jsonl")
# The chat files: <day>/user-agent-chat.md inside this folder.
CHATS = os.path.join(".claude", "agent-memory", "main-agent")

# The order of the subjects; files not listed here come after, by name.
SUBJECT_ORDER = ["claude-code", "git", "github", "terminal", "programming", "ai-agents"]

STATUSES = ["not started", "in progress", "learned"]   # index = points 0, 1, 2
KIND_LEVEL = {"did": 1, "partial": 1, "explained": 2, "answered": 2}
KINDS = set(KIND_LEVEL) | {"missed"}
# Days to wait after the last proof before a concept is due for review.
REVIEW_AFTER_DAYS = {"in progress": 5, "learned": 21}

TIMESTAMP = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$")  # such as 2026-10-06 15:39


def today():
    return local_time.now().date()


def read(path):
    """The text of a file, or "" when it does not exist."""
    if not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read()


# ---- The tree ----------------------------------------------------------------
# A concept row starts with its ID, which begins with a letter. (The divider
# line under a table header, "|---|---|", must not count as a concept.)
ROW = re.compile(r"^\|\s*([a-z][a-z0-9-]*)\s*\|(.*)\|\s*$")


def load_tree(project):
    """Returns (subjects, concepts).
    subjects: a list of {"file", "name", "branches": [{"name", "about", "ids"}]}
    concepts: {id: {"id", "name", "what", "means", "needs", "level", "subject", "branch"}}"""
    files = glob.glob(os.path.join(project, TREE_DIR, "*.md"))
    def order(path):
        stem = os.path.splitext(os.path.basename(path))[0]
        return (SUBJECT_ORDER.index(stem) if stem in SUBJECT_ORDER else len(SUBJECT_ORDER), stem)
    subjects, concepts = [], {}
    for path in sorted(files, key=order):
        subject = {"file": os.path.basename(path), "name": os.path.basename(path)[:-3], "branches": []}
        branch = None
        for line in read(path).splitlines():
            if line.startswith("# "):
                subject["name"] = line[2:].strip()
            elif line.startswith("## Branch:"):
                branch = {"name": line[len("## Branch:"):].strip(), "about": "", "ids": []}
                subject["branches"].append(branch)
            elif branch is not None and line.strip() and not line.startswith("|") and not branch["about"]:
                branch["about"] = line.strip()
            elif branch is not None:
                row = ROW.match(line)
                if not row:
                    continue
                cells = [c.strip() for c in row.group(2).split("|")]
                if len(cells) < 5:
                    continue
                cid = row.group(1)
                needs = [n.strip() for n in cells[3].split(",") if n.strip() not in ("", "-")]
                concepts[cid] = {"id": cid, "name": cells[0], "what": cells[1], "means": cells[2],
                                 "needs": needs, "level": cells[4], "subject": subject["name"],
                                 "branch": branch["name"]}
                branch["ids"].append(cid)
        subjects.append(subject)
    return subjects, concepts


def check_tree(concepts):
    """Problems in the tree itself: needs that do not exist."""
    return [f"skill tree: {c['id']} needs unknown concept {need}"
            for c in concepts.values() for need in c["needs"] if need not in concepts]


# ---- The user's own words ----------------------------------------------------
def normal(text):
    """Small letters, straight quote marks and single spaces, so a quote still
    matches when only spacing, capital letters or the style of ' differs."""
    text = text.lower().replace("’", "'").replace("‘", "'")
    text = text.replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", text).strip()


def user_messages_in_chat(path):
    """The user's messages in a chat file, as one text. In a chat file, each
    user message starts with a hidden marker line "<!-- message ... -->", then
    a heading line; it ends at the next "## " heading or marker. Older chat
    files also have "<!-- reply -->" blocks, where the user answered a quoted
    part of an answer. Lines starting with ">" are quotes of the agent's words,
    not the user's, so they are left out."""
    out, inside = [], False
    lines = read(path).splitlines()
    for i, line in enumerate(lines):
        if line.startswith("<!-- message ") or line.startswith("<!-- reply"):
            inside = True
            continue
        if line.startswith(">"):
            continue
        if inside and line.startswith("## ") and i > 0 and lines[i - 1].startswith("<!-- message "):
            continue  # the heading right after the marker, such as "## 14:24 Sam"
        if line.startswith("## ") or line.startswith("<!-- "):
            inside = False
        if inside:
            out.append(line)
    return "\n".join(out)


def is_user_message(entry):
    """True when an entry of a raw record is a message the user typed. Claude
    Code marks those with the type "user" and the origin "human"; other "user"
    entries are tool results and system notes. This is the only place that
    knows this, so a change in Claude Code's format is fixed here once."""
    return entry.get("type") == "user" and (entry.get("origin") or {}).get("kind") == "human"


def user_messages_in_record(path):
    """The user's own messages in a raw record (one JSON object per line)."""
    out = []
    for line in read(path).splitlines():
        try:
            entry = json.loads(line)
        except ValueError:
            continue
        if not is_user_message(entry):
            continue
        content = entry.get("message", {}).get("content")
        if isinstance(content, list):
            content = "\n".join(p.get("text", "") for p in content if isinstance(p, dict))
        if isinstance(content, str):
            out.append(content)
    return "\n".join(out)


# ---- The proof log -----------------------------------------------------------
def load_proof(project):
    """All entries of the proof log, plus the problems found while reading.
    The file is JSONL: one JSON object per line. A broken line breaks only
    itself; it is reported and skipped."""
    entries, problems = [], []
    for number, line in enumerate(read(os.path.join(project, PROOF_LOG)).splitlines(), 1):
        if not line.strip():
            continue
        try:
            entry = json.loads(line)
        except ValueError:
            problems.append(f"proof log line {number}: not valid JSON")
            continue
        if not isinstance(entry, dict):
            problems.append(f"proof log line {number}: not a JSON object")
            continue
        entry = {k: str(entry.get(k) or "").strip()
                 for k in ("timestamp", "concept", "kind", "quote", "note", "source")}
        entry["line"] = number
        entries.append(entry)
    return entries, problems


def compute(project, transcript_path=None):
    """Reads the tree and the proof, and returns
    (subjects, concepts, state, problems).
    state: {id: {"status", "last" (a date or None), "entries": [entries]}}
    problems: entries that were not counted, and why."""
    subjects, concepts = load_tree(project)
    entries, problems = load_proof(project)
    problems = check_tree(concepts) + problems
    state = {cid: {"status": "not started", "last": None, "entries": []} for cid in concepts}
    texts = {}  # a cache: source -> the user's words in it, normalized

    def users_words(entry):
        day = entry["timestamp"][:10]
        source = entry["source"] or os.path.join(CHATS, day, "user-agent-chat.md")
        if source not in texts:
            path = source if os.path.isabs(source) else os.path.join(project, source)
            texts[source] = normal(user_messages_in_chat(path))
        words = texts[source]
        # Today's newest message may not be in the chat file yet: also look in
        # the raw record of the current session.
        if transcript_path and day == today().isoformat():
            if "__record__" not in texts:
                texts["__record__"] = normal(user_messages_in_record(transcript_path))
            words += " " + texts["__record__"]
        return words

    for entry in sorted(entries, key=lambda e: e["timestamp"]):
        where = f"proof log line {entry['line']}"
        cid, kind = entry["concept"], entry["kind"].lower()
        if not TIMESTAMP.match(entry["timestamp"]):
            problems.append(f"{where}: the timestamp must look like 2026-10-06 15:39")
            continue
        if cid not in concepts:
            problems.append(f"{where}: unknown concept '{cid}'")
            continue
        if kind not in KINDS:
            problems.append(f"{where}: unknown kind '{kind}'")
            continue
        if not entry["quote"]:
            problems.append(f"{where}: no quote; every entry needs the user's own words")
            continue
        if normal(entry["quote"]) not in users_words(entry):
            problems.append(f"{where}: quote not found in the user's messages: \"{entry['quote'][:60]}\"")
            continue
        current = STATUSES.index(state[cid]["status"])
        level = max(0, current - 1) if kind == "missed" else max(current, KIND_LEVEL[kind])
        state[cid]["status"] = STATUSES[level]
        state[cid]["last"] = date.fromisoformat(entry["timestamp"][:10])
        state[cid]["entries"].append(entry)
    return subjects, concepts, state, problems


# ---- Questions the tutor needs answered --------------------------------------
def is_ready(cid, concepts, state):
    """A concept not started whose needed concepts all have proof."""
    return state[cid]["status"] == "not started" and all(
        state.get(n, {"status": "not started"})["status"] != "not started" for n in concepts[cid]["needs"])


def counts(state, ids=None):
    result = {s: 0 for s in STATUSES}
    for cid in (ids if ids is not None else state):
        result[state[cid]["status"]] += 1
    return result


def percent(state, ids):
    """How much of a group is proved: 1 point per concept in progress, 2 per
    concept learned, out of 2 per concept."""
    if not ids:
        return 0
    points = sum(STATUSES.index(state[c]["status"]) for c in ids)
    return round(100 * points / (2 * len(ids)))


def due_for_review(concepts, state, limit):
    """Concepts due for review, oldest first, at most one per branch (mixing
    topics in reviews helps memory more than several questions on one topic)."""
    due = []
    for cid, s in state.items():
        wait = REVIEW_AFTER_DAYS.get(s["status"])
        if wait is not None and s["last"] and (today() - s["last"]).days >= wait:
            due.append((s["last"], cid))
    picked, branches = [], set()
    for _, cid in sorted(due):
        branch = concepts[cid]["branch"]
        if branch not in branches and len(picked) < limit:
            picked.append(cid)
            branches.add(branch)
    return picked


def ready_next(subjects, concepts, state, limit):
    """Ready concepts to suggest: the lowest level first, then the tree's own
    order; at most one per subject in each round, so subjects stay mixed."""
    per_subject = []
    for subject in subjects:
        ids = [cid for b in subject["branches"] for cid in b["ids"] if is_ready(cid, concepts, state)]
        ids.sort(key=lambda cid: concepts[cid]["level"])  # sort keeps the tree order inside a level
        per_subject.append(ids)
    picked = []
    while len(picked) < limit and any(per_subject):
        for ids in per_subject:
            if ids and len(picked) < limit:
                picked.append(ids.pop(0))
    return picked


def user_name(project):
    """The user's name from the profile ("- **Name:** ..."), or "".
    The placeholder "(not filled in yet)" counts as no name."""
    m = re.search(r"\*\*Name:\*\*\s*(.+)", read(os.path.join(project, PROFILE)))
    name = m.group(1).strip() if m else ""
    return "" if name.startswith("(") else name
