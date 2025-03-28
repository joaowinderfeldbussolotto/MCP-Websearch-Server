from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
from web_context import search_web, fetch_url
load_dotenv()

mcp = FastMCP("docs")

USER_AGENT = "docs-app/1.0"
SERPER_URL="https://google.serper.dev/search"

docs_urls = {
    "langchain": "python.langchain.com/docs",
    "llama-index": "docs.llamaindex.ai/en/stable",
    "openai": "platform.openai.com/docs",
}


@mcp.tool()  
async def get_docs(query: str, library: str):
  """
  Search the latest docs for a given query and library.
  Supports langchain, openai, and llama-index.

  Args:
    query: The query to search for (e.g. "Chroma DB")
    library: The library to search in (e.g. "langchain")

  Returns:
    Text from the docs
  """
  if library not in docs_urls:
    raise ValueError(f"Library {library} not supported by this tool")
  
  query = f"site:{docs_urls[library]} {query}"
  results = await search_web(query)
  if len(results["organic"]) == 0:
    return "No results found"
  
  text = ""
  for result in results["organic"]:
    text += await fetch_url(result["link"])
    
  return text


if __name__ == "__main__":
    mcp.run(transport="stdio")