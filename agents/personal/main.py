import sys

from core import config  # noqa: F401  (garante ANTHROPIC_API_KEY carregada)
from core.orchestrator import build_domain_options
from core.runner import run

from agents.personal.subagents import PERSONAL_AGENTS, PERSONAL_MCP_SERVERS

ORCHESTRATOR_PROMPT = (
    "Você é o orquestrador do domínio PESSOAL do agent-network. "
    "Delegue pedidos pessoais ao subagente especializado mais adequado via tool Agent. "
    "Nunca misture ou acesse informações do domínio de trabalho do usuário."
)


def build_options():
    return build_domain_options(
        domain_prompt=ORCHESTRATOR_PROMPT,
        agents=PERSONAL_AGENTS,
        mcp_servers=PERSONAL_MCP_SERVERS,
        extra_allowed_tools=["mcp__utils__count_words"],
    )


def main():
    prompt = " ".join(sys.argv[1:]) or (
        "Use o agente journal-summarizer para resumir: 'Hoje me senti cansado mas "
        "consegui terminar a leitura do livro, quero começar a correr de novo na "
        "próxima semana e preciso organizar as contas do mês.'"
    )
    run(prompt, build_options())


if __name__ == "__main__":
    main()
