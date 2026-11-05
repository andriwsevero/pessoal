from claude_agent_sdk import create_sdk_mcp_server, tool


@tool("count_words", "Conta palavras e caracteres de um texto", {"text": str})
async def count_words(args):
    text = args["text"]
    return {
        "content": [
            {"type": "text", "text": f"{len(text.split())} palavras, {len(text)} caracteres."}
        ]
    }


utils_server = create_sdk_mcp_server(name="utils", version="0.1.0", tools=[count_words])
