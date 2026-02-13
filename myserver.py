import json
from fastmcp import FastMCP

# 1. MCP 서버 인스턴스 생성
mcp = FastMCP("Advanced Data Tools")

# 2. 도구 등록
@mcp.tool()
def analyze_log_file(filepath: str) -> str:
    """
    Analyzes a log file and returns a summary of errors.
    Mock function for demo.
    """
    return f"Checked {filepath}: Found 3 Critical Errors, 12 Warnings."

@mcp.tool()
def query_customer_db(customer_id: str) -> str:
    """
    Retrieves customer information from the secure database.
    Returns a JSON string of the customer record.
    """
    # [FIX] dict 대신 JSON 문자열을 반환하여 MCP text 응답과 호환
    if customer_id == "C123":
        return json.dumps({"name": "Kim Agent", "plan": "Premium", "last_login": "2024-02-07"})
    return json.dumps({"error": "Customer not found"})

# 3. 서버 실행
if __name__ == "__main__":
    mcp.run()
