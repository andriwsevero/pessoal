# Domínio: Trabalho

Este projeto é o espaço de agentes de **trabalho** do usuário. Tudo aqui dentro é isolado do domínio pessoal (pasta `personal/`, em outro projeto) — nunca misture ou faça referência a informações pessoais do usuário aqui.

Delegue pedidos ao subagente especializado mais adequado em `.claude/agents/` sempre que a tarefa combinar com a `description` de um deles.

## Como adicionar um novo agente de trabalho

1. Crie um arquivo em `.claude/agents/<nome>.md` com frontmatter:
   ```yaml
   ---
   name: nome-do-agente
   description: Frase clara do que faz e QUANDO usar (é isso que decide a delegação automática).
   model: haiku   # ou sonnet/opus/inherit, dependendo da complexidade da tarefa
   ---
   Prompt/instruções do subagente aqui.
   ```
2. Rode `claude` dentro desta pasta (`work/`) e peça algo que combine com a `description` — ou mencione o agente explicitamente no pedido pra testar a delegação.
