# 🦜 LangChain Course: From Zero to Agent Hero

A comprehensive collection of tutorials and projects covering the LangChain ecosystem, from basic LLM integration to advanced agentic patterns using LangGraph.

## 📁 Repository Structure

Each directory in this repository represents a specific module or project in the LangChain learning path.

| Module | Project Name | Description | Key Technologies |
|:---|:---|:---|:---|
| **01** | [**Hello World**](./01-hello-world) | Basic setup and first LLM call. | OpenAI, PromptTemplates |
| **02** | [**Search Agent**](./02-search-agent) | Building agents that use web search tools. | Tavily, create_agent |
| **03** | [**Agents Under the Hood**](./03-agents-under-the-hood) | Deep dive into agent loops and ReAct prompts. | Ollama, Regex, Raw Loops |
| **04** | [**RAG Gist**](./04-rag-gist) | Introduction to Retrieval Augmented Generation. | Pinecone, LCEL |
| **05** | [**Doc Helper**](./05-documentation-helper) | A full-stack RAG application for documentation. | Streamlit, Pinecone, Tavily |
| **06** | [**ReAct Agent**](./06-react-agent-function-calling) | ReAct pattern with LangGraph and tool calling. | LangGraph, ToolNode |
| **07** | [**Reflection Agent**](./07-reflection-agent) | Self-correcting agents that iterate on output. | LangGraph, Reflection |
| **08** | [**Reflexion Agent**](./08-reflexion-agent) | Advanced Actor-Critic model with tool research. | LangGraph, Advanced RAG |

## 🚀 Getting Started

### Prerequisites

- **Python 3.11+**
- **[uv](https://github.com/astral-sh/uv)** (recommended for dependency management)
- API Keys for **OpenAI**, **Tavily**, and **Pinecone**.

### Installation

Clone the repository and install dependencies in the respective project directories:

```bash
# Example for a specific module
cd 06-react-agent-function-calling
uv sync
```

### Environment Setup

Most projects require a `.env` file in their respective root folder:

```env
OPENAI_API_KEY=sk-...
TAVILY_API_KEY=tvly-...
PINECONE_API_KEY=...
INDEX_NAME=...
```

## 🧠 Learning Path

1. **Foundations**: Start with `01` and `04` to understand basic LLM calls and RAG.
2. **Agents Basics**: Move to `02` and `03` to see how agents work at a high and low level.
3. **Advanced Agents**: Explore `06`, `07`, and `08` to master LangGraph and complex agentic architectures.
4. **Full Stack**: Check out `05` for a real-world application example.

## 🛠️ Tools Used

- **Framework**: [LangChain](https://github.com/langchain-ai/langchain) 🦜🔗
- **Orchestration**: [LangGraph](https://github.com/langchain-ai/langgraph) 🕸️
- **Models**: OpenAI (GPT-4o-mini, o4-mini), Ollama
- **Search**: [Tavily AI](https://tavily.com/) 🔍
- **Vector DB**: [Pinecone](https://www.pinecone.io/) 🌲
- **UI**: [Streamlit](https://streamlit.io/) 🖥️

---
*Maintained by [rasivasu](https://github.com/rasivasu)*

## 🙏 Acknowledgments & Credits

This repository is a collection of projects and tutorials from the excellent Udemy course:
**[LangChain- Agentic AI Engineering with LangChain & LangGraph](https://www.udemy.com/course/langchain/)** by **[Eden Marco](https://github.com/emarco177)**.

All the implementations and architectural patterns found here are based on the course's curriculum. I highly recommend the course to anyone looking to master Agentic AI.
