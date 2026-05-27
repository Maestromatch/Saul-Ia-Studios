# Open Design IAStudio

> Adaptacion del repo `nexu-io/open-design` para Saul IA Studios.

Fuente principal: https://github.com/nexu-io/open-design

## Que es

Open Design es una alternativa local-first y open-source a Claude Design/Figma orientada a generar artefactos visuales con agentes. Usa skills, design systems en Markdown, preview sandbox, export y un daemon local que puede delegar en CLIs como Codex, Claude Code, Gemini, Cursor, OpenCode y otros.

Version revisada:
- `0.8.0-preview`
- Licencia: Apache-2.0
- Stack: Next.js, React, TypeScript, Node 24, Express daemon, SQLite, pnpm, Docker, Electron opcional.

## Valor para IAStudio

Open Design convierte "crear diseno" en una cadena controlada:

1. Brief interactivo.
2. Eleccion de direccion visual.
3. Design system activo en `DESIGN.md`.
4. Skill adecuada para el artefacto.
5. Template/layout library.
6. Preview sandbox.
7. Autocritica 5D.
8. Export o entrega.

Para IAStudio esto sirve en:
- Landing agencia.
- Demos por nicho.
- Dashboard CRM.
- Deck comercial.
- Social carousel.
- E-guide o mini lead magnet.
- Pricing page.
- Documento tipo propuesta.

## Decision de adopcion

No se instala completo por ahora.

Motivos:
- Requiere Node 24/pnpm o Docker.
- Crea y persiste datos en `.od/`.
- Puede manejar credenciales BYOK.
- Ejecuta agentes locales contra carpetas reales.
- Es mas plataforma que simple recurso.

Se adopta como metodologia y formato:
- `design-system/DESIGN.md`
- `design-system/critique-rubric.md`
- pipeline de brief -> artefacto -> critica -> entrega.

## Relacion con UI UX Pro Max

- `ui-ux-pro-max`: nos da criterio, patrones y checklist UI/UX.
- `open-design`: nos da pipeline de produccion de artefactos.

Juntos:
- UI UX Pro Max define que se ve bien y funciona.
- Open Design define como producirlo con agentes y repetirlo.

## Pipeline IAStudio para artefactos visuales

### 1. Brief interactivo

Antes de disenar, resolver:
- Superficie: landing, demo, dashboard, deck, carousel, e-guide.
- Audiencia: pyme local, constructora, optica, servicio tecnico, emprendedor.
- Objetivo: diagnostico, venta, confianza, educacion, onboarding.
- Tono: operativo, premium, cercano, tecnico, editorial.
- Marca: IAStudio o cliente.
- Escala: una pantalla, multipagina, deck, mobile, dashboard.
- Restricciones: WhatsApp, precio, datos reales, sin promesas falsas.

### 2. Direccion visual

Usar una de estas direcciones adaptadas:
- `Tech Utility`: sistemas, dashboards, CRM, bots.
- `Modern Minimal`: landing agencia, propuestas limpias.
- `Editorial Monocle`: decks, reportes, casos.
- `Warm Soft`: pymes locales, onboarding, formalizacion.
- `Brutalist Experimental`: solo para campanas o piezas llamativas, no para clientes conservadores.

### 3. DESIGN.md

Leer `design-system/DESIGN.md` antes de modificar o crear UI.

Regla:
- Si es IAStudio, usar este `DESIGN.md`.
- Si es cliente, crear `brand-spec.md` o override antes de disenar.

### 4. Skill o tipo de artefacto

Mapeo IAStudio:
- Landing principal -> `web-prototype` / `saas-landing`.
- Demo nicho -> `web-prototype`.
- CRM -> `dashboard`.
- Pricing/oferta -> `pricing-page`.
- Deck comercial -> `simple-deck` o `guizang-ppt`.
- Reporte cliente -> `finance-report` adaptado / `weekly-update`.
- Carrusel ads -> `social-carousel`.
- E-guide -> `digital-eguide`.

### 5. Preview mental

Aunque no usemos Open Design instalado, cada entrega debe imaginarse como artefacto exportable:
- HTML usable.
- PDF/print si es propuesta o deck.
- ZIP si es plantilla.
- Captura si es demo visual.

### 6. Critica 5D

Antes de cerrar:
- Filosofia: tiene una direccion clara.
- Jerarquia: se entiende que leer primero.
- Detalle: alineacion, spacing, copy, microinteracciones.
- Funcionalidad: CTA, responsive, formularios, tabs, export.
- Innovacion: tiene al menos un detalle memorable cuando corresponde.

## Reglas de seguridad y privacidad

- No guardar API keys ni credenciales en `.od/` sin decidirlo.
- No instalar artefactos en repo de cliente sin revisar licencia.
- No copiar design systems de marcas famosas como si fueran marca propia.
- Usar inspiracion, no plagio.
- Evitar que outputs generados contengan datos reales de clientes sin permiso.

## Que gana IAStudio

IAStudio gana una fabrica visual disciplinada: cada pieza importante parte con brief, usa un sistema visual portable, se produce como artefacto y se revisa con una rubrica antes de salir al cliente.
