from fastmcp import FastMCP
from ddgs import DDGS

# 1. MCP 서버 정의
mcp = FastMCP("ddg_search_server")

# 2. DuckDuckGo 검색 도구 등록
@mcp.tool()
def duckduckgo_search(query: str, max_results: int = 3) -> str:
    """
    Performs a web search using DuckDuckGo.
    Use this to find real-time information.
    """
    try:
        results = []
        with DDGS() as ddgs:
            search_gen = ddgs.text(query, max_results=max_results)
            for r in search_gen:
                results.append(f"Title: {r['title']}\nLink: {r['href']}\nSnippet: {r['body']}\n")
        return "\n".join(results) if results else "No results found."
    except Exception as e:
        return f"Error: {str(e)}"

# 3. 서버 실행 (SSE 방식, 포트 8000)
if __name__ == "__main__":
    print(">>> Starting DuckDuckGo MCP Server on port 8000...")
    mcp.run(transport="sse", port=8000)
