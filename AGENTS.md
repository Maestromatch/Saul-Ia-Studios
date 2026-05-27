# Saul IA Studios — Estado del proyecto

Archivo de contexto para retomar rápido tras apagón / nueva sesión. Mantener actualizado.

## Identidad
- Marca: **Saul IA Studios SpA** (en formalización)
- Carpeta raíz: `C:\Users\Usuario 01\IAStudio_Lanzamiento\`
- Promesa: "IA instalada en tu negocio en 7 días"
- Cerebro doctrinario del agente comercial: `./agente ventas/` (Hormozi + DeMarco + guías propias)

## Productos (3)
1. **Pack IA Express** ($250K-$450K) — piloto bot + landing + CRM
2. **Formaliza Tu Negocio** ($89K DIY / $249K Híbrido / $590K Llave en mano)
3. **Pack Emprendedor 360** ($590K Esencial / $890K Pro) — flagship 45 días

## Nicho activo
**Ópticas** zona sur RM (El Bosque, San Bernardo, La Cisterna, San Miguel, Maipú).
Servicios técnicos queda en pausa.

## WhatsApp operativo
`+56968171774` (configurado en `index.html` y `demo-opticas.html`)

## Estado al 2026-05-18
- **Plan 48h comercial**: Día 1 sin empezar (0 mensajes enviados)
- **Constitución SpA**: corre en paralelo, Saúl la ejecuta físicamente (checklist en `mi-spa-checklist.md`)
- **Landing `index.html` v3 Agencia**: ✅ reposicionada desde "IA + empresa lista" hacia "sistemas IA para captar y convertir clientes por WhatsApp"; incluye tres caminos, servicios principales, mini-servicios, caso interno Saul El Constructor, proceso, confianza y FAQ. Formaliza/Pack 360 bajaron de protagonismo para evitar dispersión.
- **Demos interactivas**: 4 escenarios por demo con tabs + JS vanilla. Ópticas: lentes/examen/reparación/convenio. Servicio técnico: notebook/celular/impresora/domicilio
- **Demo `demo-opticas.html`**: ✅ desplegada en `https://saul-ia-studios.vercel.app/demo-opticas.html`
- **Repo GitHub**: `https://github.com/Maestromatch/Saul-Ia-Studios` sincronizado (force-push aplicado el 2026-05-15, se sobrescribieron 2 commits viejos)
- **Tracker ópticas**: 22 prospectos investigados; 3 con WhatsApp confirmado online, 4 con fijo, 15 requieren verificación manual IG/FB
- **Mensajes personalizados**: 22 mensajes hiper-personalizados listos en `mensajes-personalizados-opticas-dia1.md`

## URLs operativas
- Landing: `https://saul-ia-studios.vercel.app/`
- Demo Ópticas (compartir por WhatsApp): `https://saul-ia-studios.vercel.app/demo-opticas.html`
- Demo Servicio Técnico: `https://saul-ia-studios.vercel.app/demo-servicio-tecnico.html`
- Demo Constructora (dogfooding caso interno): `https://saul-ia-studios.vercel.app/demo-constructora.html`
- Repo: `https://github.com/Maestromatch/Saul-Ia-Studios`

## Tracks en paralelo
- **Track A · Ópticas** (Saúl ejecuta físico): enviar mensajes, llamar fijos, verificar IG/FB, primer cierre — pausado pendiente
- **Track B · Constructora interna** (dogfooding): bot WhatsApp ✅ FUNCIONANDO (ejecución 1132 exitosa). Landing v3 ✅ DESPLEGADA en `landing-bio-saul.vercel.app`. Chat widget web ✅ integrado. **Próximo**: importar `n8n-webchat-workflow.json` + test 6 casos — ver `clientes/saul-el-constructor/CHECKPOINT-2026-05-18.md`.
- **Track C · Ads Growth Constructoras** (agencia): módulo premium de captación pagada para Saul El Constructor y futuras constructoras. Carpeta creada en `clientes/saul-el-constructor/05-ads-growth/` con brief, campaña Meta 14 días, matriz de anuncios, guía creativa, tracking CRM, rutina de optimización, respuestas y reporte semanal.

## Bloqueos abiertos
1. WhatsApps faltantes: 4 ópticas con fijo (llamar para pedir WA), 15 con verificación manual por IG/FB
2. Tracker operativo `tracker-prospeccion-opticas.csv` desactualizado vs nuevo seed de 22 prospectos
3. Decisión pendiente: Mac-Hale El Bosque / La Cisterna (cadena con web corporativa robusta — recomendación agente: descartar)
4. **Track B**: importar `n8n-webchat-workflow.json` en n8n + asignar credenciales + pegar API key OpenAI
5. **Track B**: test 6 casos WhatsApp (ver `casos-prueba.md`) antes de activar producción
6. **n8n plan**: 837+/1000 ejecuciones — decidir upgrade ($20/mes) o migrar webchat a Vercel serverless
7. **Track C Ads**: no lanzar presupuesto hasta que bot/CRM/landing pasen test end-to-end y existan fotos/videos reales suficientes.

## Decisiones tomadas
- Foco vertical 1: ópticas
- Precio piloto: $250K-$450K (50% anticipo / 50% contra entrega)
- Constitución SpA con abogado (no solo IA — error pasado documentado)
- OS (producto empaquetado) NO se lanza en este sprint, queda mes 3-4

## Archivos clave (orden de uso)
- `memory/observations-index.md` — leer primero para recuperar contexto por IDs antes de abrir archivos largos
- `protocolo-memoria-y-verificacion-agencia.md` — reglas locales de memoria, anti-secretos y verificacion por evidencia
- `design-system/MASTER.md` — criterio visual base para landing, demos y dashboards
- `README.md` — visión global del kit
- `iastudio-os-vision.md` — producto OS futuro (mes 3-4)
- `plan-48-horas.md` — misión actual día 1-2 comercial
- `agente ventas/agente-comercial-playbook.md` — 7 flujos del agente
- `demo-opticas.html` + `index.html` + `style.css` — frontend
- `catalogo-servicios-agencia-v1.md` / `mini-servicios-entrada-v1.md` / `manual-creador-servicios-saul-v1.md` — oferta y ejecucion de agencia
- `seo-comunicacion-landing-agencia.md` — criterio SEO y comunicacion para landing principal
- `mensaje-demo-opticas.md` — mensajes de prospección con cadencia 1-3-7-15-30
- `mensajes-personalizados-opticas-dia1.md` — 22 mensajes hiper-personalizados listos para enviar
- `tracker-prospeccion-opticas.csv` — pipeline operativo
- `prospectos-opticas-seed.csv` — semilla de prospectos (22)
- `clientes/_PLANTILLA-CLIENTE/` — estructura post-cierre (onboarding/construccion/entrega/testimonio)
- `clientes/saul-el-constructor/05-ads-growth/` — módulo premium Ads Growth para constructoras (campañas, copy, tracking, optimización y aprendizaje)
- `sop-entrega-piloto-opticas.md` — SOP 5 fases del piloto
- `onboarding-cliente-opticas.md` — cuestionario maestro ópticas
- `stack-tecnico.md` — herramientas, costos, FAQ técnicas (ref interna + respuestas a prospectos)
- `oferta-pack-emprendedor-360.md` — flagship 2 tiers ($590K/$890K), 45 días
- `oferta-formaliza-tu-negocio.md` — 3 tiers ($89K/$249K/$590K), comparativa, costos terceros
- `mi-spa-checklist.md` / `mi-spa-datos-clave.md` — formalización SpA paralela
- `landing-dual-wireframe.md` — wireframe original (ya implementado en index.html v2)
- `scripts-llamada-fijos.md` — guion para llamar a los 4 prospectos con fijo
- `flujo-respuestas-spin-opticas.md` — plantillas SPIN listas para cuando respondan los 3 inmediatos

## Cerebro operativo extendido (`tips/`)

Carpeta con 22 guías propias del usuario (comerciales, técnicas, operativas). **Consultar antes de proponer enfoques nuevos** — reflejan cómo Saúl piensa el negocio y el stack. Índice por categoría en `memory/reference_tips_iastudio.md` (memoria persistente).

## Memoria y design system

Nueva carpeta `memory/` activa como memoria progresiva:
- `observations-index.md`: indice ligero y primera lectura.
- `evolucion.md`: timeline estrategico.
- `repos-github.md`: repos integrados como habilidades.
- `habilidades.md`: capacidades internas extraidas.
- `ui-ux-pro-max-iastudio.md`: protocolo UI/UX.
- `Codex-mem-iastudio.md`: regla de memoria por capas.

Regla:
- antes de cambios grandes, leer indice de memoria;
- para UI, revisar `design-system/MASTER.md` y override de pagina;
- para landing, demo o propuesta web premium, revisar `agente-comercial-agencia/memory/prompt-agente-web-premium-iastudio.md`;
- para crear o modificar proyectos, aplicar `agente-comercial-agencia/memory/agency-agents-iastudio.md` y auto-invocar todos los agentes que apliquen por fase y riesgo;
- no guardar tokens ni secretos;
- cada aprendizaje reusable debe convertirse en SOP, plantilla, oferta, skill o checklist.

## Auto-invocacion de agentes

Regla activa desde 2026-05-21:
- En proyectos nuevos o modificaciones importantes, usar `agente-comercial-agencia/memory/agency-agents-iastudio.md` como router.
- Activar especialistas por fase: Project Manager Senior, Workflow Architect, Arquitectura/UX, implementador, Security Engineer, Evidence Collector, Reality Checker y Technical Writer.
- Para ventas/propuestas, activar Outbound Strategist, Discovery Coach, Sales Engineer, Proposal Strategist y Pipeline Analyst.
- Para UI/frontend, activar Frontend Developer, UI Designer, UX Architect, Accessibility Auditor y Performance Benchmarker.
- Para automatizaciones, activar Workflow Architect, Automation Governance Architect, API Tester, Security Engineer y Reality Checker.
- Si el entorno permite subagentes reales y el trabajo se puede paralelizar, delegar con scopes separados. Si no, aplicar estos roles como checklist operativo.

## Reglas operativas del sprint
- Mantener datos hardcoded esta semana; al empacar OS (mes 3-4) se variabilizan a `{{NOMBRE_AGENCIA}}`, `{{NUMERO_WHATSAPP}}`, etc.
- Cada archivo nuevo idealmente marca transferibilidad OS al pie (comentario)
- No optimizar marca/logo/colores antes de vender
- Push directo a main autorizado solo en proyecto Mastermatch (no aplica acá)

## Subagente disponible
`agente-comercial-saul` — investigación de prospectos, ACA, SPIN, propuestas, seguimiento, objeciones para los 3 productos. Cerebro vive en `./agente ventas/`.

## Próximos pasos sugeridos (cuando se retome)
### Track B — Constructor Saúl (PRIORITARIO)
1. Importar `clientes/saul-el-constructor/02-construccion/n8n-webchat-workflow.json` en n8n → asignar credenciales Supabase + pegar OpenAI API key
2. Test chat widget en `landing-bio-saul.vercel.app` (burbuja bottom-right)
3. Correr 6 casos de prueba WhatsApp (`casos-prueba.md`) → si pasan, activar producción
4. Subir fotos obras a `C:\Users\Usuario 01\landing-bio-saul\obras\` para reemplazar placeholders

### Track C — Ads Growth Constructoras
5. Completar brief en `clientes/saul-el-constructor/05-ads-growth/01-brief-cliente.md`
6. Recolectar 10-20 fotos reales + 2 videos cortos según `04-guia-creativos.md`
7. Lanzar campaña piloto 14 días desde `02-campana-meta-14-dias.md` solo cuando Track B esté estable
8. Registrar aprendizaje diario en `09-learning-log.md`

### Track A — Ópticas (cuando Track B esté cerrado)
9. Lanzar `agente-comercial-saul` para expandir lista ópticas con WhatsApp verificados (meta 40)
10. Enviar primer batch mensajes Día 1 con link demo ópticas

## Git workflow en esta máquina
- Push/fetch a GitHub requiere flag SSL: `git -c http.schannelCheckRevoke=false push ...`
- Branch principal: `main`
- Vercel autodesplega en cada push a main (≤1 min)

---

**Última actualización**: 2026-05-18
**Mantener actualizado**: al terminar cada sesión, ajustar Estado / Bloqueos / Decisiones / Próximos pasos.
