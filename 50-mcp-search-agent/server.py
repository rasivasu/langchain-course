import os
import logging
from dotenv import load_dotenv
from fastmcp import FastMCP
from tavily import TavilyClient

# Configure logging to stderr
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("TavilySearchServer")

load_dotenv()

# Validate API Key
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
if not TAVILY_API_KEY:
    logger.error("TAVILY_API_KEY is not set in environment variables.")
    raise ValueError("TAVILY_API_KEY is required.")

# Initialize FastMCP Server
mcp = FastMCP("TavilySearchServer")

# Initialize Tavily Client
tavily = TavilyClient(api_key=TAVILY_API_KEY)

@mcp.tool()
def search_web(query: str) -> str:
    """
    Search the web using Tavily.
    
    Args:
        query: The search query to execute.
    
    Returns:
        The search results as a string.
    """
    logger.info(f"Executing search for: {query}")
    results = tavily.search(query=query)
    return str(results)

if __name__ == "__main__":
    mcp.run()
