import asyncio

from claude_agent_sdk import AssistantMessage, ResultMessage, TextBlock, ToolUseBlock, query


async def _run(prompt: str, options) -> str:
    final_text = ""
    async for message in query(prompt=prompt, options=options):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    print(block.text)
                    final_text = block.text
                elif isinstance(block, ToolUseBlock) and block.name == "Agent":
                    print(f"  -> delegado ao subagente: {block.input.get('subagent_type')}")
        elif isinstance(message, ResultMessage):
            custo = f"${message.total_cost_usd:.4f}" if message.total_cost_usd else "N/A"
            print(f"[concluído: {message.subtype}, custo: {custo}]")
    return final_text


def run(prompt: str, options) -> str:
    return asyncio.run(_run(prompt, options))
