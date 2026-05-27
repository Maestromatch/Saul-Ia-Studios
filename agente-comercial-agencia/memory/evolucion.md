# Evolucion de la agencia

> Bitacora estrategica para registrar como evoluciona Saul IA Studios con cada aprendizaje.

## 2026-05-19 - Memoria para integracion de repos

Creado el sistema base de memoria en `memory/` para integrar repos de GitHub como habilidades, recursos y decisiones operativas.

Decisiones:
- Los repos no se guardan solo como links; se convierten en capacidades reutilizables.
- Cada integracion debe dejar claro que mejora: venta, entrega, automatizacion, demo, stack, CRM o SOP.
- La memoria principal vive en cuatro archivos: `repos-github.md`, `habilidades.md`, `evolucion.md` y `reference_tips_iastudio.md`.

Pendiente:
- Recibir primer repo de GitHub del usuario.
- Analizar estructura, licencia, stack y valor real para la agencia.
- Integrar los aprendizajes utiles en recursos concretos.

## 2026-05-19 - Memoria aplicada al proyecto IAStudio

Entrada nueva:
- Carpeta `memory/` ya creada con protocolos de memoria, UI/UX, repos y aprendizaje progresivo.

Que cambia en la agencia:
- `CLAUDE.md` ahora apunta a `memory/observations-index.md` como primera lectura.
- `modelo-operativo-agencia-v1.md` incorpora memoria progresiva y verificacion por evidencia.
- `manual-creador-servicios-saul-v1.md` exige revisar memoria/design-system antes de trabajos importantes.
- `roadmap-agencia-30-dias.md` registra la memoria como base operacional.
- Se crea `protocolo-memoria-y-verificacion-agencia.md` como documento rector.

Decision:
- El proyecto ya no debe evolucionar solo por conversacion; cada cambio importante debe dejar evidencia, checklist o aprendizaje reusable.

Pendiente:
- Probar este protocolo en el proximo cambio de landing, workflow, servicio o prospeccion.

## 2026-05-19 - Integracion de obra/superpowers

Entrada nueva:
- Repo: https://github.com/obra/superpowers
- Tema: framework de skills y metodologia de desarrollo agentico.

Que cambia en la agencia:
- IAStudio gana un protocolo operativo para trabajar con agentes: diagnosticar, especificar, planificar, ejecutar, revisar y verificar.
- La entrega tecnica deja de depender solo de intuicion; ahora cada pieza importante debe tener criterio de exito y evidencia.
- La memoria de repos no solo guarda herramientas, tambien convierte metodologias externas en SOPs internos.

Habilidad nueva:
- Protocolo Superpowers IAStudio.
- Planes ejecutables para agentes.
- Verificacion antes de cierre.
- Escritura de skills internas.

Recurso creado o actualizado:
- `memory/superpowers-iastudio.md`
- `memory/repos-github.md`
- `memory/habilidades.md`
- `memory/evolucion.md`

Prueba pendiente:
- Usarlo en el proximo cambio tecnico: landing, bot, workflow n8n, CRM, demo o plantilla de cliente.

Decision tomada:
- No instalar ni clonar automaticamente el repo por ahora. Se adopta primero como metodologia local y se evaluara instalacion del plugin si el flujo demuestra valor.

## 2026-05-19 - Integracion de affaan-m/ECC

Entrada nueva:
- Repo: https://github.com/affaan-m/ECC
- Tema: sistema operativo agentico para skills, memoria, seguridad, research-first, hooks, MCP configs y verificacion.

Que cambia en la agencia:
- IAStudio gana una capa de operaciones para trabajar con muchos repos y convertirlos en capacidades sin saturar la memoria.
- Se adopta el principio "search-first": antes de construir, decidir si conviene adoptar, extender, componer o crear desde cero.
- El aprendizaje queda separado por scope: cliente/proyecto vs global de agencia.
- Seguridad y verificacion pasan a ser parte del cierre de entrega, especialmente cuando haya WhatsApp, Supabase, n8n, APIs o datos de clientes.

Habilidad nueva:
- Research-first antes de construir.
- Aprendizaje continuo por proyecto.
- Security review para entregas IA.
- Gestion de contexto y compactacion.
- Verification loop de produccion ligera.

Recurso creado o actualizado:
- `memory/ecc-iastudio.md`
- `memory/repos-github.md`
- `memory/habilidades.md`
- `memory/evolucion.md`

Prueba pendiente:
- Usar el modelo ECC para clasificar el siguiente repo como adoptar / extender / componer / construir.
- Crear una skill interna IAStudio con formato propio y scope definido.

Decision tomada:
- No instalar ECC completo por ahora. Se adopta selectivamente por su tamano y porque instalar hooks/globales sin una necesidad concreta podria meter ruido operativo.

## 2026-05-19 - Integracion de nextlevelbuilder/ui-ux-pro-max-skill

Entrada nueva:
- Repo: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- Tema: skill de inteligencia UI/UX con design system generator, patrones, paletas, tipografias, reglas por industria, stacks y checklist.

Que cambia en la agencia:
- IAStudio gana una fuente visual base para que landings, demos y dashboards salgan con coherencia profesional.
- El diseno deja de ser solo estetica: ahora se conecta con conversion, confianza, accesibilidad, responsive y entrega verificable.
- Se adopta el patron `MASTER.md` + overrides por pagina para mantener consistencia sin rigidizar cada cliente.

Habilidad nueva:
- Design system IAStudio.
- Patron landing de conversion con confianza.
- Checklist UI/UX antes de entregar.
- Dashboard CRM visualmente vendible.

Recurso creado o actualizado:
- `memory/ui-ux-pro-max-iastudio.md`
- `design-system/MASTER.md`
- `design-system/pages/landing-agencia.md`
- `design-system/pages/demo-nicho.md`
- `design-system/pages/dashboard-crm.md`
- `memory/repos-github.md`
- `memory/habilidades.md`
- `memory/evolucion.md`

Prueba pendiente:
- Auditar `index.html` y `demo-opticas.html` contra el checklist visual.
- En la proxima mejora frontend, validar responsive en 375px, 768px, 1024px y 1440px.

Decision tomada:
- No instalar `uipro-cli` por ahora. La skill ya existe localmente como catalogo, y se integra primero como sistema visual/documental para no sumar dependencia ni archivos generados sin necesidad.

## 2026-05-19 - Integracion de thedotmack/claude-mem

Entrada nueva:
- Repo: https://github.com/thedotmack/claude-mem
- Tema: memoria persistente, compresion de contexto, hooks, busqueda progresiva, observaciones con IDs y privacidad.

Que cambia en la agencia:
- IAStudio gana un modelo de memoria por capas: indice primero, timeline despues y detalle solo cuando hace falta.
- La memoria deja de ser solo documentos largos; ahora tambien tiene IDs recuperables y costo mental bajo.
- Se incorpora una politica explicita para no guardar secretos, datos sensibles ni contexto temporal innecesario.

Habilidad nueva:
- Memoria progresiva con IDs.
- Politica anti-secretos en memoria.
- Recuperacion de contexto por capas.
- Contexto por carpeta sin ruido.

Recurso creado o actualizado:
- `memory/claude-mem-iastudio.md`
- `memory/observations-index.md`
- `memory/repos-github.md`
- `memory/habilidades.md`
- `memory/evolucion.md`
- `memory/README.md`

Prueba pendiente:
- Usar `observations-index.md` como primera capa con el proximo repo.
- Mantener cada entrada nueva con ID, tipo, scope, fuente y archivo de detalle.

Decision tomada:
- No instalar `claude-mem` completo por ahora. Se adopta su arquitectura como memoria manual/progresiva porque la instalacion completa activa hooks, worker local, base SQLite y captura automatica de sesiones.

## 2026-05-19 - Integracion de czlonkowski/n8n-mcp

Entrada nueva:
- Repo: https://github.com/czlonkowski/n8n-mcp
- Tema: MCP server para que agentes puedan buscar documentacion de n8n, usar templates, validar nodos/workflows y gestionar instancias n8n via API.

Que cambia en la agencia:
- IAStudio gana un protocolo mas serio para construir automatizaciones n8n sin depender solo de prueba/error visual.
- Los workflows ahora deben partir desde templates o documentacion de nodos, configurar parametros explicitos y pasar validaciones antes de entrega.
- Se refuerza una regla critica: no editar produccion directo con IA.

Habilidad nueva:
- n8n workflow builder con MCP.
- Validacion multinivel de automatizaciones.
- Seguridad MCP para n8n.

Recurso creado o actualizado:
- `memory/n8n-mcp-iastudio.md`
- `memory/repos-github.md`
- `memory/habilidades.md`
- `memory/evolucion.md`
- `memory/observations-index.md`
- `stack-tecnico.md`

Prueba pendiente:
- Aplicar este protocolo al workflow lead capturado -> alerta -> CRM -> follow-up.
- Evaluar conexion MCP en modo solo documentacion antes de usar `N8N_API_KEY`.

Decision tomada:
- No instalar ni conectar `n8n-mcp` todavia. Primero se adopta como SOP seguro; la conexion real requiere decidir ambiente, API key, permisos, backups y si se desactiva telemetria.

## 2026-05-19 - Integracion de nexu-io/open-design

Entrada nueva:
- Repo: https://github.com/nexu-io/open-design
- Tema: plataforma local-first para producir artefactos visuales con agentes, skills, design systems, preview sandbox y export.

Que cambia en la agencia:
- IAStudio gana un pipeline de produccion visual completo, no solo criterios de UI.
- El diseno pasa a tener preflight: brief interactivo, direccion visual, `DESIGN.md`, skill adecuada y autocritica 5D antes de entregar.
- El design system se formaliza en formato portable compatible con Open Design.

Habilidad nueva:
- Pipeline Open Design para artefactos visuales.
- `DESIGN.md` portable para IAStudio.
- Critica visual de 5 dimensiones.
- Skills visuales componibles.

Recurso creado o actualizado:
- `memory/open-design-iastudio.md`
- `design-system/DESIGN.md`
- `design-system/critique-rubric.md`
- `memory/repos-github.md`
- `memory/habilidades.md`
- `memory/evolucion.md`
- `memory/observations-index.md`

Prueba pendiente:
- Usar este pipeline en una landing/demo/deck real.
- Auditar una pieza actual con la rubrica 5D.

Decision tomada:
- No instalar Open Design por ahora. Se adopta como metodologia y formato porque el stack completo requiere Node 24/pnpm o Docker, crea `.od/`, ejecuta agentes locales y maneja persistencia/credenciales.

## 2026-05-20 - Integracion de gridaco/grida

Entrada nueva:
- Repo: https://github.com/gridaco/grida
- Tema: canvas editor/rendering engine, headless Figma rendering, Database/CMS y Forms con Supabase.

Que cambia en la agencia:
- IAStudio gana un radar tecnico para transformar disenos y datos en artefactos exportables y sistemas de captura.
- Grida no reemplaza el flujo actual, pero abre opciones futuras para Figma -> assets, formularios avanzados y prototipos conectados a Supabase.
- Se refuerza la idea de prototipo data-first: primero datos, formulario y estados; despues UI compleja.

Habilidad nueva:
- Figma render/export pipeline.
- Formularios data-first con Supabase.
- Prototipos data-first.

Recurso creado o actualizado:
- `memory/grida-iastudio.md`
- `memory/repos-github.md`
- `memory/habilidades.md`
- `memory/evolucion.md`
- `memory/observations-index.md`

Prueba pendiente:
- Evaluar `@grida/refig` cuando exista necesidad real de exportar assets desde Figma.
- Comparar Grida Forms vs HTML + Supabase para lead capture avanzado.

Decision tomada:
- No instalar Grida por ahora. Se registra como radar tecnico porque el monorepo es grande, requiere Node 22+/pnpm 10+ y el Canvas SDK aun esta en alpha.

## 2026-05-20 - Integracion de NeverSight/learn-skills.dev

Entrada nueva:
- Repo: https://github.com/NeverSight/learn-skills.dev
- Tema: catalogo/crawler de AI Agent Skills con rankings, cache de `SKILL.md`, feed JSON/RSS y busqueda web.

Que cambia en la agencia:
- IAStudio gana radar de skills: antes de crear o instalar habilidades, puede buscar si existe una skill madura.
- La memoria de repos deja de ser solo reactiva a links del usuario; ahora puede tener watchlist por categorias.
- Se incorpora una forma de evaluar skills por popularidad, tendencia, fuente, rutas estandar y costo de contexto.

Habilidad nueva:
- Radar de skills para IAStudio.
- Evaluacion de skills antes de instalar.
- Feed de aprendizaje continuo de skills.

Recurso creado o actualizado:
- `memory/learn-skills-iastudio.md`
- `memory/skill-radar-watchlist.md`
- `memory/repos-github.md`
- `memory/habilidades.md`
- `memory/evolucion.md`
- `memory/observations-index.md`

Prueba pendiente:
- Usar el radar antes de crear la primera skill interna `landing-demo-nicho`.
- Evaluar 3 skills candidatas con el checklist.

Decision tomada:
- No instalar ni correr el crawler ahora. Se adopta como metodologia porque correrlo requiere Bun, red, fuentes externas y posiblemente `GITHUB_TOKEN`.

## 2026-05-20 - Integracion de guia TodoDeIA Claude Code Setup

Entrada nueva:
- Fuente: https://www.tododeia.com/community/claude-code-setup
- Verificacion: repo oficial `anthropics/claude-plugins-official`, plugin `claude-code-setup`, skill `claude-automation-recommender`.

Que cambia en la agencia:
- IAStudio gana un protocolo de checkup read-only para proyectos Claude Code.
- Las automatizaciones se separan en cinco categorias: Hooks, Skills, MCP servers, Subagents y Slash commands.
- Se refuerza la regla de aplicar poco y con criterio: diagnosticar primero, instalar despues.

Habilidad nueva:
- Auditoria Claude Code Setup.
- Matriz de automatizaciones Claude Code.

Recurso creado o actualizado:
- `memory/claude-code-setup-iastudio.md`
- `memory/fuentes-web.md`
- `memory/habilidades.md`
- `memory/evolucion.md`
- `memory/observations-index.md`
- `memory/README.md`

Prueba pendiente:
- Correr el prompt read-only en Claude Code contra `IAStudio_Lanzamiento` cuando se use ese entorno.
- Elegir maximo 1-2 automatizaciones para aplicar primero.

Decision tomada:
- No instalar el plugin desde este chat. Se integra como protocolo porque requiere Claude Code 2.x y decision del usuario sobre que recomendaciones aplicar.

## 2026-05-20 - Integracion de nolly-studio/cult-ui

Entrada nueva:
- Repo: https://github.com/nolly-studio/cult-ui
- Tema: registry de componentes React/shadcn motion-rich, AI UI patterns, docs de instalacion y shadcn MCP.

Que cambia en la agencia:
- IAStudio gana un banco selectivo de componentes para que landings, demos y dashboards no salgan genericos.
- Se adopta la idea de copy-source: usar piezas concretas, adaptarlas al sistema visual propio y asumir mantenimiento.
- Se suma criterio de performance de movimiento antes de entregar interfaces animadas.

Habilidad nueva:
- Banco Cult UI para landings y demos.
- Componentes componibles con components-build.
- Revision de motion performance.
- Shadcn registry y MCP para UI.

Recurso creado o actualizado:
- `memory/cult-ui-iastudio.md`
- `memory/repos-github.md`
- `memory/habilidades.md`
- `memory/evolucion.md`
- `memory/observations-index.md`
- `design-system/MASTER.md`
- `design-system/DESIGN.md`

Prueba pendiente:
- Probar 1-3 componentes Cult UI en una demo de nicho o landing, validando responsive, focus y performance.
- Evaluar shadcn MCP solo si el proyecto usa React/shadcn y tiene `components.json`.

Decision tomada:
- No instalar componentes ni configurar registry automaticamente. Se integra como banco de patrones y protocolo de adopcion segura para evitar dependencia visual o motion innecesario.

## 2026-05-21 - Integracion de msitarzewski/agency-agents

Entrada nueva:
- Repo: https://github.com/msitarzewski/agency-agents
- Tema: biblioteca de agentes especialistas para engineering, design, sales, marketing, product, testing, support, finance y specialized.
- Pedido del usuario: que los agentes se auto-invoquen al realizar o modificar proyectos, todos los que se puedan.

Que cambia en la agencia:
- IAStudio gana un router de auto-invocacion por fase, riesgo y tipo de proyecto.
- Crear o modificar proyectos deja de ser una sola accion: ahora dispara especialistas de alcance, workflow, arquitectura, UX, seguridad, QA, ventas y handoff cuando apliquen.
- Se adopta "todos los que puedan aportar", no "todos por volumen".

Habilidad nueva:
- Router IAStudio de auto-invocacion de agentes.
- Orquestacion PM Workflow Build QA Reality.
- Prospeccion por senales y propuestas especializadas.
- Reality checking con evidencia.

Recurso creado o actualizado:
- `memory/agency-agents-iastudio.md`
- `memory/repos-github.md`
- `memory/habilidades.md`
- `memory/evolucion.md`
- `memory/observations-index.md`
- `memory/README.md`
- `CLAUDE.md`

Prueba pendiente:
- Usar este router en la proxima modificacion real de proyecto.
- Activar subagentes reales solo cuando el entorno lo permita y el scope sea paralelizable.

Decision tomada:
- No instalar el roster completo. Se adopta primero como protocolo central porque instalar cientos de agentes puede saturar contexto y configuraciones locales.

## 2026-05-21 - Integracion de prompt local Agente Web Premium

Entrada nueva:
- Fuente local: `C:\Users\Usuario 01\Documents\Downloads\prompt-agente-web-premium.txt`
- Tema: prompt system para propuestas web premium, estandar visual, proceso de brief, prohibiciones, performance, accesibilidad y autocritica.

Que cambia en la agencia:
- IAStudio gana un quality gate premium para landing pages, product sites, demos y propuestas web.
- El design-system ahora tiene una vara mas alta para piezas comerciales importantes.
- Se formaliza el proceso diagnostico -> tesis visual -> wireframe -> implementacion -> autocritica.

Habilidad nueva:
- Quality gate web premium.
- Tesis visual antes de implementar.
- Autocritica premium de propuesta web.

Recurso creado o actualizado:
- `memory/prompt-agente-web-premium-iastudio.md`
- `memory/fuentes-internas.md`
- `memory/habilidades.md`
- `memory/evolucion.md`
- `memory/observations-index.md`
- `memory/README.md`
- `design-system/MASTER.md`
- `design-system/DESIGN.md`
- `CLAUDE.md`

Prueba pendiente:
- Aplicar el quality gate en la proxima mejora de `index.html`, demo por nicho o propuesta web premium.

Decision tomada:
- No copiar el prompt literal como regla absoluta. Se adapta a IAStudio porque cuando el usuario ya pide implementar, el agente debe avanzar y solo preguntar si falta informacion critica.

## 2026-05-21 - Integracion de AgriciDaniel/claude-seo

Entrada nueva:
- Repo: https://github.com/AgriciDaniel/claude-seo
- Tema: skill suite SEO para Claude Code con auditoria tecnica, contenido, E-E-A-T, schema, GEO/AEO, local SEO, mapas, Google APIs, backlinks, drift y reportes.

Que cambia en la agencia:
- IAStudio gana una capa SEO/GEO para todas las paginas publicas.
- Las landings dejan de medirse solo por visual y conversion; ahora tambien por indexabilidad, rendimiento, schema, citabilidad IA y SEO local.
- Se conecta diseno premium con busqueda: mejor landing + mejor estructura + mejor evidencia.

Habilidad nueva:
- Auditoria SEO/GEO IAStudio.
- SEO local para pymes.
- Schema y datos estructurados.
- SEO drift monitoring.

Recurso creado o actualizado:
- `memory/claude-seo-iastudio.md`
- `memory/repos-github.md`
- `memory/habilidades.md`
- `memory/evolucion.md`
- `memory/observations-index.md`
- `memory/README.md`
- `design-system/DESIGN.md`
- `CLAUDE.md`

Prueba pendiente:
- Aplicar auditoria SEO/GEO a la landing principal o a una demo publicada.
- Evaluar `AgriciDaniel/codex-seo` si se quiere instalacion nativa para Codex.

Decision tomada:
- No instalar Claude SEO desde este chat. Primero se adopta como protocolo porque la instalacion requiere scripts, Python, potenciales credenciales Google/DataForSEO/Firecrawl y decision de entorno.

## 2026-05-22 - Integracion de remotion-dev/skills

Entrada nueva:
- Repo: https://github.com/remotion-dev/skills
- Tema: skill de buenas practicas Remotion para video programatico con React.

Que cambia en la agencia:
- IAStudio gana un protocolo para producir videos reproducibles desde codigo.
- Los demos, reportes, ads y explicadores pueden transformarse en plantillas parametrizables por nicho/cliente.
- Se refuerza que motion para video no se hace con CSS transitions sino con frames, composiciones y QA de render.

Habilidad nueva:
- Video programatico con Remotion.
- Plantillas de video parametrizables.
- Captions y voiceover sincronizados.
- QA de render motion.

Recurso creado o actualizado:
- `memory/remotion-skills-iastudio.md`
- `memory/repos-github.md`
- `memory/habilidades.md`
- `memory/evolucion.md`
- `memory/observations-index.md`
- `memory/README.md`
- `CLAUDE.md`

Prueba pendiente:
- Crear un clip vertical corto para una oferta IAStudio o una demo por nicho.
- Si se implementa, usar Remotion Studio y render still de control antes del render final.

Decision tomada:
- No instalar Remotion ni crear proyecto ahora. Se adopta como protocolo y se activara cuando haya necesidad real de video programatico.

## 2026-05-22 - Registro de carpeta Google Drive pendiente

Entrada nueva:
- Fuente: https://drive.google.com/drive/folders/1PoxECZTHbmA0B6Rndwve_JWQSmzJJiC6?usp=drive_link
- Tipo: carpeta Google Drive externa.

Que cambia en la agencia:
- IAStudio gana un protocolo para recibir carpetas Drive sin asumir que el contenido ya fue leido.
- Se separa `link recibido` de `contenido integrado`.
- Queda trazabilidad para retomar cuando haya acceso real.

Habilidad nueva:
- Ingesta segura de carpetas Drive.

Recurso creado o actualizado:
- `memory/google-drive-folder-iastudio.md`
- `memory/fuentes-drive.md`
- `memory/README.md`
- `memory/habilidades.md`
- `memory/evolucion.md`
- `memory/observations-index.md`

Prueba pendiente:
- Habilitar acceso publico, compartir ZIP local o enviar archivos individuales.
- Reprocesar la fuente cuando el contenido sea legible.

Decision tomada:
- No marcar como integrado. El enlace no lista contenido desde acceso web directo, por lo que queda como pendiente.

## Plantilla diaria de evolucion

Fecha:

Entrada nueva:

Que cambia en la agencia:
-

Habilidad nueva:
-

Recurso creado o actualizado:
-

Prueba pendiente:
-

Decision tomada:
-
