# agent-network

Rede de agentes e subagentes construída com o [Claude Agent SDK](https://docs.claude.com/en/docs/agent-sdk) (Python), separada em dois domínios independentes — `work` (trabalho) e `personal` (pessoal) — que compartilham a mesma infraestrutura base em `core/`.

Cada domínio tem seu próprio orquestrador: ele recebe um pedido e delega para o subagente especializado mais adequado via tool `Agent`. Os domínios não compartilham sessão, contexto nem permissões entre si.

## Setup

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt

copy .env.example .env
# edite .env e cole sua ANTHROPIC_API_KEY (https://console.anthropic.com/settings/keys)
```

## Rodando

```powershell
python -m agents.work.main
python -m agents.personal.main

# ou com um pedido customizado:
python -m agents.work.main "Use o agente note-summarizer para resumir: ..."
```

Cada execução imprime a resposta do subagente, uma linha confirmando a delegação (`-> delegado ao subagente: ...`) e o custo da chamada.

## Estrutura

```
core/              # infraestrutura compartilhada pelos dois domínios
  config.py        # carrega .env e valida ANTHROPIC_API_KEY
  orchestrator.py  # fábrica de ClaudeAgentOptions
  runner.py        # executa query() e imprime resultado
  tools.py         # tools customizadas compartilhadas (MCP in-process)
agents/
  work/            # domínio de trabalho: orquestrador + subagentes
  personal/        # domínio pessoal: orquestrador + subagentes
```

## Como adicionar um novo agente

1. Escolha o domínio (`work` ou `personal`), ou crie um novo domínio seguindo o mesmo padrão de pasta (um `main.py` + um `subagents.py`).
2. Adicione uma entrada no dict `*_AGENTS` daquele domínio (`agents/<domínio>/subagents.py`) com:
   - `description`: frase clara do que o agente faz e quando usá-lo — é isso que o orquestrador usa para decidir a quem delegar.
   - `prompt`: instruções especializadas do subagente.
   - `tools` / `model`: opcional, restrinja conforme necessário.
3. Se o agente precisar de uma tool nova, defina-a em `core/tools.py` (ou um arquivo de tools próprio do domínio) com `@tool(...)` e registre-a em `create_sdk_mcp_server(...)`, depois inclua o server no dict `mcp_servers` passado a `build_domain_options`.
4. Teste mencionando o agente explicitamente no prompt (ex: `"Use o agente <nome> para ..."`) para confirmar que a delegação funciona antes de confiar no roteamento automático por `description`.

## Segurança

Nunca comite o arquivo `.env` — ele já está no `.gitignore`. Use sempre `.env.example` como referência de quais variáveis são necessárias.
