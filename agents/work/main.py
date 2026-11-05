import sys

from core import config  # noqa: F401  (garante ANTHROPIC_API_KEY carregada)
from core.orchestrator import build_domain_options
from core.runner import run

from agents.work.subagents import WORK_AGENTS, WORK_MCP_SERVERS

ORCHESTRATOR_PROMPT = (
    "Você é o orquestrador do domínio de TRABALHO do agent-network. "
    "Delegue pedidos de trabalho ao subagente especializado mais adequado via tool Agent. "
    "Nunca misture ou acesse informações do domínio pessoal do usuário."
)


def build_options():
    return build_domain_options(
        domain_prompt=ORCHESTRATOR_PROMPT,
        agents=WORK_AGENTS,
        mcp_servers=WORK_MCP_SERVERS,
        extra_allowed_tools=["mcp__utils__count_words"],
    )


def main():
    prompt = " ".join(sys.argv[1:]) or (
        "Use o agente note-summarizer para resumir: 'Reunião de hoje: decidimos adiar "
        "o lançamento para sexta, Ana vai revisar o contrato, e precisamos confirmar "
        "orçamento com o financeiro até quarta.'"
    )
    run(prompt, build_options())


if __name__ == "__main__":
    main()
