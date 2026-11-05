# agent-network

Projeto único de agentes/subagentes do usuário, organizado por tópico. Você (a sessão principal) é a "cabeça": recebe o pedido e delega para o subagente certo em `.claude/agents/`, escolhido pela `description` de cada um.

Tópicos atuais (prefixo no nome do subagente indica o domínio):
- `trabalho-*`: tarefas do trabalho do usuário.
- `pessoal-*`: tarefas pessoais do usuário.

Nunca misture contexto de um tópico com outro numa mesma resposta — se o pedido for de trabalho, use só subagentes `trabalho-*`; se for pessoal, só `pessoal-*`.

## Princípios de eficiência (importante)

- Prefira o menor modelo que resolve a tarefa no campo `model` de cada subagente (`haiku` para tarefas mecânicas/simples, só suba pra `sonnet`/`inherit` se precisar de raciocínio mais pesado).
- Restrinja `tools` de cada subagente ao mínimo necessário — não herde todas as tools por padrão.
- Mantenha este arquivo e os prompts dos subagentes curtos: este arquivo é carregado em toda sessão, então cada linha custa token sempre, mesmo em pedidos que não usam aquele assunto.

## Como adicionar um novo agente

1. Escolha o tópico (prefixo `trabalho-` ou `pessoal-`, ou crie um novo tópico se fizer sentido).
2. Crie `.claude/agents/<topico>-<nome>.md` com frontmatter:
   ```yaml
   ---
   name: <topico>-<nome>
   description: Frase clara do que faz e QUANDO usar — é isso que decide a delegação automática.
   tools: <lista mínima necessária, ou omita só se precisar de tudo>
   model: haiku   # ou sonnet/opus/inherit
   ---
   Prompt/instruções do subagente.
   ```
3. Teste mencionando o agente explicitamente no pedido antes de confiar no roteamento automático por `description`.

Documentação oficial de subagentes: https://code.claude.com/docs/en/sub-agents
