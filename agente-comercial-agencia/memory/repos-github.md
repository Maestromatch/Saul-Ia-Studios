# Repositorios GitHub para integrar

> Registro de repos que el usuario entrega para convertirlos en recursos de Saul IA Studios.

## Estado

12 repos registrados e integrados como metodologia operativa.

## Tabla maestra

| Fecha | Repo | Tema | Estado | Integracion propuesta | Pendiente |
| --- | --- | --- | --- | --- | --- |
| 2026-05-19 | https://github.com/obra/superpowers | Framework de skills y metodologia de desarrollo agentico | Integrado en memoria | Adaptar como protocolo IAStudio: diagnostico, plan, ejecucion, TDD cuando aplique, revision y verificacion con evidencia | Probarlo en el proximo cambio tecnico o entrega de cliente |
| 2026-05-19 | https://github.com/affaan-m/ECC | Sistema operativo para agentes: skills, hooks, memoria, seguridad, research-first y MCP configs | Integrado en memoria | Adoptar selectivamente como capa de operaciones: busqueda antes de construir, aprendizaje continuo, seguridad, verificacion y gestion de contexto | Convertir 1 skill IAStudio propia usando este modelo |
| 2026-05-19 | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill | Skill de inteligencia UI/UX, design systems, patrones, paletas, tipografias y checklist | Integrado en memoria + design-system | Adoptar como protocolo de diseno para landing, demos, dashboards y propuestas visuales | Auditar `index.html` y `demo-opticas.html` contra el checklist |
| 2026-05-19 | https://github.com/thedotmack/claude-mem | Memoria persistente, compresion de contexto, busqueda por capas y privacidad | Integrado en memoria | Adoptar memoria progresiva manual: indice, timeline, detalle bajo demanda y politica anti-secretos | Probar `observations-index.md` con el proximo repo |
| 2026-05-19 | https://github.com/czlonkowski/n8n-mcp | MCP server para documentar, crear, validar y gestionar workflows n8n | Integrado en memoria + stack | Adoptar como protocolo de construccion n8n: templates primero, validacion multinivel, parametros explicitos y seguridad por ambiente | Probarlo en Track B o workflow lead-alerta-seguimiento |
| 2026-05-19 | https://github.com/nexu-io/open-design | Plataforma local-first para producir artefactos visuales con skills, design systems y preview sandbox | Integrado en memoria + design-system | Adoptar como pipeline de produccion visual: brief interactivo, DESIGN.md, artefacto, self-critique y export | Probar con una landing/demo nueva o deck comercial |
| 2026-05-20 | https://github.com/gridaco/grida | Canvas editor/rendering engine + Database/CMS + Forms con Supabase | Integrado en memoria | Adoptar como radar tecnico: Figma export/rendering, forms data-first, Supabase CMS y canvas para prototipos | Evaluar `@grida/refig` para export de assets y Grida Forms para lead capture |
| 2026-05-20 | https://github.com/NeverSight/learn-skills.dev | Catalogo/crawler de AI Agent Skills con rankings, feed, cache de SKILL.md y busqueda web | Integrado en memoria | Adoptar como radar de skills: descubrir, comparar, cachear y priorizar habilidades antes de instalar o crear | Usar watchlist en proxima busqueda de skill |
| 2026-05-20 | https://github.com/nolly-studio/cult-ui | Registry de componentes React/shadcn motion-rich para design engineers | Integrado en memoria + design-system | Adoptar como banco selectivo de componentes para landings, demos, dashboards y artefactos IA | Probar 1-3 componentes en una demo, validando motion/performance |
| 2026-05-21 | https://github.com/msitarzewski/agency-agents | Biblioteca de agentes especialistas por division: engineering, design, sales, marketing, testing, support y specialized | Integrado en memoria | Adoptar como router IAStudio de auto-invocacion por fase, riesgo y tipo de proyecto | Probarlo en la proxima modificacion real de landing, workflow o propuesta |
| 2026-05-21 | https://github.com/AgriciDaniel/claude-seo | Skill suite SEO para Claude Code: technical SEO, E-E-A-T, schema, GEO, local SEO, maps, Google APIs y reportes | Integrado en memoria | Adoptar como protocolo IAStudio de auditoria SEO/GEO para landing, demos, clientes locales y reportes | Evaluar `AgriciDaniel/codex-seo` si se instala algo en Codex |
| 2026-05-22 | https://github.com/remotion-dev/skills | Skill oficial/interna de Remotion para video programatico con React y reglas por dominio | Integrado en memoria | Adoptar como protocolo IAStudio para videos demo, ads, reportes animados y plantillas parametrizables | Probar en un clip vertical de oferta o demo por nicho |

## Plantilla de analisis

### Repo

- URL:
- Fecha de lectura:
- Stack:
- Tipo: app / automatizacion / prompt / agente / landing / CRM / datos / otro
- Licencia:
- Valor para la agencia:
- Riesgos o dependencias:
- Archivos clave:
- Habilidades extraidas:
- Recursos a integrar:
- Proxima accion:

### obra/superpowers

- URL: https://github.com/obra/superpowers
- Fecha de lectura: 2026-05-19
- Stack: skills Markdown, scripts Shell/JavaScript/Python/TypeScript, plugin para multiples agentes.
- Tipo: framework de skills / metodologia de trabajo agentico.
- Licencia: MIT.
- Valor para la agencia: convierte trabajo con agentes en un proceso repetible: brainstorm, especificacion, plan, ejecucion, pruebas, review y cierre con evidencia.
- Riesgos o dependencias: su version completa depende de instalar el plugin en el entorno; en esta memoria se integra como metodologia local sin copiar automatismos ni asumir instalacion.
- Archivos clave:
  - `README.md`: vision, instalacion, workflow base y filosofia.
  - `.codex-plugin/plugin.json`: metadata para Codex, version 5.1.0 y capacidades.
  - `skills/`: biblioteca de habilidades operativas.
  - `skills/brainstorming/SKILL.md`: convertir ideas en disenos y specs.
  - `skills/writing-plans/SKILL.md`: planes ejecutables con tareas pequenas y verificables.
  - `skills/test-driven-development/SKILL.md`: ciclo RED-GREEN-REFACTOR.
  - `skills/verification-before-completion/SKILL.md`: evidencia antes de afirmar que algo esta listo.
- Habilidades extraidas:
  - Protocolo de diagnostico antes de construir.
  - Planes de implementacion con pasos concretos, comandos y criterios de exito.
  - Verificacion obligatoria antes de prometer entrega.
  - Revision temprana por cumplimiento de spec y calidad.
  - Creacion de skills propias reutilizables.
- Recursos integrados:
  - `memory/superpowers-iastudio.md`
  - `memory/habilidades.md`
  - `memory/evolucion.md`
- Proxima accion: usar el protocolo en el proximo repo, landing, bot, workflow n8n o entrega de cliente.

### affaan-m/ECC

- URL: https://github.com/affaan-m/ECC
- Fecha de lectura: 2026-05-19
- Stack: TypeScript/JavaScript, Python, Shell, Markdown, MCP configs, hooks, skills, rules, agents y comandos.
- Tipo: agent operating system / harness performance optimization system.
- Licencia: MIT.
- Valor para la agencia: aporta una capa de operaciones para agentes: research-first, memoria persistente por proyecto, seguridad, verificacion, catalogo de skills, reglas, comandos y optimizacion de contexto.
- Riesgos o dependencias: es grande y puede sobrecargar contexto o instalar hooks globales si se adopta completo. Para IAStudio se integra de forma selectiva, no como instalacion total.
- Archivos clave:
  - `README.md`: vision, quick start, versiones y catalogo general.
  - `.codex-plugin/plugin.json`: metadata Codex, version `2.0.0-rc.1`, skills y MCP configs.
  - `package.json`: paquete `ecc-universal`, instaladores, scripts, catalogo de skills y validaciones.
  - `skills/search-first/SKILL.md`: investigar antes de construir.
  - `skills/continuous-learning-v2/SKILL.md`: aprendizaje por instintos, scope por proyecto y confianza.
  - `skills/security-review/SKILL.md`: checklist de seguridad para secretos, input, SQL, auth, XSS, CSRF, rate limiting y dependencias.
  - `skills/verification-loop/SKILL.md`: build, types, lint, tests, security scan y diff review.
  - `skills/strategic-compact/SKILL.md`: compactacion estrategica y optimizacion de contexto.
- Habilidades extraidas:
  - Search-first: adoptar/extender/construir despues de investigar.
  - Memoria por proyecto con aprendizaje promovible a global.
  - Security review antes de desplegar recursos con datos, APIs o credenciales.
  - Verification loop como reporte de preparacion.
  - Context budget: cargar solo lo necesario y compactar al cambiar de fase.
- Recursos integrados:
  - `memory/ecc-iastudio.md`
  - `memory/habilidades.md`
  - `memory/evolucion.md`
- Proxima accion: aplicar ECC en el siguiente repo buscando primero si conviene adoptar, envolver o transformar en recurso propio.

### nextlevelbuilder/ui-ux-pro-max-skill

- URL: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- Fecha de lectura: 2026-05-19
- Stack: Python, Markdown, CSV data, CLI npm, templates por plataforma.
- Tipo: AI skill / design system generator / biblioteca UI/UX.
- Licencia: MIT.
- Valor para la agencia: transforma diseno de landings, demos y dashboards en un proceso repetible con patrones, paletas, tipografia, accesibilidad, anti-patrones y checklist antes de entregar.
- Riesgos o dependencias: instalar la CLI completa (`uipro-cli`) requiere red y puede agregar archivos generados. Para IAStudio se adopta primero como memoria y design-system local.
- Archivos clave:
  - `README.md`: vision, features, instalacion, uso y flujo de generacion.
  - `skill.json`: version `2.5.0`, descripcion, plataformas soportadas y licencia.
  - `src/ui-ux-pro-max/data/`: datasets de estilos, colores, tipografias, landing, productos, charts y UX guidelines.
  - `src/ui-ux-pro-max/scripts/search.py`: busqueda/generacion de recomendaciones.
  - `src/ui-ux-pro-max/scripts/design_system.py`: generacion de design systems.
- Habilidades extraidas:
  - Generar sistema visual por tipo de producto/industria.
  - Usar `MASTER.md` + overrides por pagina como fuente de verdad visual.
  - Elegir patron de landing segun objetivo: conversion, confianza, demo interactiva o social proof.
  - Aplicar checklist UI/UX antes de entregar: responsive, contraste, foco, hover, motion y anti-patrones.
  - Recomendaciones para dashboards de ventas/CRM y monitoreo.
- Recursos integrados:
  - `memory/ui-ux-pro-max-iastudio.md`
  - `design-system/MASTER.md`
  - `design-system/pages/landing-agencia.md`
  - `design-system/pages/demo-nicho.md`
  - `design-system/pages/dashboard-crm.md`
- Proxima accion: usarlo en la proxima mejora visual de landing o demo y registrar captura/prueba responsive.

### thedotmack/claude-mem

- URL: https://github.com/thedotmack/claude-mem
- Fecha de lectura: 2026-05-19
- Stack: TypeScript, Node.js 20+, Bun, Express, React, SQLite/FTS5, Chroma opcional, MCP tools, hooks.
- Tipo: memoria persistente / compresion de contexto / plugin de productividad agentica.
- Licencia: Apache-2.0.
- Valor para la agencia: aporta un modelo de memoria persistente con observaciones resumidas, busqueda por capas, IDs citables, control de privacidad y recuperacion selectiva de contexto.
- Riesgos o dependencias: la instalacion completa usa hooks, worker local, base SQLite, Bun, uv y posible indexacion de sesiones. No se instala por ahora para evitar guardar contenido sensible o sumar servicios de fondo sin decision explicita.
- Archivos clave:
  - `README.md`: quick start, features, arquitectura, search tools, requisitos y configuracion.
  - `.codex-plugin/plugin.json`: version `13.2.0`, skills, MCP, hooks e interfaz Codex.
  - `package.json`: paquete `claude-mem` version `13.2.0`, Apache-2.0, bin CLI y scripts worker/test.
  - `docs/architecture/overview`: hooks, worker, SQLite/FTS5, Chroma opcional, viewer UI y flujo de datos.
  - `docs/progressive-disclosure`: filosofia de indice primero y detalle bajo demanda.
  - `docs/usage/private-tags`: uso de `<private>` para no persistir contenido sensible.
  - `docs/usage/search-tools`: workflow search -> timeline -> get_observations.
  - `docs/usage/folder-context`: contexto por carpeta con `CLAUDE.md`, desactivado por defecto.
- Habilidades extraidas:
  - Memoria progresiva: indice primero, timeline despues, detalle solo si hace falta.
  - Observaciones con IDs citables.
  - Politica de privacidad para secretos, datos de clientes y prompts exploratorios.
  - Separar memoria viva de resumen estable.
  - Contexto por carpeta como opcion futura, no automatica.
- Recursos integrados:
  - `memory/claude-mem-iastudio.md`
  - `memory/observations-index.md`
  - `memory/habilidades.md`
  - `memory/evolucion.md`
- Proxima accion: usar `observations-index.md` como primera lectura antes de abrir archivos largos de memoria.

### czlonkowski/n8n-mcp

- URL: https://github.com/czlonkowski/n8n-mcp
- Fecha de lectura: 2026-05-19
- Stack: TypeScript, JavaScript, Node.js, MCP SDK, Express, sql.js/better-sqlite3, Docker, n8n packages.
- Tipo: MCP server / n8n workflow builder / documentation and validation layer.
- Licencia: MIT.
- Version revisada: `2.54.0`.
- Valor para la agencia: convierte n8n en un sistema construible con IA de forma mas segura: busqueda de templates, documentacion de nodos, ejemplos reales, validacion de nodos, validacion de workflow y gestion opcional via API.
- Riesgos o dependencias: con `N8N_API_KEY` el MCP tiene permisos equivalentes a la API de n8n configurada. No se debe apuntar directo a produccion sin copia, backup, ambiente de prueba y validacion.
- Archivos clave:
  - `README.md`: vision, capacidades, reglas de uso, workflow process y herramientas MCP.
  - `package.json`: paquete `n8n-mcp` version `2.54.0`, bin `n8n-mcp`, scripts y dependencias.
  - `docs/CODEX_SETUP.md`: configuracion para Codex en modo documentacion o modo completo con API n8n.
  - `docs/N8N_DEPLOYMENT.md`: despliegue local, Docker, HTTP mode, auth tokens, `/mcp` endpoint y buenas practicas.
  - `docs/SECURITY_HARDENING.md`: limites de seguridad, `AUTH_TOKEN`, `DISABLED_TOOLS`, SSRF gate y prompt injection awareness.
  - `PRIVACY.md`: telemetria anonima y opt-out con `N8N_MCP_TELEMETRY_DISABLED=true`.
- Habilidades extraidas:
  - Templates first: buscar plantillas antes de crear desde cero.
  - Never trust defaults: configurar explicitamente parametros que controlan comportamiento.
  - Validacion multinivel: `validate_node` minimal, `validate_node` full runtime, `validate_workflow`, validacion post-deploy.
  - No produccion directo: copiar workflow, probar en desarrollo, exportar backup y recien desplegar.
  - Operacion MCP segura: modo documentacion sin API key para diseno, modo gestion solo cuando haya necesidad y credenciales controladas.
  - Preferir nodos estandar antes que Code node.
- Recursos integrados:
  - `memory/n8n-mcp-iastudio.md`
  - `memory/habilidades.md`
  - `memory/evolucion.md`
  - `memory/observations-index.md`
  - `stack-tecnico.md`
- Proxima accion: usar el protocolo para el siguiente workflow n8n: lead capturado -> alerta -> CRM -> follow-up.

### nexu-io/open-design

- URL: https://github.com/nexu-io/open-design
- Fecha de lectura: 2026-05-19
- Stack: Next.js, React, TypeScript, Node 24, Express daemon, SQLite, pnpm, Electron opcional, Docker, agent CLI adapters.
- Tipo: local-first design studio / artifact generator / skill runtime.
- Licencia: Apache-2.0.
- Version destacada: `0.8.0-preview`.
- Valor para la agencia: convierte diseno en una cadena operativa: brief interactivo, seleccion de direccion visual, `DESIGN.md` portable, skill especializada, preview sandbox, autocritica 5D y export de artefactos.
- Riesgos o dependencias: pesado para instalar en esta etapa; requiere Node 24/pnpm o Docker, crea datos en `.od/`, puede guardar proyectos/credenciales BYOK y ejecuta agentes locales. No se instala por ahora.
- Archivos clave:
  - `README.md`: vision, arquitectura, skills, design systems, BYOK, preview sandbox y export.
  - `QUICKSTART.md`: requisitos Node 24, pnpm 10.33.x, Docker y `pnpm tools-dev`.
  - `PRIVACY.md`: referencias de privacidad.
  - `docs/skills-protocol.md`: protocolo de skills con `SKILL.md`, `od:` frontmatter, modos, inputs, parametros, outputs y `DESIGN.md`.
  - `skills/web-prototype/SKILL.md`: prototipo web con template y layout library.
  - `skills/critique/SKILL.md`: revision de 5 dimensiones: filosofia, jerarquia, detalle, funcionalidad, innovacion.
- Habilidades extraidas:
  - Brief interactivo antes de disenar para evitar redirecciones caras.
  - `DESIGN.md` portable de 9 secciones como fuente de verdad visual.
  - Skills visuales con inputs, parametros, preview y outputs.
  - Preview/export mental model: HTML, PDF, PPTX, ZIP, Markdown segun artefacto.
  - Autocritica 5D antes de entregar una landing, demo, dashboard o deck.
  - Craft references: reglas universales separadas de marca.
- Recursos integrados:
  - `memory/open-design-iastudio.md`
  - `design-system/DESIGN.md`
  - `design-system/critique-rubric.md`
  - `memory/habilidades.md`
  - `memory/evolucion.md`
  - `memory/observations-index.md`
- Proxima accion: aplicar pipeline OD a una pieza visual concreta: landing de agencia, demo nicho, dashboard CRM o deck comercial.

### gridaco/grida

- URL: https://github.com/gridaco/grida
- Fecha de lectura: 2026-05-20
- Stack: TypeScript, React, Next.js, Rust, Skia, WASM, FlatBuffers, Supabase, pnpm monorepo.
- Tipo: open-source canvas editor/rendering engine + Database/CMS + Forms.
- Licencia: Apache-2.0.
- Valor para la agencia: aporta infraestructura para tres problemas futuros: exportar/renderear disenos tipo Figma sin navegador, construir formularios/lead capture mas potentes que Google Forms, y prototipar experiencias data-first conectadas a Supabase.
- Riesgos o dependencias: monorepo grande, requiere Node.js 22+ y pnpm 10+, el Canvas SDK esta en alpha y varias partes son base de plataforma mas que producto listo para cliente pequeno.
- Archivos clave:
  - `README.md`: vision, canvas, Grida Forms, Database/CMS, quickstart y paquetes.
  - `package.json`: scripts de monorepo, `pnpm`, tareas de dev/test/lint/typecheck.
  - `format/grida.fbs`: formato `.grida` con FlatBuffers.
  - `packages/`: paquetes reutilizables como `@grida/refig`, `@grida/canvas-wasm`, primitives de canvas.
  - `supabase/`: integracion de Database/CMS y Forms con Supabase.
  - Docs `@grida/refig`: renderer headless Figma -> PNG/JPEG/WebP/PDF/SVG.
- Habilidades extraidas:
  - Render/export de disenos Figma sin depender de navegador.
  - Radar para formularios avanzados: file upload, signature, hidden fields, logic blocks, partial submissions, Supabase sync.
  - Data-first prototype: formularios + database + CMS antes de construir app completa.
  - Separar artefacto visual de asset exportable para venta, ads y entregables.
  - No adoptar SDK alpha en proyectos pagados sin prueba aislada.
- Recursos integrados:
  - `memory/grida-iastudio.md`
  - `memory/habilidades.md`
  - `memory/evolucion.md`
  - `memory/observations-index.md`
- Proxima accion: probar mentalmente Grida Forms para un flujo de lead capture y `@grida/refig` para exportar assets desde Figma cuando haya diseno fuente.

### NeverSight/learn-skills.dev

- URL: https://github.com/NeverSight/learn-skills.dev
- Fecha de lectura: 2026-05-20
- Stack: TypeScript, Bun, Python scripts, GitHub Actions, JSON feeds, cached Markdown.
- Tipo: catalogo/crawler de AI Agent Skills / skill search web app.
- Licencia: no detectada claramente en lectura rapida del repo; verificar antes de reutilizar codigo.
- Valor para la agencia: convierte el descubrimiento de skills en un sistema: rankings, trending/hot, feed RSS/JSON, cache de `SKILL.md`, rutas estandar de skills y manual skills persistentes.
- Riesgos o dependencias: depende de fuentes externas como `skills.sh`, GitHub raw/API y posiblemente rate limits. El crawler puede requerir `GITHUB_TOKEN`; no guardar tokens en memoria ni repo.
- Archivos clave:
  - `README.md`: proposito, fuentes, outputs, uso local, GitHub Actions y formatos de datos.
  - `data/manual_skills.json`: registro manual de skills no rastreadas por proveedores.
  - `data/skills.json`: leaderboards all-time, trending y hot.
  - `data/skills_index.json`: indice web-friendly con `skillMdPath`.
  - `data/feed.json` y `data/feed.xml`: feed simplificado/RSS.
  - `data/skills-md/`: cache de `SKILL.md` desde rutas comunes.
  - `scripts/`: builders, sync, traducciones, notificaciones y registro manual.
- Habilidades extraidas:
  - Radar de skills: buscar antes de crear una skill propia.
  - Ranking por all-time/trending/hot para separar popularidad estable de novedad.
  - Cache local de `SKILL.md` y descripcion para evaluacion offline.
  - Manual skills persistentes para recursos que el crawler no encuentra.
  - Rutas estandar para buscar skills: `skills/<skill>/SKILL.md`, `.claude/skills/`, `.cursor/skills/`, `.codex/skills/`, `plugins/*/skills/`.
  - Feed RSS/JSON para monitorear nuevas skills sin revisar GitHub manualmente.
- Recursos integrados:
  - `memory/learn-skills-iastudio.md`
  - `memory/skill-radar-watchlist.md`
  - `memory/habilidades.md`
  - `memory/evolucion.md`
  - `memory/observations-index.md`
- Proxima accion: antes de crear una skill interna, buscar si ya existe una skill madura que se pueda adoptar, extender o referenciar.

### nolly-studio/cult-ui

- URL: https://github.com/nolly-studio/cult-ui
- Fecha de lectura: 2026-05-20
- Stack: TypeScript, React, Next.js, Tailwind CSS, shadcn/ui registry, Motion, pnpm, Turborepo.
- Tipo: component registry / design engineering / AI UI patterns.
- Licencia: MIT.
- Valor para la agencia: aporta una biblioteca de componentes visuales listos para copiar/adaptar en landings, demos, dashboards y experiencias con agentes sin depender de una libreria cerrada.
- Riesgos o dependencias: no debe pegarse por novedad visual; cada componente copy-source queda bajo mantenimiento propio. Algunas piezas requieren Tailwind/shadcn/motion y deben pasar revision responsive/performance.
- Archivos clave:
  - `README.md`: vision del proyecto, AI SDK Agents, blocks, templates y links.
  - `apps/www/registry/default/`: registry de componentes, blocks y examples.
  - `apps/www/content/docs/`: documentacion MDX.
  - `.agents/skills/components-build/SKILL.md`: especificacion para componentes componibles, accesibles y tipados.
  - `.claude/skills/fixing-motion-performance/SKILL.md`: reglas para revisar motion y evitar jank.
  - Docs `installation`: configuracion de registry `@cult-ui`.
  - Docs `mcp-server`: uso del shadcn MCP para buscar/instalar desde registries.
- Habilidades extraidas:
  - Banco Cult UI para landings y demos.
  - Componentes componibles con `components-build`.
  - Revision de motion performance.
  - Shadcn registry/MCP como canal controlado de adopcion.
- Recursos integrados:
  - `memory/cult-ui-iastudio.md`
  - `memory/repos-github.md`
  - `memory/habilidades.md`
  - `memory/evolucion.md`
  - `memory/observations-index.md`
  - `design-system/MASTER.md`
  - `design-system/DESIGN.md`
- Proxima accion: probar 1-3 piezas Cult UI en una demo de nicho o landing, manteniendo tokens IAStudio y validando responsive/performance.

### msitarzewski/agency-agents

- URL: https://github.com/msitarzewski/agency-agents
- Fecha de lectura: 2026-05-21
- Stack: Markdown agent files, Bash scripts, conversion/install tooling, multi-tool integrations.
- Tipo: biblioteca de agentes / agencia de especialistas / roles operativos.
- Licencia: MIT.
- Valor para la agencia: convierte tareas complejas en un sistema de especialistas con identidad, mision, workflows, entregables y metricas. Permite que IAStudio auto-invoque roles por fase: plan, workflow, diseno, implementacion, QA, seguridad, venta y handoff.
- Riesgos o dependencias: instalar todos los agentes puede saturar herramientas y contexto. Para IAStudio se adopta primero como matriz de auto-invocacion, no como copia masiva.
- Archivos clave:
  - `README.md`: roster completo, quick start, divisiones y opciones de instalacion.
  - `scripts/install.sh`: instala agentes en herramientas como Claude Code, Copilot, Gemini CLI, OpenCode, Cursor, Aider, Windsurf, Qwen y Kimi.
  - `scripts/convert.sh`: genera integraciones para varias herramientas.
  - `specialized/agents-orchestrator.md`: orquestador PM -> arquitectura -> dev/QA -> reality check.
  - `specialized/specialized-workflow-architect.md`: workflow specs con happy path, fallos, estados, handoffs y recuperacion.
  - `testing/testing-reality-checker.md`: certificacion con evidencia y `NEEDS WORK` por defecto.
  - `sales/sales-outbound-strategist.md`: prospeccion por senales y secuencias multi-canal.
  - `sales/sales-proposal-strategist.md`: propuestas como narrativa de decision.
- Habilidades extraidas:
  - Router IAStudio de auto-invocacion de agentes.
  - Orquestacion PM -> Workflow -> Build -> QA -> Reality.
  - Prospeccion y propuestas por especialistas.
  - Reality checking con evidencia antes de cierre.
- Recursos integrados:
  - `memory/agency-agents-iastudio.md`
  - `memory/repos-github.md`
  - `memory/habilidades.md`
  - `memory/evolucion.md`
  - `memory/observations-index.md`
  - `CLAUDE.md`
- Proxima accion: aplicar el router en la proxima modificacion de proyecto; activar todos los agentes que apliquen por fase y riesgo.

### AgriciDaniel/claude-seo

- URL: https://github.com/AgriciDaniel/claude-seo
- Fecha de lectura: 2026-05-21
- Stack: Claude Code skills, Markdown agents, Python scripts, Google APIs, Playwright opcional, MCP extensions.
- Tipo: SEO skill suite / auditoria tecnica / GEO-AEO / SEO local / reporting.
- Licencia: MIT.
- Valor para la agencia: convierte cada landing o sitio cliente en un activo auditable: SEO tecnico, Core Web Vitals, schema, contenido, local SEO, mapas, GEO para busqueda con IA, drift monitoring y reportes.
- Riesgos o dependencias: instalar implica scripts, dependencias Python y posibles credenciales Google/DataForSEO/Firecrawl. Para IAStudio se adopta primero como protocolo; si se instala, revisar antes `AgriciDaniel/codex-seo`.
- Archivos clave:
  - `README.md`: vision, comandos, features, limitaciones, requisitos y ecosistema.
  - `skills/seo/SKILL.md`: orquestador, routing, scoring, subskills, subagents y quality gates.
  - `AGENTS.md`: instrucciones multi-plataforma y arquitectura resumida.
  - `CLAUDE.md`: reglas de arquitectura, seguridad, scripts y reportes.
  - `docs/ARCHITECTURE.md`: flujo de auditoria con subagentes paralelos.
  - `skills/seo-local/SKILL.md`: SEO local, GBP, NAP, reviews, citations, LocalBusiness schema.
  - `schema/templates.json`: snippets JSON-LD.
  - `scripts/`: fetch, parse, PageSpeed, GSC, GA4, CrUX, drift, reportes.
- Habilidades extraidas:
  - Auditoria SEO/GEO IAStudio.
  - SEO local para pymes.
  - Schema y datos estructurados.
  - Core Web Vitals como gate de entrega.
  - SEO drift monitoring.
  - Reporte SEO accionable para cliente.
- Recursos integrados:
  - `memory/claude-seo-iastudio.md`
  - `memory/repos-github.md`
  - `memory/habilidades.md`
  - `memory/evolucion.md`
  - `memory/observations-index.md`
  - `memory/README.md`
  - `design-system/DESIGN.md`
  - `CLAUDE.md`
- Proxima accion: aplicar el protocolo en la proxima landing/demo publica y registrar baseline SEO antes/despues de cambios.

### remotion-dev/skills

- URL: https://github.com/remotion-dev/skills
- Fecha de lectura: 2026-05-22
- Stack: TypeScript, React, Remotion 4, `@remotion/*` packages, rules Markdown.
- Tipo: agent skill / video programatico / React motion.
- Licencia: no detectada en lectura rapida; verificar antes de reutilizar codigo textual.
- Valor para la agencia: aporta un protocolo profesional para crear videos reproducibles desde codigo: demos, anuncios, reportes animados, clips verticales y assets parametrizables por cliente/nicho.
- Riesgos o dependencias: el paquete se declara interno y sin documentacion publica completa. No se instala automaticamente. Renderizar videos requiere proyecto Remotion, dependencias, assets licenciados y revision de performance.
- Archivos clave:
  - `README.md`: indica paquete interno sin documentacion publica.
  - `skills/remotion/SKILL.md`: buenas practicas de Remotion.
  - `skills/remotion/rules/`: reglas por dominio: audio, captions, timing, transitions, parameters, videos, voiceover, 3D, Lottie, maps, FFmpeg, Tailwind, fonts.
  - `package.json`: paquete privado `@remotion/skills`, version `4.0.457`, dependencias Remotion 4.
- Habilidades extraidas:
  - Video programatico con Remotion.
  - Plantillas de video parametrizables.
  - Captions y voiceover sincronizados.
  - Motion por frames y QA de render.
  - Dashboard-to-video para reportes.
- Recursos integrados:
  - `memory/remotion-skills-iastudio.md`
  - `memory/repos-github.md`
  - `memory/habilidades.md`
  - `memory/evolucion.md`
  - `memory/observations-index.md`
  - `memory/README.md`
  - `CLAUDE.md`
- Proxima accion: probar el protocolo con un video corto de 15-30 segundos para una oferta IAStudio o demo por nicho.
