# Claude Code Setup IAStudio

> Adaptacion de la guia TodoDeIA sobre `claude-code-setup` y del plugin oficial de Anthropic para Saul IA Studios.

Fuente principal:
- https://www.tododeia.com/community/claude-code-setup

Fuentes verificadas:
- https://github.com/anthropics/claude-plugins-official
- https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-code-setup
- `plugins/claude-code-setup/skills/claude-automation-recommender/SKILL.md`

## Que es

`claude-code-setup` es un plugin oficial de Anthropic para Claude Code. Su skill principal, `claude-automation-recommender`, analiza un codebase en modo read-only y recomienda automatizaciones Claude Code adaptadas al proyecto.

Categorias que revisa:
- Hooks.
- Skills.
- MCP servers.
- Subagents.
- Slash commands.

La idea central:
- No instala nada.
- No modifica archivos.
- Recomienda top 1-2 por categoria.
- Explica por que aplica a ese stack.
- El usuario decide que aplicar.

## Valor para IAStudio

IAStudio ya esta acumulando memoria, skills y protocolos. Esta herramienta agrega una capa de diagnostico de setup para cada proyecto:

- Detectar automatizaciones utiles antes de construir.
- Evitar instalar demasiadas cosas por ansiedad.
- Separar "recomendacion" de "aplicacion".
- Proteger archivos sensibles con hooks.
- Recomendar MCPs segun stack real.
- Recomendar skills/subagents sin contaminar el flujo principal.

## Flujo recomendado

### 1. Abrir el proyecto correcto

Antes de correr el analisis:
- Confirmar carpeta correcta.
- Revisar que Claude Code vea el root del proyecto.
- En CLI, usar `pwd` o pedir que liste archivos root.

### 2. Instalar plugin si se usa Claude Code

Comando recomendado dentro de Claude Code:

```text
/plugin install claude-code-setup@claude-plugins-official
```

Fallback si marketplace oficial no aparece:

```text
/plugin marketplace add anthropics/claude-plugins-official
```

Luego:

```text
/reload-plugins
```

Verificar:
- `/plugin`
- Installed -> `claude-code-setup` Enabled.
- Errors vacio.

### 3. Prompt IAStudio recomendado

Usar este prompt read-only:

```text
Activa la skill claude-automation-recommender y haz un analisis completo de este proyecto.

Quiero el siguiente formato de salida:
1. RESUMEN DEL PROYECTO
   - Tipo de proyecto y framework principal.
   - Stack tecnologico detectado.
   - Archivos clave revisados.

2. RECOMENDACIONES
   Top 1-2 por categoria:
   - Hooks
   - Skills
   - MCP servers
   - Subagents
   - Slash commands

Para cada recomendacion inclui:
   - Nombre.
   - Que hace en una linea.
   - Por que sirve especificamente en este proyecto.
   - Comando exacto, path o snippet.
   - Setup adicional requerido: API keys, permisos, cuenta paga, riesgo.

3. CATEGORIAS NO APLICABLES
   Marcarlas como no aplica y explicar por que.

4. ORDEN SUGERIDO
   Aplicar maximo 1-2 primero.

Importante: no apliques nada. Solo recomienda.
```

## Mapa de categorias para IAStudio

### Hooks

Uso:
- Auto-format.
- Auto-lint.
- Typecheck.
- Bloquear `.env`, secretos, lockfiles o archivos sensibles.

Regla IAStudio:
- Hooks de proteccion primero; hooks de productividad despues.

### Skills

Uso:
- Frontend design.
- Plan agent.
- Documentos.
- Project conventions.
- Nuevas skills internas: `landing-demo-nicho`, `auditoria-whatsapp-express`, `workflow-n8n-lead-followup`.

Regla IAStudio:
- Instalar o crear skills solo si una tarea se repite.

### MCP servers

Uso:
- Context7 para docs actuales.
- Playwright/browser para QA visual.
- Supabase MCP para proyectos con DB.
- GitHub MCP para issues/PRs.
- n8n-MCP para workflows.

Regla IAStudio:
- MCP con credenciales solo despues de seguridad, scope y backup.

### Subagents

Uso:
- Security reviewer.
- Performance reviewer.
- Accessibility/UI reviewer.
- API/documentation reviewer.

Regla IAStudio:
- Usar cuando haya entrega real, riesgo o proyecto grande.

### Slash commands

Uso:
- `/test`
- `/pr-review`
- `/explain`
- `/qa-landing`
- `/audit-secrets`
- `/handoff-cliente`

Regla IAStudio:
- Crear slash command solo para flujos repetidos semanalmente.

## Trampas y limites

- Requiere Claude Code 2.x.
- No aplica al chat web normal.
- No es lista exhaustiva del ecosistema.
- No auto-instala nada.
- En repos grandes puede trabarse; limitar a subdirectorio.
- Algunas recomendaciones requieren API keys, planes pagos o permisos.
- Aunque sea oficial, cada plugin/MCP recomendado debe evaluarse antes de instalar.

## Como se combina con nuestra memoria

- `learn-skills-iastudio`: buscar skills externas.
- `n8n-mcp-iastudio`: validar workflows n8n.
- `claude-mem-iastudio`: registrar recomendaciones con IDs.
- `ecc-iastudio`: evaluar scope, seguridad y contexto.
- `superpowers-iastudio`: convertir recomendacion en plan verificable antes de aplicar.

## Que gana IAStudio

IAStudio gana un checkup de automatizacion por proyecto. Antes de llenar un proyecto con plugins o MCPs, podemos pedir un diagnostico read-only, priorizar 1-2 mejoras de alto impacto y aplicar una por una con control.
