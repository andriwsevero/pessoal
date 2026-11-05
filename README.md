# agent-network

Rede de agentes/subagentes do Claude Code: um projeto único, com uma "cabeça" (a sessão principal do Claude Code, guiada pelo `CLAUDE.md` raiz) que delega para subagentes especializados em `.claude/agents/`, organizados por tópico (`trabalho-*`, `pessoal-*`, e outros que forem surgindo).

Roda inteiramente dentro da sua assinatura Claude Pro/Max (login via `claude login`), sem precisar de API key separada nem custo por uso — porque usa os subagentes nativos do Claude Code, não o Agent SDK.

## Como usar

```powershell
cd agent-network
claude
```

Dentro da sessão, peça algo que combine com a `description` de um subagente — o Claude delega automaticamente — ou mencione o agente explicitamente: `"Use o agente trabalho-resumo-notas para resumir: ..."`.

## Estrutura

```
CLAUDE.md                        # contexto da "cabeça": como e quando delegar, princípios de eficiência
.claude/agents/
  trabalho-resumo-notas.md       # subagente de exemplo (tópico trabalho)
  pessoal-resumo-diario.md       # subagente de exemplo (tópico pessoal)
```

## Como adicionar um novo agente

1. Escolha o tópico (prefixo `trabalho-` ou `pessoal-`), ou crie um novo tópico se fizer sentido.
2. Crie `.claude/agents/<topico>-<nome>.md` com frontmatter:
   ```yaml
   ---
   name: <topico>-<nome>
   description: Frase clara do que faz e QUANDO usar — é isso que decide a delegação automática.
   tools: <lista mínima necessária, ou omita se precisar de tudo>
   model: haiku   # ou sonnet/opus/inherit
   ---
   Prompt/instruções do subagente.
   ```
3. Teste mencionando o agente explicitamente no pedido antes de confiar no roteamento automático por `description`.

## Eficiência (token/custo)

- Modelo menor (`haiku`) para tarefas simples; só suba pra `sonnet`/`inherit` quando precisar de raciocínio mais pesado.
- `tools` restrito ao mínimo necessário por subagente.
- `CLAUDE.md` e prompts de subagente curtos — o `CLAUDE.md` raiz é carregado em toda sessão.

Documentação oficial de subagentes: https://code.claude.com/docs/en/sub-agents
