from claude_agent_sdk import AgentDefinition

from core.tools import utils_server

PERSONAL_AGENTS = {
    "journal-summarizer": AgentDefinition(
        description=(
            "Resume anotações pessoais, diário ou pensamentos soltos em bullets curtos. "
            "Use quando o usuário pedir para resumir texto do contexto pessoal."
        ),
        prompt=(
            "Você é um assistente pessoal de organização. Resuma o texto recebido em até "
            "5 bullets curtos e acolhedores, sem julgamento, destacando sentimentos e "
            "ações que o usuário mencionou querer tomar."
        ),
        tools=["mcp__utils__count_words"],
        model="haiku",
    ),
}

PERSONAL_MCP_SERVERS = {"utils": utils_server}
