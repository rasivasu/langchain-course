# 🦜 LangChain Course: From Zero to Agent Hero

A collection of projects covering the LangChain ecosystem, from basic LLM integration to advanced agentic patterns using LangGraph.

## 📁 Repository Structure

Each directory in this repository represents a specific module or project in the LangChain learning path.

| Module | Project Name | Description | Key Technologies |
|:---|:---|:---|:---|
| **01** | [**Hello World**](./01-hello-world) | Basic setup, instructions following, and first LLM call. | OpenAI, Few-Shot |
| **02** | [**Search Agent**](./02-search-agent) | Building agents that autonomously use web search tools. | Tavily, Tool-use |
| **03** | [**Agents Under the Hood**](./03-agents-under-the-hood) | Deep dive into agent loops, ReAct prompts, and regex parsing. | Ollama, CoT, ReAct |
| **04** | [**RAG Gist**](./04-rag-gist) | Foundational Retrieval Augmented Generation with vector stores. | Pinecone, LCEL |
| **05** | [**Doc Helper**](./05-documentation-helper) | A full-stack RAG application for intelligent documentation search. | Streamlit, Tavily |
| **06** | [**ReAct Agent**](./06-react-agent-function-calling) | ReAct pattern implemented using LangGraph and ToolNode. | LangGraph, ToolNode |
| **07** | [**Reflection Agent**](./07-reflection-agent) | Self-correcting agents that iterate and critique their output. | Self-Correction |
| **08** | [**Reflexion Agent**](./08-reflexion-agent) | Advanced Actor-Critic model with tool-assisted self-reflection. | Actor-Critic |
| **09** | [**Agentic RAG**](./09-agentic-rag) | The pinnacle: CRAG and Self-RAG for self-correcting retrieval. | CRAG, Self-RAG |

## 📚 Research Library

This repository links practical implementations to foundational AI research. Each module contains a `docs/` folder with the relevant seminal papers:

*   **Prompting**: [Few-Shot Learning (GPT-3)](./01-hello-world/docs/gpt3_few_shot_paper.pdf), [Chain-of-Thought](./03-agents-under-the-hood/docs/chain_of_thought_paper.pdf).
*   **Agent Architecture**: [ReAct](./06-react-agent-function-calling/docs/react_paper.pdf), [Toolformer](./02-search-agent/docs/toolformer_paper.pdf), [Reflexion](./08-reflexion-agent/docs/reflexion_paper.pdf).
*   **RAG Evolution**: [Original RAG Paper](./04-rag-gist/docs/original_rag_paper.pdf), [Corrective RAG (CRAG)](./09-agentic-rag/docs/Corrective-RAG_CRAG.pdf), [Self-RAG](./09-agentic-rag/docs/Self-RAG_Self-Reflection.pdf).

## 🚀 Getting Started

### Prerequisites

- **Python 3.11+**
- **[uv](https://github.com/astral-sh/uv)** (highly recommended for lightning-fast dependency management)
- API Keys for **OpenAI**, **Tavily**, and **Pinecone**.

### Installation & Execution

Each module is an independent project. Navigate to a directory and use `uv` to sync and run:

```bash
cd 09-agentic-rag
uv sync
python main.py
```

## 🧠 Learning Path

1.  **Foundations**: Start with `01` and `04` to master basic LLM calls and the core RAG pattern.
2.  **Mechanics**: Move to `02` and `03` to understand how agents use tools at both a high and low level.
3.  **The LangGraph Shift**: Explore `06` and `07` to transition from linear chains to stateful, cyclic graphs.
4.  **Advanced Reasoning**: Master `08` (Actor-Critic) and `09` (Agentic RAG) to build production-grade self-correcting systems.

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
