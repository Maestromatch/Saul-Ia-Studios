# La Tribu Divisual — Recursos Integrados

> Memoria operativa de los recursos de la comunidad "La Tribu Divisual" de Juan Pe Navarro / Divisual Project.
> Fuente: `_inbox/la-tribu/` (descargado 2026-05-25)
> Estado: LEÍDO Y CLASIFICADO ✅

---

## Resumen ejecutivo

El Drive de La Tribu contenía **mucho más** de lo esperado. No son solo n8n workflows sueltos — es un sistema operativo completo para una agencia IA:

- **17 skills instalables para Claude Code** (10 del divisual-skills-pack + 7 del COWORK pack + 3 del DEEPSEEK folder)
- **15 workflows n8n** listos para importar (comerciales, publicación, video)
- **2 guiones de llamada fría** completos con manejo de objeciones
- **1 metodología de diagnóstico** como servicio vendible

---

## SKILLS INSTALABLES PARA CLAUDE CODE

### Divisual Skills Pack — 10 skills (Bloque Negocio + Contenido)

| Skill | Carpeta | Qué hace | Valor para AetriaStudio |
|-------|---------|----------|------------------------|
| `crear-skill` | `01-crear-skill/` | Meta-skill: crea skills custom desde cero | Crear skills propias de AetriaStudio |
| `seo-optimizer` | `02-seo-optimizer/` | Audita web estática y aplica cambios SEO al código | Servicio SEO técnico para clientes |
| `prospeccion` | `03-prospeccion/` | Busca leads reales, analiza presencia digital, dashboard HTML + JSON | **PRIORIDAD ALTA** — automatiza Track A ópticas y expansión |
| `n8n-workflow-patterns` | `04-n8n-workflow-patterns/` | Genera workflows n8n desde lenguaje natural (5 patrones probados) | **PRIORIDAD ALTA** — construir workflows para clientes más rápido |
| `auditoria-negocio` | `05-auditoria-negocio/` | Diagnóstico 12 dimensiones: web, redes, ads, copy, customer journey, GMB, competencia | **PRIORIDAD ALTA** — "Servicio de Diagnóstico Inicial IA" como oferta de entrada |
| `create-briefing` | `06-create-briefing/` | Extrae transcripción de vídeo referencia → genera briefing listo para grabar | Track F posts y contenido YouTube |
| `analyze-video` | `07-analyze-video/` | Análisis estructural de vídeo viral | Investigación de contenido competencia |
| `youtube` | `08-claude-youtube/` | Orquestador completo canal YouTube (14 sub-skills: estrategia, SEO, shorts, thumbnails, scripts) | Servicio YouTube completo para clientes |
| `instagram-a-web` | `09-instagram-a-web/` | Convierte perfil Instagram en landing profesional | Oferta entrada rápida para clientes con IG |
| `10-video-use` | `10-video-use/` | Edición vídeo desde lenguaje natural: transcribir, cortar silencios, subtítulos, color, Manim | Track F posts + servicio video |

### 7 Skills Claude Cowork Pack

| Skill | Qué hace | Valor para AetriaStudio |
|-------|----------|------------------------|
| `espia-tendencias` | Monitoring X/Twitter via Grok con Computer Use — informe semanal de tendencias | Inteligencia de nicho para clientes + propios |
| `scraping-competencia` | Scraping de presencia digital de competidores | Análisis pre-propuesta para clientes |
| `diseno-canva` | Diseño Canva desde lenguaje natural | Contenido visual rápido |
| `dashboard-negocio` | Dashboard de métricas de negocio | Reportes para clientes |
| `emails-venta` | Genera secuencias de 7 emails con A/B testing, preview text, CTA, PS | **PRIORIDAD ALTA** — servicio email marketing para clientes |
| `auditor-seo` | Auditoría SEO completa | Complementa `seo-optimizer` |
| `calendario-contenido` | Planificación de calendario de contenido | Content Engine para clientes |

### Skills DEEPSEEK V4 (2 skills de alto valor comercial)

| Skill | Qué hace | Valor para AetriaStudio |
|-------|----------|------------------------|
| `landing-cliente-local` | Genera landing Next.js 15 completa para negocio local: hero, productos, mapa, WhatsApp CTA, SEO LocalBusiness schema | **PRIORIDAD ALTA** — acelera entrega Pack IA Express 10x |
| `propuesta-cliente` | Genera 3 archivos: PDF propuesta comercial, email listo para enviar, follow-up calendar | **PRIORIDAD ALTA** — automatiza generación de propuestas para Carnes Lolol, ópticas, etc. |

---

## WORKFLOWS N8N (JSONs)

### Workflows de prospección y comercial

| Archivo | Función real (analizado) | Usar para |
|---------|--------------------------|-----------|
| `Agente Icebreaker - Conseguir Clientes.json` | Lee lista de URLs desde Google Sheets → scraping web por HTTP → genera email personalizado con IA → actualiza Sheets con estado "Enviado" | Automatizar outreach a 100+ ópticas |
| `v2 Agente Email Scrapper.json` | Extrae emails de webs de empresas en volumen | Conseguir contactos de ópticas sin WhatsApp |
| `Agente Google Reviews.json` | Gestiona/responde reseñas de Google Maps con IA | Servicio gestión reputación para clientes |

### Workflows de publicación y contenido

| Archivo | Función | Usar para |
|---------|---------|-----------|
| `Agente Whatsapp La Tribu Divisual.json` (46KB) | Agente WhatsApp completo en n8n | Bot ópticas/constructoras — Track A y B |
| `LinkedIn Automático By La Tribu.json` (63KB) | Publicación automatizada LinkedIn | Canal B2B para AetriaStudio |
| `Publicador Insta Link By La Tribu Divisual.json` (53KB) | Publicador Instagram con links | Complementa Zernio |
| `Agente instagram la Tribu.json` (11KB) | Engagement Instagram automático | Crecimiento orgánico clientes |
| `La Tribu - Olaf.json` (15KB) | Agente IA personalizado (analizar) | TBD al importar |

### Workflows de video y ads

| Archivo | Función | Usar para |
|---------|---------|-----------|
| `AutoShorts - La Tribu Divisual.json` (14KB) | Generación automática de video corto | Nueva oferta "Content IA Video" |
| `Wan 2.5 La Tribu Divisual.json` (14KB) | Generación video IA con Wan 2.5 | Producción visual para clientes |
| `VEO 3 $100k ADS.json` | Workflow Meta Ads con VEO 3 video generation | Track C Ads Growth + nueva oferta ads |
| `APP Web La Tribu Divisual.json` | Agente para crear apps web | Oferta "App con IA" |

---

## GUIONES DE LLAMADA FRÍA (PDFs leídos)

Ambos PDFs son **idénticos en contenido**, diseño diferente (negro vs blanco). Autor: Juan Pe Navarro, Divisual Project.

**Metodología clave extraída e integrada en `scripts-llamada-fijos.md`:**

- Objetivo único: conseguir una REUNIÓN de 20 min (no vender, no pedir WhatsApp)
- "No vendes IA por teléfono. Vendes 20 minutos de su tiempo para un diagnóstico."
- Presencial cierra 3x más que videollamada — ventaja de estar en zona sur RM
- Versión A (si eres nuevo) — sinceridad rompe el patrón de defensa del decisor
- Versión B (con experiencia) — referir a casos anteriores
- 5 objeciones con respuestas exactas
- Arma secreta: Loom de 2 min → convierte el "no" en reunión el 30% de las veces
- Horario óptimo: martes a jueves, 10:00-12:00 y 16:00-18:00

---

## TEMPLATES COMERCIALES (DEEPSEEK folder)

### `propuesta-cliente.md` — Skill completa (leída)
Genera automáticamente 3 archivos:
1. `propuesta-comercial.pdf` — 5 páginas: portada, contexto, solución, precios+timeline, términos
2. `email-envio.md` — email personalizado listo para Gmail
3. `followup-calendar.md` — evento Google Calendar 3 días después

Inputs: nombre cliente, proyecto, precio total, timeline, entregables, forma de pago.

### `landing-cliente-local.md` — Skill completa (leída)
Genera landing Next.js 15 completa para negocio local:
- Stack: Next.js 15 + Tailwind CSS 4 + shadcn/ui + Google Maps iframe
- Secciones: Hero + CTA WhatsApp, Productos/Servicios grid, Sobre nosotros, Horarios + Mapa, Contacto
- SEO: LocalBusiness schema.org, OG tags, sitemap, robots.txt
- Outputs en carpeta `[nombre-cliente-slug]/` lista para deplovar en Vercel

---

## MATERIALES DE CAPACITACIÓN (para revisión manual)

| Carpeta | Contenido | Cuándo revisar |
|---------|-----------|----------------|
| `CONSEGUIR CLIENTES CON N8N/` | Tutorial completo de captación con n8n | Al configurar Agente Icebreaker |
| `3 AGENTES DE IA QUE GENERAN 5K/` | Agentes: Google Reviews + Icebreaker + Email Scrapper | Al escalar prospección |
| `APP CON IA/` | Tutorial crear apps web + Prompt Maestro docx | Al lanzar oferta "App con IA" |
| `$100K ADS VEO 3 PLANTILLA/` | Workflow ads con video IA + tutorial | Al activar Track C Ads |
| `SKILL CLAUDE CODE + PLAYWRIGHT/` | browser-automation.zip para web scraping avanzado | Al necesitar Playwright en skills |
| `GUIA-INSTALACION.pdf` | Cómo instalar el divisual-skills-pack | Al instalar las skills |

---

## Mapa de prioridad de integración

| Prioridad | Recurso | Acción |
|-----------|---------|--------|
| 🔴 INMEDIATO | `propuesta-cliente` skill | Usar para generar propuesta Carnes Lolol |
| 🔴 INMEDIATO | Guion llamada fría Modo B | Integrado en `scripts-llamada-fijos.md` ✅ |
| 🟡 ESTA SEMANA | `prospeccion` skill | Ampliar lista ópticas a 40+ con dashboard |
| 🟡 ESTA SEMANA | `auditoria-negocio` skill | Auditar Carnes Lolol y próximos prospectos |
| 🟡 ESTA SEMANA | `landing-cliente-local` skill | Template para entregar Pack IA Express más rápido |
| 🟠 MES 1 | `Agente Icebreaker` JSON | Automatizar outreach a 100+ ópticas |
| 🟠 MES 1 | `Agente Whatsapp` JSON | Mejorar bot Track A y B |
| 🟠 MES 1 | `emails-venta` skill | Crear secuencias email para seguimiento |
| 🔵 MES 2 | `LinkedIn Automático` JSON | Abrir canal B2B |
| 🔵 MES 2 | `AutoShorts` + `Wan 2.5` | Lanzar oferta "Content IA Video" |
| 🔵 MES 2 | `youtube` skill (14 sub-skills) | Canal YouTube AetriaStudio |
| ⚪ MES 3 | `10-video-use` Python | Edición video programático |

---

## Instrucción de instalación de skills

Ver `divisual-skills-instalacion.md` para guía paso a paso de cómo instalar estas skills en Claude Code globalmente o por proyecto.
