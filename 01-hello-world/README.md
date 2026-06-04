# Hello World: LangChain Basics

A simple introduction to LangChain, demonstrating how to set up the environment and make your first LLM call.

## 📚 Foundational Research

The ability of Large Language Models to follow instructions and perform tasks without specific training is rooted in the concept of few-shot learning and instruction following:

- **GPT-3:** [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) (Brown et al., 2020). This seminal paper demonstrated that scaling models to 175B parameters allows them to perform tasks via in-context learning, which is the basis for how we interact with LLMs today. (See `docs/gpt3_few_shot_paper.pdf`)

## Overview

This project serves as the "Hello World" for LangChain. it covers:
- Setting up `.env` with API keys
- Initializing a Chat Model (OpenAI)
- Using `PromptTemplate` to structure queries
- Extracting information from a text snippet

## Setup

1. Install dependencies:
   ```bash
   uv sync
   ```

2. Configure environment:
   Create a `.env` file with your `OPENAI_API_KEY`.

3. Run the script:
   ```bash
   python main.py
   ```

## Learning Points
- How LangChain interacts with OpenAI models.
- The role of `dotenv` in managing secrets.
- Basic prompt engineering with `PromptTemplate`.
