# UI UX Pro Max IAStudio

> Adaptacion del repo `nextlevelbuilder/ui-ux-pro-max-skill` para Saul IA Studios.

Fuente principal: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

## Que es

`ui-ux-pro-max-skill` es una skill de inteligencia UI/UX para generar y revisar sistemas visuales. Su repositorio declara 67 estilos UI, 161 paletas, 57 combinaciones tipograficas, 99 guias UX, 25 tipos de charts y soporte para 15+ stacks. Tambien propone un flujo de design system con `MASTER.md` y overrides por pagina.

## Por que importa para IAStudio

IAStudio vende sistemas IA a pymes. La interfaz no es decoracion: es confianza. Una landing, demo o dashboard mal presentado baja conversion aunque el bot funcione.

Esta integracion nos da:
- Criterio visual repetible.
- Checklists antes de entregar.
- Un sistema base para no reinventar estilos.
- Estructura para demos de nicho.
- Mejor forma de mostrar valor en CRM y dashboards.

## Decision de adopcion

No se instala `uipro-cli` por ahora. Se adopta de forma documental y operativa:

- `design-system/MASTER.md` como fuente visual base de Saul IA Studios.
- `design-system/pages/` como overrides por tipo de pagina.
- `memory/habilidades.md` para registrar capacidades.
- `memory/evolucion.md` para registrar cambios estrategicos.

## Clasificacion ECC

- Adoptar: patron `MASTER.md` + overrides por pagina.
- Extender: checklist UI/UX adaptado a landings, demos y dashboards IAStudio.
- Componer: usar junto a Superpowers para planificar y verificar entregas.
- Construir: crear nuestra propia version de design system local, sin instalar la CLI aun.

## Uso recomendado

### Antes de crear una landing

1. Leer `design-system/MASTER.md`.
2. Leer override de pagina si existe.
3. Definir objetivo: confianza, conversion, demo, agenda o educacion.
4. Seleccionar patron:
   - `Conversion-Optimized` para captacion.
   - `Trust & Authority` para servicios B2B.
   - `Interactive Product Demo` para demos de bots.
   - `Social Proof-Focused` cuando exista caso/testimonio.
5. Crear UI y copy con CTA WhatsApp claro.

### Antes de crear una demo de nicho

1. Problema visible en primer viewport.
2. Panel interactivo o conversacion que demuestre el sistema.
3. Casos reales del nicho.
4. CRM/follow-up visible como prueba de valor.
5. CTA directo a piloto o diagnostico.

### Antes de crear dashboard o CRM

1. Priorizar escaneo rapido.
2. Mostrar estados, urgencia, proximo paso y valor recuperado.
3. Evitar decoracion innecesaria.
4. Usar tablas, chips, filtros y metricas compactas.
5. Revisar que el cliente entienda el valor en menos de 10 segundos.

## Checklist UI/UX IAStudio

Antes de entregar:

- CTA principal visible y accionable.
- WhatsApp abre con mensaje prellenado correcto.
- Responsive revisado en 375, 768, 1024 y 1440px.
- Contraste minimo AA en textos principales.
- Botones con hover/focus.
- Elementos clickeables con cursor y area suficiente.
- Sin placeholders ni datos falsos no marcados.
- Sin emojis como iconos principales; usar texto, CSS o iconos reales cuando aplique.
- Animaciones suaves y respetuosas.
- Sin gradientes genericos tipo "AI purple" salvo que el proyecto lo justifique.
- Textos no se solapan ni rompen botones.
- La primera pantalla comunica marca, problema, solucion y siguiente accion.

## Aplicacion por activos actuales

### Landing agencia

Archivo: `index.html`

Patron recomendado:
- Conversion-Optimized + Trust & Authority.

Estilo:
- Minimalismo operativo.
- Swiss/enterprise local.
- Paneles de sistema.
- Verde confianza + neutros claros.

Objetivo:
- Diagnostico por WhatsApp.
- Explicar sistema completo sin vender piezas sueltas.

### Demo opticas

Archivo: `demo-opticas.html`

Patron recomendado:
- Interactive Product Demo + Social Proof-Focused cuando exista caso real.

Objetivo:
- Mostrar que el bot responde, agenda, captura datos y deriva.
- Convertir a piloto.

Nota:
- Revisar caracteres especiales/encoding antes de usar como pieza comercial final.

### Dashboard CRM futuro

Patron recomendado:
- Sales Intelligence Dashboard.
- Real-Time Monitoring si hay bot/WhatsApp activo.

Objetivo:
- Mostrar leads por estado, proximo paso, fuente, tiempo de respuesta y oportunidades recuperadas.

## Que ganamos

Ganamos una capa de criterio visual para que cada entrega de IAStudio parezca sistema profesional y no maqueta improvisada. Esto aumenta confianza, reduce retrabajo y hace que las demos vendan mejor.
