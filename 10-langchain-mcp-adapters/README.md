# LangChain MCP Adapters

A project demonstrating the integration of LangChain with Model Context Protocol (MCP) adapters and LangSmith tracing.

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
```

**Security Note:** The `.env` file is excluded from version control (see `.gitignore`). Never commit this file to avoid exposing API keys.

## Running the Project

```bash
python main.py
```

This will:
- Load environment variables from `.env`
- Display the LangChain project and tracing configuration
- Execute the async main function

## Project Structure

```
.
├── .env                 # Environment variables (not in version control)
├── .gitignore          # Git ignore rules
├── .python-version     # Python version specification
├── README.md           # This file
├── pyproject.toml      # Project metadata and dependencies
├── uv.lock             # Lock file for reproducible builds
└── main.py             # Main application entry point
```

## Dependencies

- **langchain-mcp-adapters** (≥0.2.2): MCP adapter utilities for LangChain
- **langchain-openai** (≥1.2.2): OpenAI integration for LangChain
- **langgraph** (≥1.2.4): Graph-based workflow framework
- **python-dotenv** (≥1.2.2): Load environment variables from `.env` files

## LangSmith Integration

This project is configured to use [LangSmith](https://smith.langchain.com/) for tracing and monitoring LangChain applications. When `LANGSMITH_TRACING=true`, all LangChain operations are automatically logged to LangSmith for debugging and performance analysis.

To use LangSmith:
1. Sign up for an account at https://smith.langchain.com/
2. Get your API key from the settings
3. Add it to your `.env` file as `LANGSMITH_API_KEY`

## Development

For development with auto-reloading, consider using:

```bash
uvicorn main:app --reload  # If building a web service
```

Or simply re-run `python main.py` during development.

## License

Add license information here.
