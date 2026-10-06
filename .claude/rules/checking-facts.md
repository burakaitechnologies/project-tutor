# Checking facts

**For:** every agent.

Never present something as a fact unless you are sure of it or have checked it. Your knowledge stops at a fixed date, and tools such as Claude Code change every week. A wrong fact told with confidence teaches the user something false.

## When to check

- Before you state a fact you are not sure of.
- Before you suggest a feature, tool or approach that matters for a decision. First choose what you think fits. Then search to confirm that it exists and works as you think, and to see whether a better option exists. Then give your final suggestion. Small, everyday suggestions do not need a search.
- When the user asks for the best way to do something.

## Where to check

- Claude Code: ask the `claude-code-guide` agent, or search the docs index `https://code.claude.com/docs/llms.txt` for a keyword and read only the matching page.
- A library or framework: the Context7 tool, which returns its current documentation, when it is installed (it is an MCP server: an add-on that gives Claude extra tools); otherwise a web search.
- Other tools, and how other people solved the same problem: a web search.

## How to show certainty

- Say what you checked, and give the source.
- Say what you did not check: "I think X, but I have not checked it." Check it if it matters.
- A subagent marks every unchecked statement in its answer, so the main agent knows what still needs checking.
