## MPC Docs Server

This is a simple MCP (Model Context Protocol) server for retrieving information from the official documentation of Langchain, Llama Index, and OpenAI. It provides a tool that can be used by MCP-compatible applications to search and retrieve relevant documentation snippets.

## Features

-   **Documentation Retrieval:** Fetches content from the official documentation of Langchain, Llama Index, and OpenAI.
-   **MCP Compatibility:** Implements an MCP server, allowing it to be easily integrated with other MCP-compatible applications.
-   **Simple Tool:** Exposes a `get_docs` tool that accepts a query and library name, returning relevant documentation snippets.

## Setup

1.  **Install Dependencies:**

    ```bash
    pip install python-dotenv mcp
    ```

2.  **Environment Variables:**

    Create a `.env` file in the root directory and add the following:

    ```
    SERPER_API_KEY=YOUR_SERPER_API_KEY
    ```

    You'll need a SERPER API key to use the web search functionality. You can obtain one from [Serper.dev](https://serper.dev/). We are using the Serper API to search the web for relevant documentation.

3.  **Run the Server:**

    ```bash
    uv server/main.py
    ```


