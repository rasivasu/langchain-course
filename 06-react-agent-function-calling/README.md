# ReAct Agent with Tool Calling (LangGraph)

Implementation of a ReAct (Reason + Act) agent using LangGraph's state management and function calling.

## Overview

This project demonstrates:
- Building a stateful agent loop with `LangGraph`.
- Using `ToolNode` to handle external tool execution.
- Binding tools to a Chat Model (OpenAI).
- Integrating `TavilySearch` for real-time web access.
- Implementing custom tools (e.g., a simple `triple` math tool).

## Architecture

The application follows the **ReAct** (Reason + Act) framework, where the model interleaves reasoning traces and task-specific actions. This allows for more robust and transparent problem-solving.

For more details, see the original research paper in the `docs/` folder: [ReAct: Synergizing Reasoning and Acting in Language Models](docs/react_paper.pdf).

## Components

- **`react.py`**: Defines the LLM and the tools.
- **`nodes.py`**: Contains the graph nodes (Reasoning and Tool execution).
- **`main.py`**: Orchestrates the graph and executes the agent.

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

## Key Concepts
- **Reasoning Node**: The LLM decides whether to call a tool or provide a final answer.
- **Tool Node**: Executes the requested tools and feeds the results back into the graph.
- **Conditional Edges**: Determines the flow of execution based on the LLM's output.
