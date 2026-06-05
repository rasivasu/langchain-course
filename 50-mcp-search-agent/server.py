import os
from dotenv import load_dotenv
from fastmcp import FastMCP
from tavily import TavilyClient

load_dotenv()

# Initialize FastMCP Server
mcp = FastMCP("TavilySearchServer")

# Initialize Tavily Client
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@mcp.tool()
def search_web(query: str) -> str:
    """
    Search the web using Tavily.
    
    Args:
        query: The search query to execute.
    
    Returns:
        The search results as a string.
    """
    print(f"--- SERVER: Executing search for: {query} ---")
    results = tavily.search(query=query)
    return str(results)

if __name__ == "__main__":
    mcp.run()
