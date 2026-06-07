from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")


@mcp.tool()
def get_weather(city: str) -> str:
    """Get the weather for a given city."""
    return f"It's always sunny in {city}"


if __name__ == "__main__":
    mcp.run(transport="sse")
