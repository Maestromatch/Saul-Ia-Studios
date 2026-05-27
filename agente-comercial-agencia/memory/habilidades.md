# Memoria de habilidades

> Capacidades acumuladas del agente para operar, vender y entregar servicios de Saul IA Studios.

## Habilidades base actuales

### Comercial

- Definir ICP por nicho y descartar prospectos no ideales.
- Personalizar mensajes de prospeccion por dolor real, no por "IA".
- Manejar objeciones con foco en negocio, tiempo, respuesta y ventas perdidas.
- Usar mini-servicios como entrada cuando el prospecto no esta listo para un paquete grande.
- Registrar aprendizaje diario en CRM y learning log.

### Oferta y packaging

- Convertir tecnologia en paquetes vendibles: Pack IA Express, Formaliza Tu Negocio, Pack Emprendedor 360 y Setup Identidad Meta Legal.
- Separar oferta piloto, mini-servicio y servicio premium.
- Mantener precio fundador con anticipo y entrega acotada.

### Entrega

- Armar landing, bot basico, CRM simple y automatizacion de captura/seguimiento.
- Usar plantillas de cliente para onboarding, construccion, entrega y testimonio.
- Crear demos por nicho antes de vender implementaciones completas.

### Operacion tecnica

- Trabajar con Vercel, GitHub, Supabase, n8n, WhatsApp y formularios/landings simples.
- Documentar stack, costos, credenciales requeridas y pruebas antes de produccion.
- Evitar guardar secretos o datos sensibles en el repositorio.

## Habilidades a incorporar desde repos

Cada repo nuevo debe agregar una entrada con este formato:

### Nombre de habilidad

- Fuente:
- Problema que resuelve:
- Como se aplica en Saul IA Studios:
- Archivos o plantillas relacionadas:
- Nivel: idea / probado / operativo / empaquetado
- Proxima prueba:

### Protocolo Superpowers IAStudio

- Fuente: https://github.com/obra/superpowers
- Problema que resuelve: evita que el agente salte directo a construir, entregue cosas a medias o declare exito sin evidencia.
- Como se aplica en Saul IA Studios: antes de crear recursos importantes, convertir la idea en mini-spec, plan ejecutable, tareas verificables, pruebas/revision y cierre con evidencia.
- Archivos o plantillas relacionadas: `memory/superpowers-iastudio.md`, `clientes/_PLANTILLA-CLIENTE/`, SOPs de entrega, demos HTML, workflows n8n.
- Nivel: operativo en memoria, pendiente de prueba en proyecto real.
- Proxima prueba: aplicarlo al siguiente recurso tecnico de cliente o integracion de repo.

### Planes ejecutables para agentes

- Fuente: `skills/writing-plans/SKILL.md` de `obra/superpowers`.
- Problema que resuelve: planes vagos que el agente interpreta de mas o ejecuta de forma desordenada.
- Como se aplica en Saul IA Studios: cada implementacion relevante debe tener objetivo, archivos exactos, pasos pequenos, comando de verificacion y criterio de terminado.
- Archivos o plantillas relacionadas: `memory/superpowers-iastudio.md`.
- Nivel: operativo.
- Proxima prueba: crear un plan para actualizar una demo o bot antes de tocar codigo.

### Verificacion antes de cierre

- Fuente: `skills/verification-before-completion/SKILL.md` de `obra/superpowers`.
- Problema que resuelve: declarar una landing, bot, workflow o propuesta como lista sin haberla probado.
- Como se aplica en Saul IA Studios: no se entrega ni se informa "listo" sin evidencia fresca: build, prueba manual, test de casos, captura, CRM o checklist.
- Archivos o plantillas relacionadas: SOPs de entrega, `clientes/_PLANTILLA-CLIENTE/03-entrega/`.
- Nivel: operativo.
- Proxima prueba: agregar evidencia de prueba en la proxima entrega real.

### Escritura de skills internas

- Fuente: `skills/writing-skills/SKILL.md` y biblioteca `skills/` de `obra/superpowers`.
- Problema que resuelve: conocimiento disperso en tips, conversaciones o repos que no se vuelve una capacidad reusable.
- Como se aplica en Saul IA Studios: convertir aprendizajes repetibles en habilidades internas con disparador, pasos, salida esperada y archivo fuente.
- Archivos o plantillas relacionadas: `memory/habilidades.md`, `memory/evolucion.md`, `agente-comercial-agencia/06-prompt-maestro.md`.
- Nivel: idea avanzada.
- Proxima prueba: crear una skill interna para "auditoria WhatsApp Express" o "setup identidad Meta legal".

### Research-first antes de construir

- Fuente: `skills/search-first/SKILL.md` de `affaan-m/ECC`.
- Problema que resuelve: reinventar funciones, flujos o herramientas que ya existen en repos, paquetes, MCPs o skills.
- Como se aplica en Saul IA Studios: antes de crear codigo, automatizacion o recurso complejo, buscar si conviene adoptar, extender, componer o construir.
- Archivos o plantillas relacionadas: `memory/ecc-iastudio.md`, `memory/repos-github.md`.
- Nivel: operativo.
- Proxima prueba: usarlo con el siguiente repo que entregue el usuario.

### Aprendizaje continuo por proyecto

- Fuente: `skills/continuous-learning-v2/SKILL.md` de `affaan-m/ECC`.
- Problema que resuelve: mezclar aprendizajes de proyectos distintos o perder patrones utiles tras cada sesion.
- Como se aplica en Saul IA Studios: registrar patrones por proyecto/cliente y promover a global solo cuando se repitan en mas de un caso.
- Archivos o plantillas relacionadas: `memory/evolucion.md`, `memory/habilidades.md`, carpetas `clientes/`.
- Nivel: operativo manual.
- Proxima prueba: etiquetar cada aprendizaje nuevo como `proyecto`, `cliente` o `global`.

### Security review para entregas IA

- Fuente: `skills/security-review/SKILL.md` de `affaan-m/ECC`.
- Problema que resuelve: riesgos por secretos hardcodeados, inputs sin validar, logs sensibles, APIs abiertas o dependencias inseguras.
- Como se aplica en Saul IA Studios: revisar landings con formularios, bots, Supabase, n8n, WhatsApp, Vercel y APIs antes de entregar.
- Archivos o plantillas relacionadas: `stack-tecnico.md`, SOPs de entrega, `memory/ecc-iastudio.md`.
- Nivel: operativo.
- Proxima prueba: agregar checklist de seguridad a la proxima entrega con datos o API.

### Gestion de contexto y compactacion

- Fuente: `skills/strategic-compact/SKILL.md` de `affaan-m/ECC`.
- Problema que resuelve: sesiones largas donde el agente pierde foco por exceso de contexto.
- Como se aplica en Saul IA Studios: guardar hallazgos en memoria al cerrar fase de investigacion, plan o entrega; luego continuar desde el resumen limpio.
- Archivos o plantillas relacionadas: `memory/ecc-iastudio.md`, `CLAUDE.md`, `memory/evolucion.md`.
- Nivel: operativo.
- Proxima prueba: despues de 3-4 repos, consolidar aprendizajes y limpiar duplicados.

### Verification loop de produccion ligera

- Fuente: `skills/verification-loop/SKILL.md` de `affaan-m/ECC`.
- Problema que resuelve: entregar sin build, lint, prueba visual, security scan o diff review.
- Como se aplica en Saul IA Studios: checklist de cierre por tipo de recurso: landing, bot, workflow n8n, CRM, propuesta o documento.
- Archivos o plantillas relacionadas: `memory/ecc-iastudio.md`, `clientes/_PLANTILLA-CLIENTE/03-entrega/`.
- Nivel: operativo.
- Proxima prueba: crear reporte de verificacion en la proxima entrega.

### Design system IAStudio

- Fuente: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
- Problema que resuelve: crear landings y demos visualmente inconsistentes, demasiado genericas o sin checklist UI/UX.
- Como se aplica en Saul IA Studios: usar `design-system/MASTER.md` como fuente base y overrides por pagina para landing, demos de nicho y dashboards CRM.
- Archivos o plantillas relacionadas: `design-system/MASTER.md`, `design-system/pages/`, `memory/ui-ux-pro-max-iastudio.md`.
- Nivel: operativo.
- Proxima prueba: auditar landing actual con checklist UI/UX.

### Patron landing de conversion con confianza

- Fuente: `ui-ux-pro-max-skill` landing patterns y reasoning rules.
- Problema que resuelve: landings que se ven bonitas pero no explican el problema, no reducen riesgo y no llevan a WhatsApp.
- Como se aplica en Saul IA Studios: combinar patron `Conversion-Optimized`, `Trust & Authority` e `Interactive Product Demo` segun el servicio.
- Archivos o plantillas relacionadas: `design-system/pages/landing-agencia.md`, `design-system/pages/demo-nicho.md`.
- Nivel: operativo.
- Proxima prueba: revisar `index.html` y demo constructora contra esta estructura.

### Checklist UI/UX antes de entregar

- Fuente: `ui-ux-pro-max-skill` pre-delivery checklist.
- Problema que resuelve: entregar interfaces con falta de contraste, botones sin hover, foco invisible, mala version movil o elementos que se sienten improvisados.
- Como se aplica en Saul IA Studios: antes de entregar landing/demo/dashboard, revisar contraste, responsive 375/768/1024/1440, foco, hover, CTAs, placeholders y legibilidad.
- Archivos o plantillas relacionadas: `design-system/MASTER.md`, SOPs de entrega, `clientes/_PLANTILLA-CLIENTE/03-entrega/`.
- Nivel: operativo.
- Proxima prueba: agregar checklist UI/UX al cierre de la proxima landing.

### Dashboard CRM visualmente vendible

- Fuente: `ui-ux-pro-max-skill` BI/Analytics dashboard styles.
- Problema que resuelve: CRMs o paneles internos que funcionan pero no comunican valor al cliente.
- Como se aplica en Saul IA Studios: usar estilo `Sales Intelligence Dashboard` o `Real-Time Monitoring` para mostrar leads, estados, respuesta, seguimiento y oportunidades recuperadas.
- Archivos o plantillas relacionadas: `design-system/pages/dashboard-crm.md`.
- Nivel: idea operativa.
- Proxima prueba: crear mockup o dashboard simple para el sistema de captacion.

### Memoria progresiva con IDs

- Fuente: https://github.com/thedotmack/claude-mem
- Problema que resuelve: cargar demasiada memoria antigua y perder foco en sesiones largas.
- Como se aplica en Saul IA Studios: usar `memory/observations-index.md` como capa 1, luego abrir el recurso detallado solo si el ID es relevante.
- Archivos o plantillas relacionadas: `memory/claude-mem-iastudio.md`, `memory/observations-index.md`.
- Nivel: operativo manual.
- Proxima prueba: registrar el siguiente repo nuevo con ID y usar el indice antes del detalle.

### Politica anti-secretos en memoria

- Fuente: `docs/usage/private-tags` de `thedotmack/claude-mem`.
- Problema que resuelve: que tokens, datos de clientes, logs sensibles o informacion temporal queden guardados en memoria persistente.
- Como se aplica en Saul IA Studios: no registrar secretos en `memory/`; marcar como privado o resumir sin valores sensibles cuando haya API keys, telefonos personales, credenciales, logs o datos de cliente.
- Archivos o plantillas relacionadas: `memory/claude-mem-iastudio.md`, `stack-tecnico.md`.
- Nivel: operativo.
- Proxima prueba: aplicar al proximo workflow con APIs, Supabase, n8n o WhatsApp.

### Recuperacion de contexto por capas

- Fuente: `docs/usage/search-tools` y `docs/progressive-disclosure` de `thedotmack/claude-mem`.
- Problema que resuelve: leer todo antes de saber que importa.
- Como se aplica en Saul IA Studios: capa 1 `observations-index`, capa 2 timeline en `evolucion.md`, capa 3 archivo especifico con detalle.
- Archivos o plantillas relacionadas: `memory/observations-index.md`, `memory/evolucion.md`, `memory/repos-github.md`.
- Nivel: operativo.
- Proxima prueba: en la proxima sesion, empezar revisando IDs recientes y solo abrir detalles necesarios.

### Contexto por carpeta sin ruido

- Fuente: `docs/usage/folder-context` de `thedotmack/claude-mem`.
- Problema que resuelve: carpetas grandes sin contexto local o con notas generadas que ensucian Git.
- Como se aplica en Saul IA Studios: mantener instrucciones manuales por carpetas clave cuando aporte, pero no generar `CLAUDE.md` automaticos dentro de subcarpetas por ahora.
- Archivos o plantillas relacionadas: `memory/claude-mem-iastudio.md`, `clientes/_PLANTILLA-CLIENTE/`.
- Nivel: criterio operativo.
- Proxima prueba: crear nota manual de contexto solo cuando una carpeta de cliente crezca demasiado.

### n8n workflow builder con MCP

- Fuente: https://github.com/czlonkowski/n8n-mcp
- Problema que resuelve: crear workflows n8n por intuicion, con nodos mal configurados, defaults rotos o sin validacion.
- Como se aplica en Saul IA Studios: usar protocolo templates first, documentacion de nodos, ejemplos reales, parametros explicitos y validacion antes de entregar.
- Archivos o plantillas relacionadas: `memory/n8n-mcp-iastudio.md`, `stack-tecnico.md`, SOPs de entrega y carpetas `clientes/`.
- Nivel: operativo manual, pendiente de conectar MCP.
- Proxima prueba: disenar workflow lead-alerta-CRM-follow-up usando este protocolo.

### Validacion multinivel de automatizaciones

- Fuente: `README.md` de `czlonkowski/n8n-mcp`.
- Problema que resuelve: workflows que parecen correctos visualmente pero fallan al ejecutar por campos, conexiones o expresiones.
- Como se aplica en Saul IA Studios: validar nodo rapido, validar nodo completo con perfil runtime, validar workflow, luego validar deployment y revisar ejecuciones.
- Archivos o plantillas relacionadas: `memory/n8n-mcp-iastudio.md`, `clientes/_PLANTILLA-CLIENTE/03-entrega/`.
- Nivel: operativo.
- Proxima prueba: agregar checklist n8n a una entrega real.

### Seguridad MCP para n8n

- Fuente: `docs/SECURITY_HARDENING.md` de `czlonkowski/n8n-mcp`.
- Problema que resuelve: exponer una API key de n8n con permisos amplios o permitir que IA modifique produccion sin control.
- Como se aplica en Saul IA Studios: usar modo documentacion sin API cuando se pueda; si se usa API, usar ambiente de desarrollo, backup, tokens fuertes, herramientas limitadas y revision humana.
- Archivos o plantillas relacionadas: `memory/n8n-mcp-iastudio.md`, `stack-tecnico.md`, `memory/claude-mem-iastudio.md`.
- Nivel: operativo.
- Proxima prueba: definir config segura antes de conectar n8n-MCP real.

### Pipeline Open Design para artefactos visuales

- Fuente: https://github.com/nexu-io/open-design
- Problema que resuelve: pedir "hazme una landing/deck/demo" y dejar que el agente improvise tono, estructura, sistema visual y criterio de calidad.
- Como se aplica en Saul IA Studios: antes de crear una pieza visual importante, usar brief interactivo, `DESIGN.md`, skill/tipo de artefacto, preview mental y autocritica 5D.
- Archivos o plantillas relacionadas: `memory/open-design-iastudio.md`, `design-system/DESIGN.md`, `design-system/critique-rubric.md`.
- Nivel: operativo documental, pendiente de prueba en artefacto real.
- Proxima prueba: usarlo para una demo nueva o deck comercial.

### DESIGN.md portable para IAStudio

- Fuente: `docs/skills-protocol.md` de `nexu-io/open-design`.
- Problema que resuelve: design systems mezclados entre reglas sueltas, CSS y preferencias no estructuradas.
- Como se aplica en Saul IA Studios: mantener `design-system/DESIGN.md` con 9 secciones: tema, color, tipografia, componentes, layout, profundidad, do/don't, responsive y guia para agente.
- Archivos o plantillas relacionadas: `design-system/DESIGN.md`, `design-system/MASTER.md`.
- Nivel: operativo.
- Proxima prueba: usar `DESIGN.md` como preflight antes de modificar `index.html`.

### Critica visual de 5 dimensiones

- Fuente: `skills/critique/SKILL.md` de `nexu-io/open-design`.
- Problema que resuelve: aprobar interfaces solo porque "se ven bien" sin revisar filosofia, jerarquia, detalle, funcionalidad e innovacion.
- Como se aplica en Saul IA Studios: antes de cerrar landing/demo/dashboard/deck, puntuar 5 dimensiones con evidencia y separar Keep / Fix / Quick wins.
- Archivos o plantillas relacionadas: `design-system/critique-rubric.md`, SOPs de entrega.
- Nivel: operativo.
- Proxima prueba: auditar `index.html` y `demo-opticas.html` con la rubrica.

### Skills visuales componibles

- Fuente: `docs/skills-protocol.md` y `skills/` de `nexu-io/open-design`.
- Problema que resuelve: cada pieza visual se crea desde cero aunque haya tipos repetibles.
- Como se aplica en Saul IA Studios: modelar futuras piezas como skills: landing nicho, demo WhatsApp, dashboard CRM, pricing page, deck comercial, e-guide y social carousel.
- Archivos o plantillas relacionadas: `memory/open-design-iastudio.md`, `design-system/pages/`.
- Nivel: idea avanzada.
- Proxima prueba: definir la primera skill interna `landing-demo-nicho`.

### Figma render/export pipeline

- Fuente: https://github.com/gridaco/grida y docs `@grida/refig`.
- Problema que resuelve: depender de capturas manuales o exports inconsistentes cuando hay disenos Figma.
- Como se aplica en Saul IA Studios: evaluar `@grida/refig` para renderizar `.fig` o JSON REST a PNG/JPEG/WebP/PDF/SVG en entregas, thumbnails, propuestas y assets.
- Archivos o plantillas relacionadas: `memory/grida-iastudio.md`, `design-system/`.
- Nivel: radar tecnico.
- Proxima prueba: usarlo solo cuando exista archivo `.fig` o necesidad real de export automatizado.

### Formularios data-first con Supabase

- Fuente: Grida Forms + Database/CMS.
- Problema que resuelve: formularios simples que no soportan logica, uploads, firmas, campos ocultos, submissions parciales o conexion real a base de datos.
- Como se aplica en Saul IA Studios: considerar Grida Forms para lead capture avanzado cuando Google Forms/HTML estatico se quede corto.
- Archivos o plantillas relacionadas: `memory/grida-iastudio.md`, `stack-tecnico.md`, SOPs de entrega.
- Nivel: radar tecnico.
- Proxima prueba: comparar Grida Forms vs formulario HTML + Supabase en un caso de lead capture.

### Prototipos data-first

- Fuente: Grida vision "data-first prototyping tool" y Supabase integration.
- Problema que resuelve: construir dashboards/apps completas antes de validar estructura de datos y flujo de captura.
- Como se aplica en Saul IA Studios: para clientes con datos, empezar por tabla, formulario, vistas y CMS antes de UI compleja.
- Archivos o plantillas relacionadas: `memory/grida-iastudio.md`, `design-system/pages/dashboard-crm.md`.
- Nivel: criterio operativo.
- Proxima prueba: usar en un CRM simple de leads.

### Radar de skills para IAStudio

- Fuente: https://github.com/NeverSight/learn-skills.dev
- Problema que resuelve: depender solo de repos enviados manualmente o crear skills propias sin revisar si ya existe una mejor.
- Como se aplica en Saul IA Studios: usar rankings, feed, cache de `SKILL.md` y watchlist para descubrir skills utiles por categoria antes de construir.
- Archivos o plantillas relacionadas: `memory/learn-skills-iastudio.md`, `memory/skill-radar-watchlist.md`, `memory/repos-github.md`.
- Nivel: operativo documental.
- Proxima prueba: consultar el radar antes de crear la skill interna `landing-demo-nicho`.

### Evaluacion de skills antes de instalar

- Fuente: Learn Skills outputs `skills_index.json`, `skills-md/` y manual skills.
- Problema que resuelve: instalar skills por popularidad sin revisar calidad, scope, seguridad o costo de contexto.
- Como se aplica en Saul IA Studios: evaluar cada skill con criterios: fuente, caso de uso, madurez, dependencias, riesgo, solapamiento y prueba pequena.
- Archivos o plantillas relacionadas: `memory/learn-skills-iastudio.md`.
- Nivel: operativo.
- Proxima prueba: aplicar checklist a 3 skills candidatas.

### Feed de aprendizaje continuo de skills

- Fuente: `data/feed.json`, `data/feed.xml` y rankings hot/trending de `NeverSight/learn-skills.dev`.
- Problema que resuelve: perder novedades utiles en el ecosistema de agentes.
- Como se aplica en Saul IA Studios: revisar periodicamente skills nuevas en categorias clave: n8n, WhatsApp, Supabase, UI, seguridad, ventas, research y documentos.
- Archivos o plantillas relacionadas: `memory/skill-radar-watchlist.md`, `memory/evolucion.md`.
- Nivel: idea operativa.
- Proxima prueba: definir cadencia semanal/manual de revision.

### Banco Cult UI para landings y demos

- Fuente: https://github.com/nolly-studio/cult-ui y https://www.cult-ui.com/docs
- Problema que resuelve: interfaces correctas pero genericas, sin microinteraccion, demos poco memorables o falta de piezas UI listas para adaptar.
- Como se aplica en Saul IA Studios: elegir 1-3 componentes Cult UI por pantalla para elevar landings, demos, dashboards o artefactos IA, siempre adaptados al design-system propio.
- Archivos o plantillas relacionadas: `memory/cult-ui-iastudio.md`, `design-system/MASTER.md`, `design-system/DESIGN.md`.
- Nivel: operativo documental.
- Proxima prueba: usar una pieza como `Browser Window`, `Terminal Animation`, `Cutout Card` o `Border Beam Button` en una demo real.

### Componentes componibles con components-build

- Fuente: `.agents/skills/components-build/SKILL.md` de `nolly-studio/cult-ui`.
- Problema que resuelve: componentes internos dificiles de mantener, poco accesibles o demasiado configurados.
- Como se aplica en Saul IA Studios: al crear componentes propios, priorizar composicion, accesibilidad, props tipadas, soporte controlled/uncontrolled cuando aplique, `data-state`, tokens y `cn()`.
- Archivos o plantillas relacionadas: `memory/cult-ui-iastudio.md`, `design-system/MASTER.md`.
- Nivel: criterio operativo.
- Proxima prueba: aplicar al proximo componente reusable de landing/demo.

### Revision de motion performance

- Fuente: `.claude/skills/fixing-motion-performance/SKILL.md` de `nolly-studio/cult-ui`.
- Problema que resuelve: animaciones lindas pero pesadas, jank en mobile, scroll roto o efectos que consumen pintura/layout sin necesidad.
- Como se aplica en Saul IA Studios: antes de entregar interfaces con movimiento, revisar transform/opacity, pause off-screen, no blur continuo en superficies grandes, no mezclar sistemas de animacion y respetar `prefers-reduced-motion`.
- Archivos o plantillas relacionadas: `memory/cult-ui-iastudio.md`, `design-system/MASTER.md`.
- Nivel: operativo.
- Proxima prueba: auditar una landing/demo con animaciones nuevas.

### Shadcn registry y MCP para UI

- Fuente: docs de instalacion y MCP de Cult UI.
- Problema que resuelve: copiar componentes a mano sin trazabilidad o instalar UI sin saber dependencias.
- Como se aplica en Saul IA Studios: configurar `@cult-ui` en `components.json` solo en proyectos React/shadcn aptos; usar shadcn MCP para buscar/instalar componentes con lenguaje natural cuando el proyecto lo justifique.
- Archivos o plantillas relacionadas: `memory/cult-ui-iastudio.md`, `memory/claude-code-setup-iastudio.md`.
- Nivel: radar operativo.
- Proxima prueba: simular busqueda de componentes antes de tocar un proyecto cliente.

### Router IAStudio de auto-invocacion de agentes

- Fuente: https://github.com/msitarzewski/agency-agents
- Problema que resuelve: hacer o modificar proyectos desde una sola mirada, saltando roles clave como workflow, seguridad, QA, ventas o handoff.
- Como se aplica en Saul IA Studios: antes de crear o modificar proyectos, clasificar el trabajo y activar todos los especialistas aplicables por fase y riesgo.
- Archivos o plantillas relacionadas: `memory/agency-agents-iastudio.md`, `memory/observations-index.md`, `CLAUDE.md`.
- Nivel: operativo documental.
- Proxima prueba: usarlo en la proxima modificacion real de landing, workflow n8n, CRM o propuesta.

### Orquestacion PM Workflow Build QA Reality

- Fuente: `specialized/agents-orchestrator.md`, `specialized/specialized-workflow-architect.md` y `testing/testing-reality-checker.md` de `agency-agents`.
- Problema que resuelve: avanzar de idea a implementacion sin mapa de flujos, sin handoffs y sin evidencia de que funciona.
- Como se aplica en Saul IA Studios: para cambios grandes, pasar por Project Manager Senior, Workflow Architect, implementador, Evidence Collector y Reality Checker.
- Archivos o plantillas relacionadas: `memory/agency-agents-iastudio.md`, `memory/superpowers-iastudio.md`, `memory/ecc-iastudio.md`.
- Nivel: operativo.
- Proxima prueba: crear task list y reality check para el siguiente entregable tecnico.

### Prospeccion por senales y propuestas especializadas

- Fuente: `sales/sales-outbound-strategist.md` y `sales/sales-proposal-strategist.md` de `agency-agents`.
- Problema que resuelve: outreach generico, propuestas que solo listan servicios y pipeline medido por volumen en vez de calidad.
- Como se aplica en Saul IA Studios: activar Outbound Strategist, Discovery Coach, Sales Engineer y Proposal Strategist para campañas, demos, objeciones y propuestas.
- Archivos o plantillas relacionadas: `memory/agency-agents-iastudio.md`, `agente-comercial-agencia/`, `mensajes-personalizados-opticas-dia1.md`.
- Nivel: operativo documental.
- Proxima prueba: usar en el siguiente batch comercial o propuesta a cliente.

### Reality checking con evidencia

- Fuente: `testing/testing-reality-checker.md` de `agency-agents`.
- Problema que resuelve: declarar proyectos listos sin screenshots, pruebas end-to-end o comparacion contra requerimientos.
- Como se aplica en Saul IA Studios: toda entrega importante termina con estado READY / NEEDS WORK / BLOCKED, evidencia, issues y fixes requeridos.
- Archivos o plantillas relacionadas: `memory/agency-agents-iastudio.md`, `memory/ecc-iastudio.md`, `design-system/critique-rubric.md`.
- Nivel: operativo.
- Proxima prueba: aplicar al cierre de una landing/demo con capturas desktop/mobile.

### Quality gate web premium

- Fuente: `C:\Users\Usuario 01\Documents\Downloads\prompt-agente-web-premium.txt`
- Problema que resuelve: landings o propuestas web que funcionan pero se ven genericas, sin sistema visual ni autocritica.
- Como se aplica en Saul IA Studios: antes de entregar landing, demo o propuesta web, revisar sistema de diseno, jerarquia, efectos, interacciones, tipografia, iconografia, responsive, performance y accesibilidad.
- Archivos o plantillas relacionadas: `memory/prompt-agente-web-premium-iastudio.md`, `design-system/MASTER.md`, `design-system/DESIGN.md`.
- Nivel: operativo documental.
- Proxima prueba: usarlo en la proxima mejora de `index.html` o demo comercial.

### Tesis visual antes de implementar

- Fuente: `prompt-agente-web-premium.txt`.
- Problema que resuelve: empezar a codear sin diferenciar visualmente la pieza ni saber que momentos deben vender la experiencia.
- Como se aplica en Saul IA Studios: para cambios web relevantes, definir tesis visual, sistema de color, sistema tipografico y tres momentos visuales clave antes de ejecutar.
- Archivos o plantillas relacionadas: `memory/prompt-agente-web-premium-iastudio.md`, `memory/open-design-iastudio.md`.
- Nivel: operativo.
- Proxima prueba: documentar tesis visual breve antes de un rediseno.

### Autocritica premium de propuesta web

- Fuente: `prompt-agente-web-premium.txt`.
- Problema que resuelve: entregar "se ve bien" sin pasar por prohibiciones, performance, accesibilidad o criterio de showcase.
- Como se aplica en Saul IA Studios: antes de cerrar, comparar contra prohibiciones premium, verificar que cada efecto tenga proposito y dejar nota de siguiente iteracion.
- Archivos o plantillas relacionadas: `memory/prompt-agente-web-premium-iastudio.md`, `design-system/critique-rubric.md`, `memory/agency-agents-iastudio.md`.
- Nivel: operativo.
- Proxima prueba: incluir en el reality check de la proxima landing.

### Auditoria SEO/GEO IAStudio

- Fuente: https://github.com/AgriciDaniel/claude-seo
- Problema que resuelve: landings y demos visualmente fuertes pero sin indexabilidad, schema, performance, citabilidad IA o backlog SEO claro.
- Como se aplica en Saul IA Studios: antes o despues de publicar paginas publicas, revisar SEO tecnico, contenido, schema, sitemap, imagenes, CWV, GEO, SXO y prioridad de fixes.
- Archivos o plantillas relacionadas: `memory/claude-seo-iastudio.md`, `design-system/DESIGN.md`, `memory/prompt-agente-web-premium-iastudio.md`.
- Nivel: operativo documental.
- Proxima prueba: auditar `index.html` o una demo publica antes del proximo despliegue.

### SEO local para pymes

- Fuente: `skills/seo-local/SKILL.md` de `AgriciDaniel/claude-seo`.
- Problema que resuelve: clientes locales que tienen web pero no comunican NAP, comuna, servicio, reseñas, GBP, schema ni areas de atencion con claridad.
- Como se aplica en Saul IA Studios: para opticas, constructoras, servicios y negocios locales, revisar Google Business Profile, NAP, reviews, paginas de servicio, LocalBusiness schema y citaciones basicas.
- Archivos o plantillas relacionadas: `memory/claude-seo-iastudio.md`, `seo-comunicacion-landing-agencia.md`, `clientes/_PLANTILLA-CLIENTE/`.
- Nivel: operativo.
- Proxima prueba: convertir en mini-servicio "SEO local express".

### Schema y datos estructurados

- Fuente: `skills/seo-schema`, `schema/templates.json` y reglas del orquestador de `claude-seo`.
- Problema que resuelve: paginas que los buscadores e IA entienden solo por texto visible, sin entidad estructurada.
- Como se aplica en Saul IA Studios: generar o revisar `Organization`, `LocalBusiness`, `Service`, `Product`, `BreadcrumbList` y `WebSite` cuando corresponda.
- Archivos o plantillas relacionadas: `memory/claude-seo-iastudio.md`.
- Nivel: operativo documental.
- Proxima prueba: agregar schema minimo a una landing real si falta.

### SEO drift monitoring

- Fuente: `seo-drift` y scripts de baseline/compare de `claude-seo`.
- Problema que resuelve: redisenos que mejoran la visual pero rompen title, H1, schema, canonical, indexabilidad o CTA SEO.
- Como se aplica en Saul IA Studios: antes de cambios grandes, registrar baseline SEO; despues comparar y documentar regresiones o mejoras.
- Archivos o plantillas relacionadas: `memory/claude-seo-iastudio.md`, `memory/ecc-iastudio.md`.
- Nivel: idea operativa.
- Proxima prueba: guardar baseline manual antes de modificar `index.html`.

### Video programatico con Remotion

- Fuente: https://github.com/remotion-dev/skills y skill local `remotion`.
- Problema que resuelve: depender de edicion manual para demos, ads, reportes y piezas repetibles por cliente.
- Como se aplica en Saul IA Studios: crear composiciones React versionables para videos de oferta, clips verticales, dashboard-to-video, explicadores y casos.
- Archivos o plantillas relacionadas: `memory/remotion-skills-iastudio.md`, `design-system/DESIGN.md`, `memory/prompt-agente-web-premium-iastudio.md`.
- Nivel: operativo documental.
- Proxima prueba: crear un clip vertical de 15-30 segundos para una demo o servicio.

### Plantillas de video parametrizables

- Fuente: `skills/remotion/rules/parameters.md` de `remotion-dev/skills`.
- Problema que resuelve: rehacer videos completos al cambiar cliente, nicho, metrica, color u oferta.
- Como se aplica en Saul IA Studios: usar Zod schemas para props editables como cliente, nicho, CTA, colores, escenas, metricas y assets.
- Archivos o plantillas relacionadas: `memory/remotion-skills-iastudio.md`, `clientes/_PLANTILLA-CLIENTE/`.
- Nivel: idea operativa.
- Proxima prueba: definir props base para plantilla `demo-nicho-video`.

### Captions y voiceover sincronizados

- Fuente: `skills/remotion/rules/subtitles.md` y `skills/remotion/rules/voiceover.md`.
- Problema que resuelve: videos sin subtitulos legibles o voz desincronizada con escenas.
- Como se aplica en Saul IA Studios: manejar captions como JSON, audio en `public/`, duracion dinamica con `calculateMetadata` y QA de legibilidad mobile.
- Archivos o plantillas relacionadas: `memory/remotion-skills-iastudio.md`.
- Nivel: radar operativo.
- Proxima prueba: aplicar en primer video con narracion.

### QA de render motion

- Fuente: `skills/remotion/SKILL.md` y `rules/timing.md`.
- Problema que resuelve: animaciones que se ven bien en idea pero fallan al render, tienen cortes raros o pierden legibilidad.
- Como se aplica en Saul IA Studios: usar frame-based motion, render stills de control, revisar primer frame, frame medio, final, audio, captions y safe area.
- Archivos o plantillas relacionadas: `memory/remotion-skills-iastudio.md`, `memory/agency-agents-iastudio.md`.
- Nivel: operativo.
- Proxima prueba: usar render still al primer prototipo Remotion.

### Ingesta segura de carpetas Drive

- Fuente: carpeta Google Drive entregada el 2026-05-22.
- Problema que resuelve: confundir un link recibido con contenido realmente leido e integrado.
- Como se aplica en Saul IA Studios: registrar carpeta, estado de acceso, folder ID y proximo paso; solo extraer habilidades cuando los archivos sean legibles.
- Archivos o plantillas relacionadas: `memory/fuentes-drive.md`, `memory/google-drive-folder-iastudio.md`.
- Nivel: operativo documental.
- Proxima prueba: procesar la carpeta cuando se comparta acceso publico, ZIP o archivos individuales.

### Auditoria Claude Code Setup

- Fuente: https://www.tododeia.com/community/claude-code-setup y `anthropics/claude-plugins-official`.
- Problema que resuelve: arrancar proyectos sin saber que hooks, skills, MCPs, subagents o slash commands convienen.
- Como se aplica en Saul IA Studios: correr o simular una auditoria read-only por proyecto y aplicar solo 1-2 automatizaciones prioritarias.
- Archivos o plantillas relacionadas: `memory/claude-code-setup-iastudio.md`, `memory/skill-radar-watchlist.md`, `memory/n8n-mcp-iastudio.md`.
- Nivel: operativo documental, pendiente de prueba en Claude Code.
- Proxima prueba: auditar `IAStudio_Lanzamiento` o un cliente antes de agregar nuevas automatizaciones.

### Matriz de automatizaciones Claude Code

- Fuente: `claude-automation-recommender/SKILL.md`.
- Problema que resuelve: mezclar en una misma bolsa hooks, skills, MCPs, subagents y slash commands.
- Como se aplica en Saul IA Studios: elegir herramienta segun tipo de problema: hook para proteccion/repeticion, skill para conocimiento reutilizable, MCP para integracion externa, subagent para revision especializada y slash command para workflow corto repetido.
- Archivos o plantillas relacionadas: `memory/claude-code-setup-iastudio.md`.
- Nivel: operativo.
- Proxima prueba: convertir la matriz en checklist antes de configurar un proyecto nuevo.

### Workflows n8n probados — La Tribu Divisual

- Fuente: Google Drive La Tribu Divisual (2026-05-25) — 7 JSONs de n8n workflows reales.
- Problema que resuelve: construir agentes desde cero cuando existen workflows completos y probados por otra agencia IA.
- Como se aplica en Saul IA Studios: importar JSONs directamente en n8n, adaptar webhooks y credenciales, re-etiquetar como servicio propio. Workflows disponibles: WhatsApp (46KB), LinkedIn (63KB), Publicador Instagram (53KB), AutoShorts (14KB), Wan2.5 video (14KB), Instagram engagement (11KB), Agente Olaf (15KB).
- Archivos o plantillas relacionadas: `memory/la-tribu-recursos-iastudio.md`, `memory/n8n-mcp-iastudio.md`.
- Nivel: pendiente descarga e importacion.
- Proxima prueba: descargar `Agente Whatsapp La Tribu Divisual.json` e importar en n8n local para analizar nodos.

### Guiones de llamada fría probados — La Tribu Divisual

- Fuente: `guion-llamada-frio-divisual.pdf` y `guion-llamada-frio-tribu.pdf` del Drive.
- Problema que resuelve: scripts de llamada fría genéricos que no cierran citas ni generan interés real.
- Como se aplica en Saul IA Studios: reemplazar o enriquecer `scripts-llamada-fijos.md` con frases y estructura probada por Divisual — aplicar en las 4 ópticas con fijo pendientes de llamar.
- Archivos o plantillas relacionadas: `scripts-llamada-fijos.md`, `memory/la-tribu-recursos-iastudio.md`.
- Nivel: pendiente descarga.
- Proxima prueba: leer ambos PDFs y actualizar `scripts-llamada-fijos.md` antes de la próxima llamada.

### Generación de video corto automático (AutoShorts + Wan 2.5)

- Fuente: `AutoShorts - La Tribu Divisual.json` + `Wan 2.5 La Tribu Divisual.json`.
- Problema que resuelve: la creación de video corto (Reels, TikTok, Shorts) es cara y lenta si se hace manualmente.
- Como se aplica en Saul IA Studios: nueva oferta de servicio "Content IA Video" — generar 5-10 videos cortos/semana de forma automática para clientes que contraten el servicio. Precio estimado: $120K-$180K/mes.
- Archivos o plantillas relacionadas: `memory/la-tribu-recursos-iastudio.md`, `memory/remotion-skills-iastudio.md`.
- Nivel: pendiente descarga y análisis de nodos.
- Proxima prueba: analizar el JSON de AutoShorts para entender qué plataforma de video usa (Kling, Runway, Wan) y si requiere API de pago.

### Plantilla de oferta irresistible — La Tribu Divisual

- Fuente: `plantilla_oferta_irresistible.docx` del Drive.
- Problema que resuelve: propuestas que no cierran porque la estructura de valor no es clara ni urgente.
- Como se aplica en Saul IA Studios: comparar estructura con propuestas actuales (Carnes Lolol, ópticas) y absorber componentes faltantes (garantía, urgencia, stack de valor, nombre del paquete).
- Archivos o plantillas relacionadas: `agente-comercial-agencia/02-ofertas-entrada.md`, `clientes/carnes-lolol/`, `oferta-pack-emprendedor-360.md`.
- Nivel: pendiente descarga.
- Proxima prueba: leer el docx y aplicar su estructura a la propuesta de Carnes Lolol.

### Setup IA local en VPS (OpenClaw + Ollama + Hostinger)

- Fuente: `2026-04-05-openclaw-ollama-hostinger-setup.pdf` del Drive.
- Problema que resuelve: clientes que quieren IA local sin pagar APIs de OpenAI o Anthropic mensualmente.
- Como se aplica en Saul IA Studios: posible nuevo servicio "IA Local" — instalar Ollama con modelo open-source en VPS Hostinger del cliente por tarifa mensual fija ($X). Ideal para pymes con datos sensibles.
- Archivos o plantillas relacionadas: `stack-tecnico.md`, `memory/la-tribu-recursos-iastudio.md`.
- Nivel: pendiente descarga y evaluacion de viabilidad.
- Proxima prueba: leer el PDF y estimar costo de VPS + tiempo de setup para definir precio de oferta.
