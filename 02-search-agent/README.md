# LangChain Search Agents Tutorial

This tutorial demonstrates how to build search agents using LangChain's `create_agent` interface. The project progresses through three key concepts, showing how to evolve from a basic custom tool implementation to using structured outputs with built-in LangChain integrations.

## 📚 Foundational Research

The development of tool-using agents is supported by research into how language models can autonomously decide when and how to use external APIs:

- **Toolformer:** [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) (Schick et al., 2023). This paper explores how LLMs can be trained to call external tools in a self-supervised manner, providing the theoretical basis for modern agentic tool-use. (See `docs/toolformer_paper.pdf`)

## Learning Objectives

- Understand the LangChain `create_agent` interface
- Build custom tools using the `@tool` decorator
- Integrate third-party search APIs (Tavily)
- Use LangChain's built-in tool integrations
- Implement structured outputs with Pydantic models

## Implementation Overview

| Step | Title | What You'll Learn | Key Changes |
|---|---|---|---|
| 1 | Intro to Search Agents | Project setup, creating custom search tools with `@tool` decorator, direct Tavily API integration. | Initial project setup, created custom `search` function using `@tool`, direct `TavilyClient` integration. |
| 2 | LangChain Tavily Built-in Tool | Using LangChain's built-in tool integrations instead of custom tools for simplification. | Replaced custom `@tool` with `TavilySearch` from `langchain_tavily`. |
| 3 | Structured Output | Implementing structured outputs with Pydantic models for type-safe agent responses. | Added `Source` and `AgentResponse` BaseModels, configured `response_format`. |

## Running the Code

1. Install dependencies:
   ```bash
   uv sync
   ```

2. Set up environment variables:
   ```bash
   # Create a .env file with:
   OPENAI_API_KEY=your_openai_key
   TAVILY_API_KEY=your_tavily_key
   ```

3. Run the agent:
   ```bash
   python main.py
   ```

## Example Query

The agent searches for AI engineer job postings in the Bay Area on LinkedIn:
```python
"search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details?"
```

## Key Takeaways

- **Custom Tools**: You can create custom tools using the `@tool` decorator for specialized functionality
- **Built-in Integrations**: LangChain provides pre-built tools that reduce boilerplate and improve maintainability
- **Structured Outputs**: Using Pydantic models with `response_format` ensures type-safe, predictable agent responses
- **Agent Interface**: The `create_agent` function provides a simple, consistent interface for building agents with different capabilities
