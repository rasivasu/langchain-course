# Reflexion Agent (Advanced Actor-Critic)

An advanced implementation of the Reflexion pattern (Actor-Critic) that combines self-reflection with external tool use and search.

## Overview

The Reflexion agent is more sophisticated than a basic Reflection agent. It:
1. **Drafts**: Provides an initial detailed answer.
2. **Executes Tools**: Uses external tools (like search) to find supporting evidence.
3. **Revises**: Incorporates tool results and self-critique to produce a high-quality, cited response.

## Architecture

- **Actor**: The `ChatOpenAI` model performing the drafting and revision.
- **Critique**: Built-in reflection step within the actor's prompt.
- **Tool Executor**: A dedicated node to execute research tasks.
- **State Graph**: Managed by `LangGraph` with a defined `MAX_ITERATIONS` limit.

## Setup

1. Install dependencies:
   ```bash
   uv sync
   ```

2. Configure environment:
   Set `OPENAI_API_KEY` and `TAVILY_API_KEY` in your `.env` file.

3. Run the agent:
   ```bash
   python main.py
   ```

## Key Components
- **`schemas.py`**: Defines structured outputs for the Actor and Revisor.
- **`tool_executor.py`**: Handles the execution of tool calls.
- **`chains.py`**: Defines the specialized chains for initial response and revision.
- **`main.py`**: Defines the graph structure and runs the process.
