# Agentic RAG with LangGraph

This project implements an **Agentic RAG (Corrective RAG)** workflow using **LangGraph**. It is designed to move beyond simple retrieve-and-generate pipelines by incorporating a grading step that evaluates the relevance of retrieved documents and dynamically supplements the context with a web search if necessary.

## 🌟 Inspiration
This project is inspired by and based on the following resources:
- [LangGraph Course - Agentic RAG](https://github.com/emarco177/langgraph-course/tree/project/agentic-rag) by Eden Marco.
- [Mistral AI Cookbook - LangGraph CRAG](https://github.com/mistralai/cookbook/tree/main/third_party/langchain) by Mistral AI and LangChain.

## 📚 Foundational Research
The architecture of this project is based on the following key research papers:
- **Corrective RAG (CRAG):** [Corrective Retrieval Augmented Generation](https://arxiv.org/abs/2401.15884) - Introduces the concept of using a retrieval evaluator to trigger web searches for missing or irrelevant knowledge. (See `docs/Corrective-RAG_CRAG.pdf`)
- **Self-RAG:** [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://arxiv.org/abs/2310.11511) - Focuses on LLMs critiquing their own retrieved documents and generations for factuality. (See `docs/Self-RAG_Self-Reflection.pdf`)
- **Adaptive RAG:** [Adaptive-RAG: Learning to Adapt Retrieval-Augmented LLMs through Question Complexity](https://arxiv.org/abs/2403.14403) - Explains how to route queries based on their complexity to different RAG strategies. (See `docs/Adaptive-RAG_Routing.pdf`)

## 🏗️ Architecture
The system is built as a stateful graph using LangGraph. The workflow ensures that only relevant information is used for generation, improving the accuracy and reliability of the final answer.

![Graph Visualization](graph.png)

### Core Nodes:
1.  **Retrieve:** Fetches documents from a local **ChromaDB** vector store (containing knowledge from Lilian Weng's blog posts).
2.  **Grade Documents:** A decision node that uses a LLM (GPT-4o-mini) with structured output to assess the relevance of each retrieved document.
3.  **Web Search:** If any document is found irrelevant, the system triggers a **Tavily Web Search** to find supplemental information.
4.  **Generate:** Synthesizes the final answer using the filtered and supplemented context.

### Control Flow:
- The graph starts at the **Retrieve** node.
- After retrieval, it moves to **Grade Documents**.
- A conditional edge determines the next step:
    - If **all** documents are relevant, it proceeds directly to **Generate**.
    - If **any** document is irrelevant, it routes to **Web Search** before final generation.

## 🚀 Key Features
- **Corrective RAG (CRAG):** Dynamically corrects the RAG process based on document quality.
- **Structured Grading:** Uses OpenAI's Structured Outputs to ensure reliable binary relevance scores.
- **Stateful Orchestration:** Leverages LangGraph to manage complex control flows and state transitions.
- **Hybrid Knowledge:** Combines local vector search with real-time web search Fallback.

## 🛠️ Setup & Installation

### Prerequisites
- Python 3.13+
- [Tavily API Key](https://tavily.com/)
- [OpenAI API Key](https://platform.openai.com/)

### Environment Variables
Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
USER_AGENT=AgenticRAG/1.0
```

### Installation
Using `uv` (recommended):
```bash
uv sync
```

### Data Ingestion
The project includes an `ingestion.py` script that loads content from Lilian Weng's blog posts into a local ChromaDB collection.
```bash
python ingestion.py
```

## 📖 Usage
Run the main application to query the agent:
```bash
python main.py
```

By default, it asks: *"What is agent memory?"* and follows the agentic workflow to provide a response.

## 📂 Project Structure
```text
├── docs/            # Foundational research papers (CRAG, Self-RAG, Adaptive RAG)
├── graph/
│   ├── chains/      # LLM chains for grading and generation
│   ├── nodes/       # Graph node implementations (retrieve, grade, search, generate)
│   ├── graph.py     # Graph definition and orchestration
│   ├── state.py     # TypedDict for graph state
│   └── consts.py    # Shared constants
├── ingestion.py     # Document loading and vector store setup
└── main.py          # Entry point
```
