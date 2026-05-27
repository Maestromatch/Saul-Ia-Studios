# Router de Agentes — Aetria Studio

Auto-invocación por fase y tipo de trabajo. Consultar antes de iniciar cualquier proyecto o tarea nueva.

---

## Cómo usar este router

Al inicio de cada tarea, identificar la fase y activar los agentes que aplican.
Si hay subagentes reales disponibles → delegar con scopes separados.
Si no → aplicar los roles como checklist operativo en orden.

---

## FASE COMERCIAL — Cliente nuevo / prospecto

| Agente | Rol | Cuándo activar |
|--------|-----|----------------|
| **agente-comercial-saul** | Ejecuta los 5 flujos: investigar, ACA, SPIN, propuesta, seguimiento | Siempre que entre un prospecto nuevo |
| Outbound Strategist | Define el ángulo de dolor y el mensaje | Antes del primer contacto |
| Discovery Coach | Prepara preguntas SPIN personalizadas | Antes de llamada de diagnóstico |
| Proposal Strategist | Construye la propuesta de 7 secciones | Post-llamada |
| Pipeline Analyst | Revisa el tracker y prioriza próximos pasos | Revisión semanal |

**Trigger:** `cliente nuevo: [nombre] | [rubro] | [zona]`
**Protocolo completo:** ver `memory/protocol_cliente_nuevo.md` en la memoria de Claude.

---

## FASE TÉCNICA — Proyecto / entregable nuevo

| Agente | Rol | Cuándo activar |
|--------|-----|----------------|
| Project Manager Senior | Define alcance, hitos y criterio de terminado | Al inicio de cualquier proyecto |
| Workflow Architect | Diseña flujos de automatización (n8n, WhatsApp, CRM) | Antes de construir automatizaciones |
| Frontend Developer | Landing, demo, dashboard, componentes UI | Proyectos con capa visual |
| Security Engineer | Revisa que no haya keys hardcodeadas ni inputs sin sanitizar | Antes de cualquier push a producción |
| Technical Writer | Documenta entregables, SOPs y onboarding del cliente | Al cierre de cada proyecto |

---

## FASE UI / FRONTEND

| Agente | Rol | Cuándo activar |
|--------|-----|----------------|
| UI Designer | Aplica identidad Aetria Studio | Cualquier interfaz nueva |
| UX Architect | Define flujo de usuario y jerarquía de información | Antes de maquetar |
| Accessibility Auditor | Verifica contraste, semántica y navegación | Antes de hacer push |
| Performance Benchmarker | Revisa peso de assets y tiempo de carga | Antes de deploy |

**Design system:** olive #2F3E2B + bronce #7A6248 sobre lino #F4F3EF · Playfair Display (headings) + Inter (cuerpo).

---

## FASE CONTENIDO / REDES

| Agente | Rol | Cuándo activar |
|--------|-----|----------------|
| Content Strategist | Define calendario, formatos y hooks por nicho | Al inicio del mes |
| Copywriter | Redacta posts y captions sin mencionar tecnología | Por pieza de contenido |
| Zernio Publisher | Publica en Instagram/Facebook vía Zernio MCP | Al aprobar cada pieza |

**Motor activo:** Zernio MCP — API key en zernio.com/dashboard/api-keys (NO guardar en repo).

---

## FASE SEO — Antes de push en landing pública

Checklist obligatorio antes de hacer push de cualquier página indexable:
- [ ] Title tag con keyword principal (rubro + ciudad)
- [ ] Meta description < 160 chars con CTA
- [ ] JSON-LD actualizado (ProfessionalService + FAQPage)
- [ ] Canonical URL correcta (aetriastudio.cl)
- [ ] OG image presente y actualizada

---

## Regla de evolución (cada sesión + cada domingo)

1. Actualizar `agente ventas/agente-comercial-aprendizajes.md` con aprendizaje de 1-2 frases.
2. Si el aprendizaje cambia un flujo → actualizar el playbook o este router.
3. Cada domingo: releer aprendizajes, proponer 1-3 mejoras al sistema.
