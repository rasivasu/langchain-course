"""LangChain MCP Adapters Demo

This module demonstrates the integration of LangChain with Model Context Protocol (MCP) servers
using the langchain-mcp-adapters library. It connects to a local MCP server, loads tools,
and uses them with a LangChain agent powered by OpenAI's GPT-4o-mini model.

The example shows:
- Connection to an MCP server via stdio transport
- Tool discovery and pretty-printing
- Conversion of MCP tools to LangChain BaseTool objects
- Agent invocation with tool access
- LangSmith tracing integration (automatic via environment variables)

Environment Variables:
    LANGSMITH_API_KEY: Authentication token for LangSmith
    LANGSMITH_TRACING: Set to 'true' to enable tracing
    LANGCHAIN_PROJECT: Project name for organizing traces
    OPENAI_API_KEY: Authentication token for OpenAI
"""

import asyncio
from pathlib import Path
from pprint import pprint

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Load environment variables from .env file
# This enables LangSmith tracing and provides API keys
load_dotenv()


async def main() -> None:
    """Main async entry point for the MCP adapter demo.

    This function:
    1. Initializes a ChatOpenAI LLM client
    2. Connects to a local MCP server via stdio
    3. Discovers and displays available tools
    4. Converts MCP tools to LangChain BaseTool objects
    5. Creates an agent with the tools
    6. Invokes the agent with a sample question

    All operations are automatically traced to LangSmith when tracing is enabled.
    """
    print("Hello from langchain-mcp-adapters!")

    # Initialize the LLM client
    # gpt-4o-mini is cost-effective and suitable for prototyping
    # All LLM calls will be automatically traced to LangSmith
    llm = ChatOpenAI(model="gpt-4o-mini")

    # Construct the path to the math server script
    # Using Path(__file__).parent ensures portability across different machines and OS
    server_script = Path(__file__).parent / "servers" / "math_server.py"

    # Configure stdio connection parameters for the MCP server
    # stdio is ideal for local servers running on the same machine
    server_params = StdioServerParameters(
        command="python",
        args=[str(server_script)],
    )

    # Establish connection to MCP server
    # stdio_client is the transport layer that handles process communication
    async with stdio_client(server_params) as (read, write):
        # Create a ClientSession for MCP protocol communication
        # ClientSession handles JSON-RPC protocol, capability negotiation, and tool invocation
        async with ClientSession(read, write) as session:
            # Initialize the MCP connection with capability negotiation
            await session.initialize()
            print("Session is initialized")

            # Discover available tools from the MCP server
            # This returns a ListToolsResult containing metadata about each tool
            tools_result = await session.list_tools()

            # Format and display available tools for debugging
            # This helps verify what tools the server is exposing
            print("\nAvailable Tools:")
            tools_dict = {
                "meta": tools_result.meta,
                "nextCursor": tools_result.nextCursor,
                "tools": [
                    {
                        "name": tool.name,
                        "description": tool.description,
                        "inputSchema": tool.inputSchema,
                        "outputSchema": tool.outputSchema,
                    }
                    for tool in tools_result.tools
                ],
            }
            pprint(tools_dict)

            # Convert MCP tools to LangChain BaseTool objects
            # This adapter layer enables MCP tools to work seamlessly with LangChain agents
            # The conversion handles schema adaptation and tool invocation wrapping
            langchain_tools = await load_mcp_tools(session)

            # Create a LangChain agent with the converted tools
            # The agent uses the LLM to decide which tools to invoke and how
            agent = create_agent(llm, langchain_tools)

            # Invoke the agent with a sample question
            # The agent will decide which tools to use and orchestrate the calls
            # All actions (LLM calls, tool invocations) are traced to LangSmith
            result = await agent.ainvoke(
                {"messages": [HumanMessage(content="What is 2 + 2?")]}
            )

            # Extract and display the final response from the agent
            # result["messages"][-1] is the last message (the agent's response)
            print(result["messages"][-1].content)


if __name__ == "__main__":
    # Run the async main function
    # asyncio.run() handles event loop creation and cleanup
    asyncio.run(main())
