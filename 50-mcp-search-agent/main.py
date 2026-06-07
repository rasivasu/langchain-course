import asyncio
import logging
import os
import sys

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("MCPAgentHost")

load_dotenv()


async def run_mcp_agent() -> None:
    # Validate environment
    if not os.getenv("OPENAI_API_KEY"):
        logger.error("OPENAI_API_KEY is not set.")
        return

    # Define server parameters to connect to our server.py
    server_params = StdioServerParameters(
        command=sys.executable,
        args=[os.path.join(os.path.dirname(__file__), "server.py")],
        env=os.environ.copy(),
    )

    try:
        # Connect to the MCP server using stdio_client
        async with stdio_client(server_params) as (read, write):
            # Create a MCP Client to communicate with the MCP server
            async with ClientSession(read, write) as session:
                # Initialize the connection and list available tools from the MCP server
                await session.initialize()

                logger.info("--- HOST: Loading MCP Tools ---")
                tools = await load_mcp_tools(session)

                llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

                # Use create_agent for robust tool calling (LangChain 1.3+)
                agent = create_agent(llm, tools)

                query = "search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details"
                logger.info(f"--- HOST: Querying agent with: {query} ---")

                result = await agent.ainvoke(
                    {"messages": [HumanMessage(content=query)]}
                )

                print("\n--- FINAL ANSWER ---")
                print(result["messages"][-1].content)

    except Exception as e:
        logger.error(f"Failed to run agent: {e}")


def run_mcp_agent_cli():
    """CLI entry point for the agent."""
    asyncio.run(run_mcp_agent())


if __name__ == "__main__":
    run_mcp_agent_cli()
