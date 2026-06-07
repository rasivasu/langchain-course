import asyncio
import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


async def main():

    # Verify LangSmith configuration is loaded
    langchain_project = os.getenv("LANGCHAIN_PROJECT")
    langsmith_tracing = os.getenv("LANGSMITH_TRACING")

    print("Hello from 10-langchain-mcp-adapters!")
    print(f"LangChain Project: {langchain_project}")
    print(f"LangSmith Tracing: {langsmith_tracing}")


if __name__ == "__main__":
    asyncio.run(main())
