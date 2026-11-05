from claude_agent_sdk import AgentDefinition

from core.tools import utils_server

WORK_AGENTS = {
    "note-summarizer": AgentDefinition(
        description=(
            "Resume anotações, atas de reunião ou e-mails de trabalho em bullets objetivos. "
            "Use quando o usuário pedir para resumir texto do contexto de trabalho."
        ),
        prompt=(
            "Você é um assistente de resumo para o ambiente de trabalho do usuário. "
            "Resuma o texto recebido em até 5 bullets objetivos, destacando decisões e "
            "próximos passos. Nunca invente informação que não esteja no texto original."
        ),
        tools=["mcp__utils__count_words"],
        model="haiku",
    ),
}

WORK_MCP_SERVERS = {"utils": utils_server}
