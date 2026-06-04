# Reflexion Agent (Advanced Actor-Critic)

An advanced implementation of the **Reflexion** pattern (Actor-Critic) that combines self-reflection with external tool use and search.

## 🌟 Inspiration
This project is inspired by and based on the following resources:
- [LangGraph Course](https://github.com/emarco177/langgraph-course) by Eden Marco.

## 📚 Foundational Research
The architecture of this project is based on the following key research paper:
- **Reflexion:** [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) - Introduces the concept of "verbal" reinforcement learning, where agents learn through self-reflection and linguistic feedback rather than traditional weight updates. (See `docs/reflexion_paper.pdf`)

## 🏗️ Architecture
The system is built as a stateful graph using **LangGraph**. The workflow ensures that the agent iteratively improves its response through self-critique and external research.

### Core Nodes:
1. **Initial Draft (Actor)**: Generates the first response and identifies research needs.
2. **Tool Execution**: Performs external searches (Tavily) to gather missing information or verify facts.
3. **Revision (Revisor)**: Critiques the draft, incorporates search results, and produces an improved answer.

### Control Flow:
- The graph starts with an **Initial Draft**.
- If the model identifies a need for more information, it transitions to **Tool Execution**.
- The loop continues with **Revision** until the `MAX_ITERATIONS` limit is reached or the answer meets the quality standards.

## 🚀 Key Features
- **Self-Correction**: Uses an internal critique mechanism to identify weaknesses in its own responses.
- **External Tool Integration**: Dynamically triggers real-time web searches via **Tavily**.
- **Structured Outputs**: Leverages Pydantic schemas and OpenAI's Structured Outputs for reliable drafting and revision.
- **Stateful Iteration**: Managed by **LangGraph** to maintain context and control the iterative loop effectively.

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
```

### Installation
Using `uv` (recommended):
```bash
uv sync
```

## 📖 Usage
Run the main application to start the Reflexion loop:
```bash
python main.py
```

## 📂 Project Structure
```text
├── docs/            # Foundational research paper
├── chains.py        # LLM chains for drafting and revision
├── main.py          # Graph definition and orchestration
├── schemas.py       # Pydantic models for structured outputs
├── tool_executor.py # Logic for executing external tool calls
├── pyproject.toml   # Project dependencies
└── uv.lock          # Dependency lock file
```
