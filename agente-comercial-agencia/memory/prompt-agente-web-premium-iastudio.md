# Prompt Agente Web Premium IAStudio

> Adaptacion del archivo local `prompt-agente-web-premium.txt` como protocolo de propuestas web premium para Saul IA Studios.

## Fuente

- Archivo local: `C:\Users\Usuario 01\Documents\Downloads\prompt-agente-web-premium.txt`
- Autor declarado en el texto: Aetria Studio
- Fecha de lectura: 2026-05-21
- Tipo: prompt system / estandar web premium / quality gate visual.

## Que es

El texto define un agente de propuestas web premium: Senior Product Designer + Frontend Engineer, orientado a landing pages, SaaS y product sites de alto nivel. Su foco no es producir una pagina mas, sino elevar la propuesta con sistema visual explicito, jerarquia cinematografica, interacciones vivas, performance, accesibilidad y autocritica antes de entregar.

Para IAStudio se adopta como protocolo de calidad, no como prompt literal. La razon: algunas reglas del texto piden detenerse por aprobacion antes de codear; en este entorno, cuando el usuario ya pide implementar, se avanza con criterio y se pregunta solo si falta informacion critica.

## Valor para IAStudio

Este prompt suma una vara mas alta para propuestas web:

- Convierte "hacer una landing" en un proceso de diagnostico, tesis visual, wireframe, implementacion y autocritica.
- Obliga a definir tokens, tipografia, color, spacing, efectos e iconografia.
- Evita resultados genericos tipo template.
- Refuerza performance, accesibilidad y responsive como parte del diseno.
- Suma un formato de entrega claro para propuestas conceptuales o codigo.

## Protocolo IAStudio

Usar cuando el trabajo sea:

- Landing premium.
- Product site.
- SaaS demo.
- Web de agencia.
- Propuesta visual para cliente.
- Redisenos de `index.html`, demos o paginas comerciales.
- Auditoria visual de una pieza web.

### Paso 1 - Diagnostico

Confirmar, o inferir desde contexto si ya existe:

- Que vende.
- Quien compra.
- Ticket o nivel de sofisticacion.
- Referencias visuales.
- Marca/identidad existente.
- Stack tecnico.
- Restricciones.
- Metrica principal: leads, demos, ventas, signups, WhatsApp o reservas.

Si falta informacion critica y no se puede inferir sin riesgo, preguntar.

### Paso 2 - Tesis visual

Antes de implementar cambios grandes, definir mentalmente o documentar:

- Diferenciacion visual.
- Sistema de color.
- Sistema tipografico.
- Tres momentos visuales clave.
- Que no se va a hacer para evitar cliche.

### Paso 3 - Wireframe en prosa

Para piezas nuevas, listar secciones:

- Hero.
- Prueba o demo.
- Problema.
- Oferta.
- Proceso.
- Casos/credibilidad.
- FAQ.
- CTA final.

Cada seccion debe tener contenido y tratamiento visual, no solo nombre.

### Paso 4 - Implementacion

Reglas base:

- HTML semantico.
- CSS con variables semanticas.
- Mobile-first.
- JS vanilla salvo que el proyecto ya use framework.
- Dependencias solo si aportan valor claro.
- Comentarios escasos y utiles.
- Sin placeholders en entrega final.

### Paso 5 - Autocritica premium

Antes de cerrar, revisar:

- Sistema de diseno explicito.
- Jerarquia visual fuerte.
- Efectos con proposito.
- Interacciones vivas sin ruido.
- Tipografia cuidada.
- Iconografia consistente.
- Responsive/performance.
- Accesibilidad.
- Prohibiciones del prompt.

Si falla algo importante, corregir antes de declarar listo.

## Quality gate premium

### Sistema de diseno

- Variables CSS semanticas.
- Paleta limitada.
- Maximo dos familias tipograficas, salvo serif de acento muy justificada.
- Escala con `clamp()` cuando aplique.
- Spacing consistente, idealmente escala 4px/8px.

### Jerarquia visual

- Un heroe visual por seccion.
- Mucho aire negativo.
- Titulos con `text-wrap: balance`.
- Parrafos con `text-wrap: pretty` cuando soporte sea aceptable.
- Contraste claro entre display, h2, body y meta.

### Efectos permitidos con proposito

- Glow radial sutil.
- Grain noise muy bajo.
- Border gradient en cards especiales.
- Sombra multi-capa con criterio.
- Backdrop blur moderado.
- Cursor blob solo si aporta al hero y no afecta performance.
- Conectores SVG animados.
- Reveal on scroll liviano con IntersectionObserver.
- Perspectiva 3D sutil en mockups.

### Interacciones vivas

- Dots online, timestamps, metricas, estados de UI o contadores si comunican producto.
- Hover suave, 200-400ms.
- Microcopy para loading, success y empty states.
- No animar por decorar.

### Performance y accesibilidad

- Mobile-first.
- LCP objetivo menor a 2s en mobile 4G si hay medicion.
- CLS menor a 0.1.
- Lazy-load de imagenes.
- Maximo dos weights por familia.
- SVG inline para iconos pequenos cuando aplique.
- Contraste AA minimo.
- `focus-visible`.
- `prefers-reduced-motion`.
- Semantica HTML correcta.
- Heading levels sin saltos.

## Prohibiciones adoptadas

- Emojis decorativos sueltos.
- Gradientes arcoiris o multicolor sin identidad.
- Cards con borde de acento solo a la izquierda como cliche AI.
- Feature blobs genericos.
- Stock photos genericas.
- Lorem ipsum en propuestas finales.
- Glassmorphism abusado.
- Neumorfismo.
- Corporate Memphis.
- Animaciones no pausables.
- Auto-play con sonido.
- Popups invasivos.
- CTAs genericos como "click here", "learn more" o "buy now".
- Tailwind sin tokens o theme custom cuando sea proyecto Tailwind.

## Adaptacion a IAStudio

IAStudio no debe copiar la estetica de Vercel/Linear/Stripe sin criterio. La inspiracion se traduce asi:

- Linear: sistema, limpieza, microinteraccion.
- Vercel: densidad tecnica elegante.
- Anthropic: serenidad editorial.
- Stripe: claridad tecnica y profundidad.
- Arc/Framer: storytelling y motion con proposito.
- Resend/Cal: producto y landing fusionados.

Para pymes locales, la vara premium debe sentirse confiable y concreta, no fria o inaccesible.

## Formato de entrega

Para codigo:

1. Resumen ejecutivo.
2. Tesis visual.
3. Tokens principales.
4. Codigo o archivos modificados.
5. Verificacion y siguiente iteracion.

Para propuesta conceptual:

1. Diagnostico.
2. Tesis.
3. Moodboard verbal.
4. Wireframe en prosa.
5. Preguntas pendientes.

## Combinacion con memoria existente

- Con `ui-ux-pro-max`: define criterio premium y prohibiciones.
- Con `open-design`: encaja como quality gate dentro de brief -> DESIGN.md -> artefacto -> critica.
- Con `cult-ui`: ayuda a elegir componentes expresivos sin caer en exceso.
- Con `agency-agents`: activa UI Designer, UX Architect, Frontend Developer, Accessibility Auditor, Performance Benchmarker y Reality Checker.
- Con `ecc`: refuerza verification loop antes de cierre.

## Que ganamos

IAStudio gana una vara premium para sitios y propuestas web: menos plantilla, mas sistema; menos decoracion, mas intencion; menos "se ve bonito", mas evidencia de calidad visual, tecnica y comercial.
