# 🤖 The Anatomy of an AI Agent: Core Components

Welcome to this educational repository dedicated to demystifying the architecture of modern AI Agents.
This guide uses a clear, component-based approach to explain how autonomous AI systems perceive, think, plan, and act.

The central reference for this project is the following diagram:

![AI Agent Architecture](https://github.com/user-attachments/assets/ffe1a763-dfbd-487c-96b0-6b82b4254cad)

## What is an AI Agent?

An **AI Agent** is an autonomous entity that can perceive its environment, make decisions, and take actions to achieve specific goals.
Think of it like a digital assistant that can do more than just answer questions—it can complete multi-step tasks, use tools, and learn from feedback.
The "brain" of these modern agents is often a **Large Language Model (LLM)**.

---


## The Core Components

Let's break down each component shown in the diagram.

### 📥 1. Perception / Input

This is the agent's sensory system. It's how the agent takes in information from the outside world, whether that's a direct command from a user, data from a sensor, or content from a website.

* **Analogy:** Your eyes and ears.
* **Function:** To gather raw data and convert it into a format the agent's brain (the LLM) can understand.

See the code: [`code_snippets/01_perception.py`](./code_snippets/01_perception.py)


### 🧠 2. Knowledge Base / Memory

Memory is crucial for context and learning. An agent needs to remember past interactions, learned facts, and its current objectives.
Memory can be:

* **Short-Term (Working Memory):** What the agent is thinking about *right now*.
* **Long-Term (Knowledge Base):** A vast library of information the agent can retrieve when needed.

* **Analogy:** Your own short-term memory versus everything you've learned in your life.
* **Function:** To store and retrieve information, providing context for decisions.

See the code: [`code_snippets/02_memory.py`](./code_snippets/02_memory.py)


### 🤔 3. Decision-Making / Reasoning Engine (LLM)

This is the central "brain" of the agent. It's typically a powerful Large Language Model (LLM) like GPT, Gemini, or Llama.
This engine takes the input from **Perception** and the context from **Memory** to think, reason, and decide what to do next.

* **Analogy:** Your conscious thought process.
* **Function:** To process information, evaluate options, and form intentions.

See the code: [`code_snippets/03_reasoning_engine.py`](./code_snippets/03_reasoning_engine.py)


### 📝 4. Planning / Task Orchestration

For complex goals, the agent can't just act. It needs a plan. The planning component breaks down a large task (e.g., "plan a trip to Paris") into a sequence of smaller,
manageable steps (e.g., 1. find flights, 2. book hotel, 3. find restaurants).

* **Analogy:** Writing a to-do list before starting a big project.
* **Function:** To create a step-by-step strategy to achieve a goal.

See the code: [`code_snippets/04_planning.py`](./code_snippets/04_planning.py)


### 🚀 5. Action / Output

This is how the agent interacts with its environment. Based on the decisions and plans from the reasoning engine, the action component executes a specific task.
This could be writing code, calling an API, sending an email, or simply responding to the user.

* **Analogy:** Your hands and voice.
* **Function:** To execute the chosen action and affect the environment.

See the code: [`code_snippets/05_action.py`](./code_snippets/05_action.py)

---


## The Interaction Loop

The components don't work in isolation. They form a continuous loop:

1.  The agent **perceives** a user request.
2.  It uses its **reasoning engine** and **memory** to understand the request.
3.  It creates a **plan** to address the request.
4.  It takes **action** by using a **tool** (like a search engine API).
5.  It receives **feedback** (the search results), updates its **memory**, and continues the loop until the goal is achieved.
    This feedback loop is how the agent **learns** and improves.

You can see a simulation of this entire process here: [`code_snippets/06_agent_loop.py`](./code_snippets/06_agent_loop.py)


## How to Contribute

Contributions are welcome! If you have ideas for improving the explanations or code snippets, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.



