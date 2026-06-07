import asyncio
from pathlib import Path

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Load environment variables from .env file
load_dotenv()


async def main():
    llm = ChatOpenAI(model="gpt-4o-mini")

    # Get the path to the math_server.py relative to this file
    server_script = Path(__file__).parent / "servers" / "math_server.py"

    server_params = StdioServerParameters(
        command="python",
        args=[str(server_script)],
    )
    print("Hello from langchain-mcp-adapters!")


if __name__ == "__main__":
    asyncio.run(main())
