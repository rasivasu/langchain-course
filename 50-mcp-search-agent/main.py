import asyncio
import os
import sys
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()

async def run_mcp_agent():
    # Define server parameters to connect to our server.py
    server_params = StdioServerParameters(
        command=sys.executable,
        args=[os.path.join(os.path.dirname(__file__), "server.py")],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # List available tools from the MCP server
            mcp_tools = await session.list_tools()
            
            # Create LangChain-compatible tools from MCP tools
            # In a real-world scenario, we'd automate this conversion.
            # For this simple example, we'll manually wrap the 'search_web' tool.
            
            @tool
            async def search_web(query: str) -> str:
                """Search the web using the MCP server's search_web tool."""
                result = await session.call_tool("search_web", arguments={"query": query})
                return str(result.content)

            tools = [search_web]
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
            
            # create_agent is an abstraction that handles the loop
            agent = create_agent(model=llm, tools=tools)

            print("--- HOST: Querying agent ---")
            query = "search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details"
            
            result = await agent.ainvoke(
                {
                    "messages": [HumanMessage(content=query)]
                }
            )
            
            print("\n--- FINAL ANSWER ---")
            print(result["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(run_mcp_agent())
