# Design System Master - Saul IA Studios

> Fuente visual base para landing, demos, dashboards y recursos frontend de IAStudio.

Inspirado por `nextlevelbuilder/ui-ux-pro-max-skill` y adaptado al estilo actual de `index.html` / `style.css`.

## Principio

IAStudio debe sentirse como un sistema operativo comercial para pymes: claro, confiable, directo y medible.

La interfaz no debe parecer una landing generica de IA. Debe comunicar:
- negocio real
- WhatsApp
- CRM
- seguimiento
- datos
- entrega responsable

## Personalidad visual

- Sobria, cercana y profesional.
- Mas "sistema instalado" que "startup futurista".
- Mas confianza local que lujo aspiracional.
- Mas claridad operativa que decoracion.

## Patrones base

### Landing principal

- Patron: `Conversion-Optimized` + `Trust & Authority`.
- Primer viewport: marca, problema, promesa, CTA WhatsApp y una visual del sistema.
- Secciones: problema, caminos de entrada, servicios, caso/demo, proceso, confianza, FAQ, CTA final.

### Demos por nicho

- Patron: `Interactive Product Demo`.
- Primer viewport: dolor del nicho + panel demo.
- Mostrar 3-4 casos reales.
- Mostrar captura de datos y proximo paso.
- CTA: piloto o diagnostico.

### Dashboards / CRM

- Patron: `Sales Intelligence Dashboard`.
- Debe priorizar estados, urgencia, proximo paso y valor recuperado.
- Nada de graficos decorativos si no ayudan a decidir.

### Propuestas web premium

- Antes de disenar, definir tesis visual: diferenciacion, color, tipografia y tres momentos memorables.
- Cada seccion debe tener un heroe visual claro, no varios elementos compitiendo.
- Mucho aire negativo. Si la pieza se siente comprimida, abrir espacio antes de decorar.
- El resultado debe sentirse propio del cliente, no plantilla generica.

## Color

Base actual:

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

Uso:
- `--accent` para CTA principal, estados positivos y rutas de avance.
- `--signal` para alerta suave, oportunidad o destaque medido.
- `--ink` para texto fuerte.
- `--muted` para descripcion, metadatos y labels.
- `--paper`, `--surface`, `--soft` para fondos y paneles.

Evitar:
- Gradientes morados genericos de IA.
- Paletas de un solo color sin contraste.
- Fondos oscuros pesados para piezas de venta local.
- Colores neon sin justificacion.

## Tipografia

Fuente base:
- Inter / system-ui.

Uso:
- H1 grandes solo en hero.
- Titulares compactos dentro de cards, paneles y dashboards.
- No usar letter spacing negativo.
- No escalar fuente con viewport width.
- Priorizar legibilidad movil.
- En propuestas premium, usar escala con `clamp()` y `text-wrap: balance` para titulares cuando aplique.

## Componentes

### Botones

- Radio: 8px.
- Alto minimo: 44-46px.
- Texto claro y accionable.
- CTA principal en verde.
- Secundario blanco o neutro.
- Hover/focus visibles.

### Cards y paneles

- Radio: 8px.
- Usar cards para items repetidos, demos, paneles o modales.
- No meter cards dentro de cards.
- Paneles de sistema deben mostrar informacion concreta, no decoracion.

### Tabs de demo

- Botones compactos.
- Estado activo claro.
- Deben funcionar con teclado cuando sea posible.
- El contenido no debe cambiar el layout de forma brusca.

### CRM rows / chips

- Mostrar estado y proximo paso.
- Usar chips para etapa: nuevo, calificado, agendar, cotizado, seguimiento, cerrado.
- Evitar chips excesivos que parezcan etiquetas sin accion.

### Componentes Cult UI / shadcn

- Usar Cult UI como banco selectivo de componentes, no como estilo visual completo.
- Maximo 1-3 piezas expresivas por pantalla.
- Adaptar tokens, radios, copy y estados al sistema IAStudio.
- Priorizar piezas que expliquen flujo: browser window, terminal animation, dynamic island, cutout card, sortable list, prompt library o botones con senal.
- Si el componente requiere shadcn registry, revisar dependencias y diff antes de integrarlo.
- No usar componentes motion-rich si distraen del CTA, bajan performance o vuelven la pagina demasiado futurista.

## Movimiento

- Transiciones 150-300ms.
- Hover sutil.
- Respetar `prefers-reduced-motion` si se agregan animaciones fuertes.
- Evitar animaciones que distraigan del CTA o de la demo.
- Animar preferentemente `transform` y `opacity`.
- Evitar blur/filtros continuos o animaciones de layout en superficies grandes.
- Todo efecto debe tener proposito: explicar producto, guiar atencion, demostrar sistema o reforzar confianza.

## Accesibilidad

- Contraste AA en textos relevantes.
- Focus visible.
- Links y botones con area tactil suficiente.
- Texto no debe solaparse ni cortarse.
- Formularios con labels reales.
- No depender solo de color para comunicar estado.

## Checklist de entrega

Antes de cerrar una pieza frontend:

- Revisar 375px.
- Revisar 768px.
- Revisar 1024px.
- Revisar 1440px.
- Probar CTA WhatsApp.
- Revisar focus/hover en botones.
- Revisar que no haya placeholders.
- Revisar que la primera pantalla tenga marca, promesa y accion.
- Revisar ortografia y caracteres especiales.
- Revisar que cada seccion tenga razon comercial.
- Revisar que haya tokens semanticos, jerarquia visual, focus visible, reduced motion y microcopy de estados si hay interaccion.
- Revisar que no haya cliches: emojis decorativos, stock generico, glassmorphism abusado, popups invasivos, CTAs genericos o gradientes sin identidad.

## Regla de oro

Si un elemento no ayuda a vender, explicar, demostrar confianza o permitir accion, se elimina.
