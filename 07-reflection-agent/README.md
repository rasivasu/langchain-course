# Reflection Agent (LangGraph)

An implementation of the Reflection pattern where an agent generates content and then critiques itself to improve the output.

## 📚 Foundational Research

The iterative self-correction pattern used here is based on research into self-feedback loops in LLMs:

- **Self-Refine:** [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651) (Madaan et al., 2023). This paper demonstrates that models can significantly improve their own outputs by generating a draft, critiquing it, and then refining it based on that feedback. (See `docs/self_refine_paper.pdf`)

## Overview

This agent follows a cyclic graph:
1. **Generate**: Create an initial version of a tweet.
2. **Reflect**: Critique the generated tweet as a "viral twitter influencer".
3. **Loop**: Feed the critique back into the Generator to create a revised version.
4. **End**: Terminate after a fixed number of iterations.

## Features
- **Cyclic Graph**: Implemented using `LangGraph`.
- **State Management**: Uses `MessageGraph` to maintain the history of generations and reflections.
- **Prompt Engineering**: Uses specialized prompts for Generation and Reflection.

## Setup

1. Install dependencies:
   ```bash
   uv sync
   ```

2. Configure environment:
   Set `OPENAI_API_KEY` in your `.env` file.

3. Run the agent:
   ```bash
   python main.py
   ```

## Learning Points
- How to implement feedback loops in LLM applications.
- Using `LangGraph` to manage multi-step, iterative processes.
- The power of "Self-Correction" in improving LLM performance.
