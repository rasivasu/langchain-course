# LangChain MCP Adapters

A comprehensive project demonstrating the integration of LangChain with Model Context Protocol (MCP) adapters and LangSmith tracing.

This project serves as a learning resource for understanding:
- How to connect to MCP servers from a Python application
- Converting MCP tools to LangChain BaseTool objects
- Building agents that can use external tools via MCP
- Automatic tracing of LLM operations with LangSmith

## Prerequisites

- Python 3.13 or higher
- `uv` package manager (or `pip`)

## Setup

### 1. Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

Or with `uv`:

```bash
uv venv
source .venv/bin/activate
```

### 2. Install Dependencies

```bash
uv sync
```

Or with pip:

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root:

```env
LANGCHAIN_PROJECT=mcp_test
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=your_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

**Security Note:** The `.env` file is excluded from version control (see `.gitignore`). Never commit this file to avoid exposing API keys.

## Running the Project

```bash
python main.py
```

This will:
- Load environment variables from `.env`
- Connect to the local MCP math server
- Display available tools
- Create an agent with those tools
- Invoke the agent with a test question
- All operations are traced to LangSmith

## Project Structure

```
.
├── .env                 # Environment variables (not in version control)
├── .gitignore          # Git ignore rules
├── .python-version     # Python version specification
├── README.md           # This file
├── pyproject.toml      # Project metadata and dependencies
├── uv.lock             # Lock file for reproducible builds
├── main.py             # Main application entry point
└── servers/            # MCP server implementations
    └── math_server.py  # Example MCP server with math tools
```

## Dependencies

- **langchain** (≥1.3.4): Core LangChain framework for building LLM applications
- **langchain-mcp-adapters** (≥0.2.2): Adapter utilities to convert MCP tools to LangChain BaseTool
- **langchain-openai** (≥1.2.2): OpenAI integration for LangChain LLMs
- **langgraph** (≥1.2.4): Graph-based workflow framework for complex agent orchestration
- **python-dotenv** (≥1.2.2): Load environment variables from `.env` files

## Architecture

### MCP (Model Context Protocol)

MCP is a lightweight protocol for standardized tool exposure:

```
Your Application (MCP Host)
    ↓
MCP Client (manages connection & protocol)
    ↓
stdio_client (transport layer)
    ↓
MCP Server (provides tools)
```

### LangChain Integration

```
ChatOpenAI LLM
    ↓
Agent (orchestrates tool use)
    ↓
LangChain Tools (adapted from MCP)
    ↓
MCP Server Tools
```

### Two-Layer Abstraction

MCP tool integration uses two adapter layers:

1. **MCP Client Layer** — Handles JSON-RPC protocol, capability negotiation, tool discovery
2. **Transport Layer (stdio_client)** — Manages process communication via stdin/stdout

This separation allows the same protocol logic to work over different transports (stdio, HTTP, etc.).

## LangSmith Integration

This project is configured to use [LangSmith](https://smith.langchain.com/) for tracing and monitoring LangChain applications.

### How It Works

When `LANGSMITH_TRACING=true`, all LangChain operations are automatically logged to LangSmith:
- **LLM calls** — Track input/output and token usage
- **Tool invocations** — Monitor MCP tool execution
- **Agent runs** — See the agent's decision-making process
- **Token counting** — Estimate costs

No explicit code changes are needed; tracing is automatic via environment variables.

### Minimum Configuration

You only need two environment variables for tracing:

```env
LANGSMITH_API_KEY=your_api_key_here
LANGSMITH_TRACING=true
```

Optional variables for customization:
- `LANGSMITH_ENDPOINT` — Server URL (defaults to official LangSmith endpoint)
- `LANGCHAIN_PROJECT` — Project name for organizing traces (defaults to `default`)

### Getting Started with LangSmith

1. Sign up for an account at https://smith.langchain.com/
2. Get your API key from the settings page
3. Add it to your `.env` file as `LANGSMITH_API_KEY`
4. Run your application — traces will appear in the LangSmith dashboard

## Development

### Running with Auto-Reload

For development with file watching, use a development server:

```bash
# Option 1: Simple re-run on file changes
watchmedo auto-restart -d . -p '*.py' -- python main.py

# Option 2: Use an IDE with built-in reload support
# (Most Python IDEs support automatic re-run on file save)
```

### Adding More Tools

To add more MCP servers with additional tools:

1. Create a new MCP server in `servers/`
2. Update `main.py` to connect to the new server
3. The tools will automatically be available to the agent

Example structure for a new server:

```python
# servers/example_server.py
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Example")

@mcp.tool()
def example_tool(param: str) -> str:
    """Description of your tool"""
    return result
```

Then in `main.py`, create multiple server connections:

```python
# Connect to multiple servers
servers = [
    StdioServerParameters(command="python", args=["servers/math_server.py"]),
    StdioServerParameters(command="python", args=["servers/example_server.py"]),
]

for server_params in servers:
    # Connect and load tools from each server
    pass
```

## Learning Resources

- [Model Context Protocol Docs](https://modelcontextprotocol.io/)
- [LangChain Docs](https://python.langchain.com/)
- [LangSmith Documentation](https://docs.smith.langchain.com/)
- [OpenAI Models](https://platform.openai.com/docs/models)

## License

Add license information here.
