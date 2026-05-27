# Cult UI IAStudio

> Adaptacion operativa de `nolly-studio/cult-ui` para Saul IA Studios.

## Fuente

- Repo: https://github.com/nolly-studio/cult-ui
- Docs: https://www.cult-ui.com/docs
- Instalacion: https://www.cult-ui.com/docs/installation
- MCP: https://www.cult-ui.com/docs/mcp-server
- Licencia: MIT

## Que es

Cult UI es un registry de componentes React/TypeScript para proyectos shadcn/ui. No se adopta como paquete npm monolitico: los componentes se distribuyen como codigo fuente para copiar o instalar via shadcn registry, de forma que el proyecto final conserva propiedad y control sobre lo que se entrega.

Su posicionamiento sirve a design engineers: piezas accesibles, customizables, motion-rich y compatibles con Tailwind/shadcn para crear interfaces menos genericas.

## Valor para IAStudio

Cult UI suma un banco de piezas visuales para elevar landings, demos, dashboards y artefactos de agencia sin inventar cada microinteraccion desde cero.

Uso recomendado:
- Landings de alto impacto: botones animados, cards con detalle, fondos medidos, heading/text effects.
- Demos por nicho: Dynamic Island, side panels, popovers, sortable lists, terminal animation o browser windows para mostrar flujo.
- Dashboards/CRM: tabs, toolbar expandable, code block, panels, vote/poll widgets cuando haya toma de decision.
- Artefactos IA: prompt library, AI instructions, terminal animation y patrones de AI SDK Agents como referencia para experiencias con agentes.

## Regla de adopcion

No pegar componentes por novedad visual. Cada pieza debe pasar esta pregunta:

`Ayuda a vender, explicar, demostrar confianza, reducir friccion o mejorar accion?`

Si la respuesta es no, no se usa.

## Flujo IAStudio

1. Definir superficie: landing, demo, dashboard, deck web o artefacto IA.
2. Elegir 1-3 componentes Cult UI maximo por pantalla.
3. Instalar/copy-source solo la pieza necesaria.
4. Adaptar tokens al `design-system/MASTER.md`: verde, neutros, radio 8px, claridad comercial.
5. Revisar dependencias reales antes de pegar codigo.
6. Validar responsive, focus, reduced motion y performance.
7. Documentar el componente usado en el entregable o SOP del cliente si queda como patron reusable.

## Instalacion segura

Para proyectos shadcn v3, se puede registrar Cult UI en `components.json`:

```json
{
  "registries": {
    "@cult-ui": "https://cult-ui.com/r/{name}.json"
  }
}
```

Ejemplos:

```bash
npx shadcn@beta add @cult-ui/text-gif
npx shadcn@beta add @cult-ui/texture-card @cult-ui/texture-button
npx shadcn@beta search @cult-ui --query "texture-button"
```

Si se usa MCP, configurar shadcn MCP en el proyecto y luego pedir busqueda/instalacion por lenguaje natural. No configurar MCP ni instalar componentes en proyectos de cliente sin revisar permisos, estructura y diff.

## Componentes a vigilar

Prioridad alta para IAStudio:
- Border Beam Button: CTA con senal visual sin caer en neon generico.
- Cutout Card: cards de caso, servicio o demo con imagen y accion.
- Grid Beam: fondo visual puntual para secciones hero/demo, con uso moderado.
- Terminal Animation: mostrar procesos de automatizacion, auditoria o setup.
- Dynamic Island: onboarding, notificaciones o demo de estado.
- Browser Window: presentar demos, captura CRM o flujo web.
- Sortable List: priorizacion de leads, tareas o pipeline.
- Prompt Library / AI Instructions: recursos para experiencias con agentes.
- Text Animate / Typewriter / Animated Number: metricas y copy dinamico con moderacion.

Evitar como default:
- Animaciones continuas sin proposito.
- Efectos de blur/filtro en superficies grandes.
- Multiplicar componentes premium en una sola pantalla.
- Romper el lenguaje sobrio/local de IAStudio con estetica demasiado gamer/futurista.

## Skills internas detectadas en el repo

El repo trae referencias muy valiosas para memoria:

- `.agents/skills/components-build/SKILL.md`: guia para crear componentes modernos, componibles, accesibles y tipados. Incluye 16 categorias: principios, composicion, accesibilidad, estado, tipos, polymorphism, as-child, data attributes, styling, tokens, docs, registry, npm y marketplaces.
- `.claude/skills/fixing-motion-performance/SKILL.md`: reglas para revisar performance de animaciones sin migrar librerias por capricho.

Adopcion IAStudio:
- Usar `components-build` como criterio para componentes propios: composicion antes que configuracion, accesibilidad por defecto, props tipadas, `cn()` y tokens.
- Usar `fixing-motion-performance` antes de entregar cualquier landing/demo con movimiento.

## Combinacion con memoria existente

- Con `ui-ux-pro-max`: Cult UI aporta piezas concretas; UI/UX Pro Max define criterio visual.
- Con `open-design`: Cult UI se usa dentro del pipeline brief -> DESIGN.md -> artefacto -> critica 5D.
- Con `grida`: Cult UI cubre interfaz; Grida cubre canvas/forms/data-first cuando se necesite.
- Con `learn-skills`: vigilar skills o registries similares antes de crear componentes propios.
- Con `claude-code-setup`: recomendar shadcn MCP o hooks de performance solo si el proyecto realmente usa React/Tailwind.

## Riesgos

- Dependencias de motion/Tailwind/shadcn pueden no calzar con proyectos estaticos simples.
- Componentes muy expresivos pueden bajar confianza si se usan en pymes locales sin criterio.
- Copy-source significa responsabilidad propia: si se pega codigo, IAStudio debe mantenerlo.
- Cult Pro y templates externos no se asumen disponibles; solo se registran como referencia.

## Que ganamos

IAStudio gana una biblioteca de patrones visuales listos para convertir interfaces genericas en demos vendibles, pero con una regla clara: adoptar poco, adaptar al sistema visual propio y verificar motion/performance antes de entregar.
