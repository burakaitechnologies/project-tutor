# Using subagents

**For:** the main agent.

A subagent is a helper Claude session that you start for one job. It begins with an empty conversation and reads `CLAUDE.md` and the rules, but not your output style.

## When to use one

- Do small work, and work that needs a decision about the whole project, yourself.
- Give a subagent a focused job with a clear end, such as research or a review. Everything it reads stays out of your conversation, which keeps your conversation small.
- Prefer subagents over extra Claude sessions. Do not use agent teams: they are experimental and cost much more.
- A subagent can start its own subagents (Claude Code allows up to 3 levels). Allow this only when a job truly needs it, because nested helpers are hard to follow.

## Which subagent

- Use Claude Code's built-in subagents: `general-purpose` for most jobs, `claude-code-guide` for questions about Claude Code. Give each one a clear prompt.
- Do not create role files (fixed subagent definitions, which Claude Code reads from an "agents" folder inside `.claude/`). Each job here is different, so a clear prompt fits better than fixed instructions. If the same job keeps repeating with the same long prompt, suggest a role file to the user first.
- Every subagent's record goes into the day folder (see `.claude/rules/keeping-memory.md`).

## The prompt

Every prompt contains: the goal and why it matters, what to deliver and in what shape (you choose the shape for each job), when to stop, and "write only to the outputs I asked for".

## When a subagent stops early

- In the same session, never restart a failed or stopped job from zero. Resume it with `SendMessage` and its ID: it continues with its full history. Its ID is in its record.
- In a later session, reopen the old session to resume it, or start a new subagent from the saved prompt.
- The built-in `Explore` and `Plan` subagents cannot be resumed, so use `general-purpose` for long jobs.
