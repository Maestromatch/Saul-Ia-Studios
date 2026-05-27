# Remotion Skills IAStudio

> Adaptacion operativa de `remotion-dev/skills` para Saul IA Studios.

## Fuente

- Repo: https://github.com/remotion-dev/skills
- Skill principal: https://raw.githubusercontent.com/remotion-dev/skills/main/skills/remotion/SKILL.md
- Package: https://raw.githubusercontent.com/remotion-dev/skills/main/package.json
- Skill local disponible: `C:\Users\Usuario 01\.codex\skills\remotion\SKILL.md`
- Fecha de lectura: 2026-05-22

## Que es

`remotion-dev/skills` es un paquete interno del equipo Remotion con una skill de buenas practicas para crear video programatico con React. El README publico es minimo, pero la skill `remotion-best-practices` concentra reglas operativas para animacion por frames, composiciones, assets, captions, audio, 3D, mapas, Lottie, GIFs, transiciones, voiceover y parametros.

Para IAStudio se adopta como protocolo de produccion de video, no como instalacion automatica.

## Valor para IAStudio

IAStudio gana una linea nueva de entregables reproducibles:

- videos demo de servicios,
- clips verticales para ads,
- explicadores de "landing -> WhatsApp -> CRM -> follow-up",
- videos de caso antes/despues,
- dashboard-to-video para reportes,
- reels con metricas y captions,
- intros/outros de marca,
- plantillas parametrizables para multiples nichos.

La ventaja clave: un video Remotion es codigo. Se puede versionar, parametrizar, ajustar por cliente y volver a renderizar sin rehacer todo en un editor manual.

## Reglas Remotion que IAStudio adopta

### Animacion por frames

- Usar `useCurrentFrame()` y `useVideoConfig()`.
- Usar `interpolate()` con rangos explicitos.
- Usar `Easing.bezier()` para timing premium.
- Separar timing de mapping: crear progreso normalizado y derivar opacidad, posicion, escala, etc.
- Clampear interpolaciones con `extrapolateLeft` y `extrapolateRight` cuando corresponda.

### Prohibido en Remotion

- No usar CSS transitions.
- No usar CSS animations.
- No usar clases Tailwind de animacion.
- No depender de timers reales; todo debe derivar del frame.

### Assets

- Poner assets en `public/`.
- Referenciar assets con `staticFile()`.
- Usar `Img` para imagenes.
- Usar `Video` y `Audio` desde `@remotion/media` cuando aplique.
- Validar licencias de imagenes, musica, SFX y fuentes antes de entregar.

### Composiciones

- Definir width, height, fps y duration en `src/Root.tsx`.
- Usar `Sequence` para ordenar escenas.
- Usar `durationInFrames` para limitar cada pieza.
- Usar `layout="none"` cuando el contenido no deba ser absolute fill.
- Usar `calculateMetadata` cuando la duracion dependa de datos, audio o props.

### Verificacion

- Usar Remotion Studio para preview cuando se implemente video.
- Hacer render still de un frame cuando haya duda visual:

```bash
npx remotion still [composition-id] --scale=0.25 --frame=30
```

- Para video final, revisar al menos: primer frame, corte intermedio, frame final, audio, captions, safe area y legibilidad mobile.

## Casos IAStudio

### Video demo de servicio

Formato:
- 1080x1920 para reels/stories.
- 1080x1080 para feed.
- 1920x1080 para presentacion o landing.

Estructura:
- Hook de dolor.
- Promesa visual.
- Demo del flujo.
- Prueba o metrica.
- CTA a WhatsApp/reunion.

### Dashboard-to-video

Uso:
- reporte de campana,
- resumen de leads,
- health check de bot,
- antes/despues de automatizacion.

Regla:
- mostrar pocos datos, con jerarquia y narracion clara.
- cada metrica debe explicar decision o resultado.

### Video con voiceover

Si se usa TTS:
- guardar audio generado en `public/voiceover/...`,
- calcular duracion con `calculateMetadata`,
- no guardar API keys en repo o memoria,
- pedir proveedor/voz solo si no existe decision previa.

### Captions

- Captions en JSON con campos: text, startMs, endMs, timestampMs, confidence.
- No quemar subtitulos sin revisar legibilidad.
- Usar contraste alto y area segura.

### Plantillas parametrizables

Usar Zod schema para props editables:
- cliente,
- nicho,
- oferta,
- colores,
- metricas,
- CTA,
- escenas activas,
- assets.

Esto permite reutilizar la misma composicion para opticas, constructoras, servicios tecnicos u otros nichos.

## Pipeline IAStudio

1. Brief: objetivo, formato, duracion, audiencia, CTA, assets, voz/audio.
2. Guion: escenas, texto en pantalla, ritmo, metricas.
3. Storyboard: frames clave y transiciones.
4. Implementacion Remotion: composicion, props, assets, audio/captions.
5. Preview: Remotion Studio.
6. Check still: frame 0, frame medio, frame final.
7. Render final.
8. QA: audio, captions, safe areas, legibilidad, duracion, CTA.
9. Export/handoff: MP4/WebM/GIF/still segun canal.

## Combinacion con memoria existente

- Con `prompt-agente-web-premium`: eleva la direccion visual y evita plantillas.
- Con `cult-ui`: inspira UI panels, browser windows y dashboard cards que luego pueden animarse en Remotion.
- Con `claude-seo`: videos pueden producir OG assets, hero videos o explicadores sin romper performance si se usan bien.
- Con `agency-agents`: activar Creative Director, Motion Designer, Frontend Developer, Performance Benchmarker, Evidence Collector y Reality Checker.
- Con `open-design`: usar brief -> DESIGN.md -> storyboard -> artefacto -> critica 5D.
- Con `n8n-mcp`: videos pueden explicar automatizaciones y workflows al cliente.

## Riesgos

- Render de video puede ser pesado en dependencias y tiempo.
- Videos grandes pueden afectar LCP si se incrustan mal en landing.
- Audio, voces, musica y SFX tienen licencias y permisos.
- TTS requiere credenciales: no guardar API keys.
- Datos de cliente en videos deben revisarse antes de publicar.
- Motion excesivo puede verse premium pero distraer del mensaje.

## Decision IAStudio

No instalar Remotion ni crear proyecto ahora. Se adopta como protocolo y se usara cuando haya una necesidad real de video programatico.

## Que ganamos

IAStudio gana una fabrica de video reproducible: anuncios, demos, reportes y explicadores pueden salir desde codigo, con assets parametrizados y calidad consistente con el design-system.
