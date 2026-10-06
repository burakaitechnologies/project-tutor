# Keeping memory

**For:** every agent. Most of it is about the main agent's memory.

## Why memory matters

- A new session starts with an empty conversation, and a compaction (Claude Code shrinking a long conversation into a summary) loses details. Notes carry decisions, findings and unfinished work across these breaks.
- The project will run for months. Notes keep its long history: what was built, what was rejected, and why.
- The reasons behind decisions are easy to forget and expensive to find again. Notes stop the next agent from trying rejected ideas again.
- The user reads the notes to review the work and learn from it.
- A subagent's work is saved, so its results stay available after it ends.

## Memory map

```
.claude/agent-memory/main-agent/
├── memory/MEMORY.md                  inbox for small lessons (Claude Code's auto memory)
├── raw-transcripts/YYYY-MM-DD/HHMM_<id>/   copies of Claude Code's raw session records, one folder per session (not in Git)
└── YYYY-MM-DD/                       one folder per day
    ├── process-log.md                settled events of the day
    ├── day-takeaways.md              what the day taught; written after the day ends
    ├── user-agent-chat.md            the user's messages and the main agent's answers
    ├── documents/                    things the main agent produced that day
    └── subagents/<agent-type>/<topic>.md   records of subagent jobs
```

A day folder is created when the first file of that day is saved. Dates use the user's clock, as `.claude/hooks/shared/local_time.py` decides it. Never store passwords, keys or private data in memory.

## Process log (written by the main agent)

- It contains only settled things: decisions the user agreed to, actions that were really done, verified facts, and approaches that were rejected. Ideas still under discussion are not logged; the chat file keeps them.
- Before every change, read the whole log of the day and rewrite it as one clean, consistent record. Keep every action that was done and every rejected approach with its reason. When a decision changed, keep both, with the "Changed from:" line of the template.
- Update the log when something becomes settled, not after every message. Never log routine actions such as "opened a file".
- Each entry follows `.claude/templates/process-entry.md`. Take the time from the time line that `.claude/hooks/user-prompt/add-current-time.py` adds to each message.

## Day takeaways (written by the main agent)

- Written once for a finished day, never for today, using `.claude/templates/day-takeaways.md`.
- `.claude/hooks/user-prompt/find-missing-takeaways.py` lists every earlier day whose takeaways are missing or older than its process log. Write those first, oldest first, from that day's process log and chat file.
- "What the user learned" lists the concepts that moved forward that day (that day's lines in `.claude/learning/progress/proof-log.jsonl`), and what they found hard.
- The file is mostly takeaways: what the day taught, decided, built and rejected, and why. "Open as of this day" lists every item still open on that day, including items opened on earlier days. An item leaves the list only on the day it is closed.

## The learning record (in `.claude/learning/`, not here)

What the user has learned is not kept in these day notes. It lives in `.claude/learning/`: the profile, the skill tree, the proof log (one JSONL file, written by the main agent) and the progress pages (written by a hook). The day notes only summarize it, in "What the user learned". How it works: `.claude/rules/teaching-while-building.md`.

## Chat file (written by a hook)

`.claude/hooks/reply-end/save-user-agent-chat.py` adds the user's messages and the main agent's answers to the day's `user-agent-chat.md`, with the session ID. Never edit it by hand.

## Subagent records (written by a hook)

`.claude/hooks/subagent-end/save-subagent-record.py` saves a record when a subagent finishes: its agent type, ID, the path of its raw transcript copy, its prompt and its answer. If a subagent stops without finishing, the main agent writes its record itself, in the same shape, with the line written exactly as `Status: stopped` (the session-start hook looks for exactly that line).

## Raw transcripts (copied by a hook)

Claude Code keeps a raw record (a transcript) of every session and subagent outside the project and deletes it after 30 days. `.claude/hooks/reply-end/backup-raw-transcripts.py` copies these records into `.claude/agent-memory/main-agent/raw-transcripts/`, so they are never lost. Every session gets one folder, inside a folder for the day it started (on the user's clock). The session folder is named after its start time and the first 8 characters of its ID: `.claude/agent-memory/main-agent/raw-transcripts/<day>/<time>_<id>/`, for example 2026-10-06/0931_1a2b3c4d. So sorting by name sorts by time, and a day folder exists only when a session started that day. Inside are the main conversation's record and a folder named "subagents"; a session that runs over several days stays in its one folder, under the day it started. The naming rule lives only in `.claude/hooks/shared/raw_transcript_copy.py`. To find the session of a conversation, look for its session ID in the chat file. They are large and contain everything that was read, so Git ignores them.

## MEMORY.md, the lessons inbox

Claude Code loads `.claude/agent-memory/main-agent/memory/MEMORY.md` into every session by itself, because `.claude/settings.local.json` points its auto memory there (see `.claude/settings.json.explained.md`); on each new computer, the `/onboard` skill makes that local file. Use it only for small lessons that are not yet part of a rule or a document, for example a technical trick about this computer. A lasting preference of the user about how they like to learn or work belongs in `.claude/learning/profile.md` instead. When a lesson becomes part of a rule or a document, delete it from `MEMORY.md`.

## At session start

At every session start, resume, `/clear` and compaction, `.claude/hooks/session-start/load-session-memory.py` prints a reading list: the newest day-takeaways files and the newest process logs (how many is set at the top of that script), plus unfinished subagent work and unsaved changes. It prints paths instead of the notes themselves, because Claude Code adds at most 10,000 characters of a hook's output to your context.

1. Read every file on the list, in the order given, before any other work. The order is oldest first, so you read the history as it happened.
2. Then tell the user in at most 5 lines: where things stand, what is waiting for them, what is unfinished, and what you propose next.
