# MCP Search Agent

This project recreates the functionality of [**02-search-agent**](../02-search-agent) using the **Model Context Protocol (MCP)** architecture. 

It demonstrates how to decouple tool execution from the agent logic, allowing for greater interoperability and modularity.

## 🏗️ Architecture

The application is split into two primary components that communicate over `stdio` using the MCP standard:

1.  **MCP Server (`server.py`)**: A standalone process that provides the search capability. It uses the `FastMCP` library and "owns" the Tavily API integration.
2.  **MCP Host (`main.py`)**: A LangChain application that consumes the search tool over the protocol. It runs the LLM and orchestrates the agent loop.

## 🗺️ Architectural Mapping

This table shows how the components in this folder map to the original monolithic implementation in `02-search-agent`.

| Component | 02-search-agent (Monolith) | 50-mcp-search-agent (MCP) | MCP Role |
| :--- | :--- | :--- | :--- |
| **Tool Execution** | `TavilySearch()` call inside `main.py` | `search_web()` in **`server.py`** | **MCP Server** |
| **Agent Logic** | `create_agent` in `2-main.py` | **`main.py`** calling `server.py` | **MCP Host** |
| **Tool Protocol** | Direct Library Import | JSON-RPC 2.0 (via `stdio`) | **MCP Transport** |
| **LLM Orchestration** | `llm.invoke` in `2-main.py` | `llm.ainvoke` in **`main.py`** | **MCP Host** |

## 📚 Foundational Research

This project builds upon research into standardized tool-model communication:

- **Toolformer:** [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761) (Schick et al., 2023). This paper provides the theoretical basis for how LLMs can be trained to recognize the need for external tools—a concept that MCP formalizes into a universal standard. (See `docs/toolformer_paper.pdf`)

## 🚀 Setup & Execution

### Prerequisites
- Python 3.11+
- [uv](https://github.com/astral-sh/uv)
- `OPENAI_API_KEY` and `TAVILY_API_KEY` in your `.env` file.

### Installation
```bash
uv sync
```

### Running the Agent
Simply run the host script. It will automatically start the server process in the background.
```bash
python main.py
```

## 🛠️ Key Files
- **`server.py`**: The MCP Server. Can be used standalone by any MCP client (Claude Desktop, Cursor, etc.).
- **`main.py`**: The MCP Host. Connects to the server and runs the LangChain agent.
- **`pyproject.toml`**: Project dependencies including `fastmcp` and `mcp`.
