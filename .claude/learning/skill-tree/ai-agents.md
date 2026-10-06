# AI and agents

One subject of the skill tree: everything a beginner can learn about AI and agents, split into branches (topics) in learning order. Each row is one concept: its ID, its name, one plain sentence, what the learner must say or do to prove they know it, the concepts it needs first ("-" means none), and its level (1 first week, 2 soon, 3 advanced). This file is the same for every user; what one user has learned is in `.claude/learning/progress/overview.md`. How the tutor uses it: `.claude/rules/teaching-while-building.md`.

## Branch: How AI works
How AI models learn, how they read and write text, and where their limits are.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| ai-machine-learning | What AI and machine learning are | Machine learning is when a computer learns patterns from many examples instead of being given every rule. | Explain how learning from examples differs from a program with written rules, and give one example. | - | 1 |
| ai-llm | Large language model (LLM) | An LLM is an AI trained on huge amounts of text so it can read and write language. | Say what an LLM is, what it learned from, and name one LLM, like Claude. | ai-machine-learning | 1 |
| ai-how-llm-writes | How an LLM writes | An LLM writes by guessing the most likely next piece of text again and again. | Explain that the model builds its answer one small piece at a time by guessing what comes next. | ai-llm | 1 |
| ai-tokens | Tokens | Tokens are the small pieces of words that an AI reads and writes, and they are used to measure size and cost. | Say what a token is, that both what the AI reads and what it writes count, and that tokens set size limits and cost. | ai-how-llm-writes | 1 |
| ai-context-window | Context window | The context window is everything an AI can see and remember at one time in a conversation, and it has a size limit. | Explain that the window holds the whole chat and every file read, that it has a token limit, and what must happen when it is full. | ai-tokens | 1 |
| ai-statelessness | No memory between chats | An AI does not remember earlier conversations unless the facts are saved somewhere and given to it again. | Explain why a new chat starts with no memory, and how saved notes or files bring facts back. | ai-context-window | 1 |
| ai-knowledge-cutoff | Knowledge cutoff | An AI only knows facts up to the date its training stopped, unless it can search. | Say what a cutoff date is, why new facts may be missing, and how searching the web helps. | ai-llm | 1 |
| ai-hallucinations | Hallucinations | A hallucination is when an AI says something false with confidence. | Explain what a hallucination is, why it happens, and one way to catch it. | ai-how-llm-writes | 1 |
| ai-nondeterminism | Answers can change | The same question can get a different answer each time, because the AI picks its words with some chance. | Explain why asking twice can give two different answers, and why that matters when you check results. | ai-how-llm-writes | 1 |
| ai-model-families | Model families and sizes | Bigger models are smarter but slower and more expensive, and smaller ones are fast and cheap. | Compare big and small models on quality, speed and cost, and say when to pick each. | ai-llm | 2 |
| ai-reasoning | Reasoning and thinking | Some models can think step by step before they answer, which helps with hard problems. | Explain what thinking before answering does, when it helps, and that it uses more time and tokens. | ai-how-llm-writes, ai-tokens | 2 |
| ai-multimodal | Multimodal AI | Multimodal AI can understand images and other inputs, not only text. | Say what multimodal means and give one example, like showing the AI a screenshot of an error. | ai-llm | 2 |

## Branch: Prompts & context
How to give an AI clear instructions and the right information.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| ai-prompts | Prompts | A prompt is the message or instructions you give to an AI. | Say what a prompt is, and that everything the AI sees in the chat shapes its answer. | ai-llm | 1 |
| ai-prompt-writing | Prompt writing skills | Clear goals, examples, and context in your prompt lead to better answers. | Rewrite a vague prompt into a clear one that has a goal, the needed facts, and an example or a check. | ai-prompts | 1 |
| ai-verifying-output | Checking AI work | AI answers can be wrong, so you check important results by testing them, reading them, or asking for sources. | Name two ways to check an AI answer, and explain why you check before you trust it. | ai-hallucinations, ai-prompts | 1 |
| ai-system-prompt | System prompt | A system prompt is hidden starting instructions that shape how the AI behaves. | Explain what a system prompt is, who writes it, and how it differs from your own messages. | ai-prompts | 2 |
| ai-context-engineering | Context engineering | Context engineering means giving the AI the right information at the right time, not too much and not too little. | Explain why both too little and too much information hurt, and give one way to choose what to include. | ai-prompt-writing, ai-context-window | 2 |
| ai-context-rot | Long chats get worse | When a conversation gets very long and full, the AI starts to miss or mix up details. | Explain why answers get worse as the context fills up, and what to do about it, like starting fresh. | ai-context-window | 2 |
| ai-prompt-caching | Prompt caching | Prompt caching reuses text the AI already read, so repeated requests are faster and cheaper. | Explain that unchanged early text can be reused to save time and money, and what stops the reuse. | ai-tokens, ai-system-prompt | 3 |

## Branch: Agents & tools
How an AI uses tools and works in steps to finish a goal by itself.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| ai-tool-use | Tool use | Tool use means the AI can ask to run actions, like searching or running code, and see the results. | Explain how the AI asks for a tool, who really runs it, and how the result comes back to the AI. | ai-prompts | 1 |
| ai-agents | AI agents | An agent is an AI that plans, uses tools, and repeats steps on its own to finish a goal. | Explain how an agent differs from a simple chat answer, and name its parts: a goal, tools, and steps. | ai-tool-use | 1 |
| ai-agent-loop | The agent loop | An agent works in a cycle of think, act, look at the result, and decide the next step, and one round from your message to its final answer is called a turn. | Describe the think, act, check cycle, say when it stops, and say what one turn is. | ai-agents | 1 |
| ai-human-in-the-loop | Human in the loop | A person checks and approves important steps so the agent does not make costly mistakes. | Explain why a person approves risky steps, and give one example of a step that needs approval. | ai-agent-loop | 1 |
| ai-prompt-injection | Prompt injection | Prompt injection is when a web page, file, or other text contains hidden instructions that try to trick the AI. | Explain how hidden text can trick an AI that reads it, give one example, and say how to protect against it. | ai-tool-use, ai-prompts | 2 |
| ai-mcp | Model Context Protocol (MCP) | MCP is an open standard that lets any AI app connect to tools and data in the same way. | Explain what MCP is for, what an MCP server gives the AI, and why one shared standard helps. | ai-tool-use | 2 |
| ai-multi-agent | Multi-agent systems | Several agents can split a big job and work together. | Explain how splitting a job between agents can help, and one new problem it brings, like sharing results. | ai-agents | 3 |

## Branch: Building with AI
How your own programs can use an AI model, and how to measure the results.

| ID | Concept | What it is | Knowing it means | Needs | Level |
|---|---|---|---|---|---|
| ai-claude-api | Claude API | The Claude API lets your own programs send messages to Claude and get answers. | Explain what the API is for, what a program sends and gets back, and that it needs a secret key. | prog-apis, ai-llm | 2 |
| ai-api-pricing | API pricing and rate limits | AI services charge per token and limit how many requests you can send in a short time. | Explain how paying per token works for input and output, and what a rate limit error means. | ai-claude-api, ai-tokens | 2 |
| ai-structured-output | Structured output | Asking an AI for data in a fixed shape, like JSON, makes its answers easy for programs to use. | Explain why a program needs a fixed answer shape, and give one example JSON shape you would ask for. | prog-json, ai-prompt-writing | 2 |
| ai-embeddings | Embeddings | An embedding turns text into a list of numbers so a computer can find texts with similar meaning. | Explain that similar meanings get similar numbers, and give one use, like finding related notes. | ai-llm | 3 |
| ai-vector-databases | Vector databases | A vector database stores embeddings so similar texts can be found quickly. | Explain what a vector database stores and how it finds texts that are close in meaning to a question. | ai-embeddings, prog-databases-sql | 3 |
| ai-rag | RAG (retrieval-augmented generation) | RAG means finding the right documents first and giving them to the AI so it answers with real facts. | Describe the two steps, find and then answer, and explain why RAG reduces made-up answers. | ai-vector-databases, ai-context-engineering | 3 |
| ai-evals | Evals | Evals are tests that measure how well an AI or agent does a job. | Explain what an eval checks, why one try is not enough, and how evals compare two versions. | ai-nondeterminism, prog-testing | 3 |
| ai-fine-tuning | Fine-tuning | Fine-tuning is extra training that makes a model better at one special kind of task. | Explain what fine-tuning changes, and when good prompts or RAG are a cheaper choice. | ai-machine-learning, ai-model-families | 3 |
