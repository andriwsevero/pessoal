from typing import Optional

from claude_agent_sdk import AgentDefinition, ClaudeAgentOptions

from core.config import ROOT_DIR


def build_domain_options(
    *,
    domain_prompt: str,
    agents: dict[str, AgentDefinition],
    mcp_servers: Optional[dict] = None,
    extra_allowed_tools: Optional[list[str]] = None,
    max_turns: int = 6,
) -> ClaudeAgentOptions:
    return ClaudeAgentOptions(
        cwd=str(ROOT_DIR),
        system_prompt={"type": "custom", "prompt": domain_prompt},
        setting_sources=[],
        agents=agents,
        mcp_servers=mcp_servers or {},
        allowed_tools=["Agent", *(extra_allowed_tools or [])],
        permission_mode="default",
        max_turns=max_turns,
    )
