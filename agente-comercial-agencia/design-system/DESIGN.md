# Saul IA Studios DESIGN.md

> Design system portable compatible con el esquema de Open Design.

## Visual Theme & Atmosphere

Saul IA Studios debe sentirse como una agencia que instala sistemas reales de captacion, WhatsApp, CRM y automatizacion para pymes locales. El tono visual es sobrio, operativo y confiable: mas sistema instalado que promesa futurista.

Direcciones recomendadas:
- Tech Utility para dashboards, bots y CRM.
- Modern Minimal para landing agencia y propuestas.
- Editorial Monocle para decks, reportes y casos.
- Warm Soft para onboarding y formalizacion.
- Premium Product Site para propuestas web de mayor valor, usando tesis visual, sistema de tokens y momentos memorables.

Evitar estetica generica de IA con gradientes morados, brillo excesivo o ilustraciones sin relacion con el negocio.

## Color Palette & Roles

Tokens base:

```css
--ink: #17211f;
--muted: #5f6f6a;
--line: rgba(119, 138, 132, 0.24);
--paper: #e9eeec;
--surface: #f7f9f8;
--soft: #dce5e1;
--wash: #fbfcfb;
--accent: #087f68;
--accent-dark: #075f50;
--signal: #f0b429;
--white: #ffffff;
```

Roles:
- `--accent`: CTA principal, estados positivos y rutas de avance.
- `--accent-dark`: enfasis secundario y texto de accion.
- `--signal`: alerta suave u oportunidad.
- `--ink`: texto principal.
- `--muted`: descripcion, metadata y labels.
- `--paper`, `--surface`, `--soft`, `--wash`: fondos, paneles y separacion.

## Typography Rules

Fuente:
- Inter o system-ui.

Reglas:
- H1 grande solo en hero.
- Titulos compactos en cards, paneles y dashboards.
- Mantener letter spacing en 0 salvo etiquetas uppercase muy pequenas.
- No usar fuentes decorativas si no hay razon de marca.
- Priorizar legibilidad mobile.

## Component Stylings

Botones:
- Radio 8px.
- Alto minimo 44px.
- CTA principal verde.
- Estados hover/focus visibles.

Paneles:
- Bordes finos con `--line`.
- Fondo blanco o `--surface`.
- Sombra sutil solo cuando ayude a separar.

Cards:
- Usar para items repetidos o informacion enmarcada.
- No anidar cards dentro de cards.

Demos:
- Panel conversacional o sistema visual.
- Tabs cortos.
- Fila CRM o resumen de lead visible.

Cult UI / shadcn:
- Usar como fuente de componentes copy-source cuando el proyecto sea React/shadcn.
- Elegir pocas piezas de alto impacto y adaptarlas a tokens IAStudio.
- Evitar que la expresividad del componente reemplace claridad comercial.

## Layout Principles

Principios:
- Primera pantalla debe mostrar marca, problema, promesa y accion.
- Layouts con ancho contenido controlado.
- Grids claros, no decoracion flotante.
- Secciones full-width o layouts limpios, no stacks de cards sin jerarquia.
- En dashboards, densidad ordenada antes que hero visual.
- En piezas premium, un solo heroe visual por seccion y aire negativo intencional.

## Depth & Elevation

Profundidad:
- Bordes y fondos antes que sombras fuertes.
- Sombra solo para demo panel, modal o elemento que deba parecer activo.
- Evitar glassmorphism decorativo.
- Evitar capas con gradientes sin funcion.

## Do's and Don'ts

Do:
- Mostrar flujo: Ads -> Landing -> Bot -> CRM -> Follow-up.
- Usar copy concreto y medible.
- Mostrar proximo paso.
- Probar WhatsApp CTA.
- Usar datos ficticios marcados cuando sea demo.
- En paginas publicas, revisar title, description, headings, schema, Open Graph, performance y citabilidad IA.

Don't:
- Vender "IA magica".
- Usar placeholders en entrega.
- Ocultar precio/rango si la pieza es comercial.
- Usar bots o dashboards como decoracion sin funcion.
- Guardar secretos en el repo.
- Usar emojis decorativos, gradientes arcoiris, stock generico, popups invasivos o CTAs genericos.

## Responsive Behavior

Breakpoints de revision:
- 375px
- 768px
- 1024px
- 1440px

Reglas:
- Hero debe mantener CTA visible en mobile.
- Tabs deben caber o envolver sin romper.
- Cards deben pasar a una columna en mobile.
- Dashboard mobile prioriza lista por estado sobre tabla completa.
- Texto no debe solaparse ni salirse de botones.

## Agent Prompt Guide

Antes de disenar:
1. Identifica superficie, audiencia, objetivo y tono.
2. Usa este `DESIGN.md` como sistema activo.
3. Elige patron: landing, demo, dashboard, pricing, deck o carousel.
4. Para web premium, define tesis visual, sistema de color/tipo y tres momentos visuales clave.
5. Si necesitas una pieza visual reusable, evaluar Cult UI o shadcn antes de construir desde cero.
6. Para paginas indexables, aplicar `memory/claude-seo-iastudio.md` como preflight SEO/GEO.
7. Crea artefacto con CTA y flujo claro.
8. Revisa con la rubrica 5D y el quality gate de `memory/prompt-agente-web-premium-iastudio.md`.
9. No declares listo sin verificacion responsive, CTA, SEO basico y motion performance si hay animaciones.
