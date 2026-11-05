# agent-network

Rede de agentes e subagentes do Claude Code, separada em dois domínios **completamente isolados** — `work/` (trabalho) e `personal/` (pessoal) — cada um é seu próprio projeto Claude Code, com seu próprio `CLAUDE.md` e seus próprios subagentes em `.claude/agents/`.

Roda inteiramente dentro da sua assinatura Claude Pro/Max (login via `claude login`), sem precisar de API key separada nem custo por uso — porque usa os subagentes nativos do Claude Code, não o Agent SDK.

## Como usar

Abra um terminal dentro do domínio que quiser:

```powershell
cd work
claude
```

ou

```powershell
cd personal
claude
```

Dentro da sessão, peça algo que combine com a `description` de um subagente — o Claude delega automaticamente — ou mencione o agente explicitamente: `"Use o agente note-summarizer para resumir: ..."`.

## Estrutura

```
work/
  CLAUDE.md               # contexto/instruções do domínio de trabalho
  .claude/agents/
    note-summarizer.md    # subagente de exemplo
personal/
  CLAUDE.md               # contexto/instruções do domínio pessoal
  .claude/agents/
    journal-summarizer.md # subagente de exemplo
```

Como cada domínio é uma pasta de projeto separada, o Claude Code descobre e carrega **apenas** os subagentes e o `CLAUDE.md` daquela pasta — não há vazamento de contexto entre trabalho e pessoal.

## Como adicionar um novo agente

1. Escolha o domínio (`work/` ou `personal/`), ou crie um novo domínio seguindo o mesmo padrão de pasta (`<domínio>/CLAUDE.md` + `<domínio>/.claude/agents/`).
2. Crie `<domínio>/.claude/agents/<nome>.md` com frontmatter:
   ```yaml
   ---
   name: nome-do-agente
   description: Frase clara do que faz e QUANDO usar — é isso que decide a delegação automática.
   model: haiku   # ou sonnet/opus/inherit
   ---
   Prompt/instruções do subagente.
   ```
3. Teste mencionando o agente explicitamente no pedido antes de confiar no roteamento automático por `description`.

Documentação oficial de subagentes: https://code.claude.com/docs/en/sub-agents
