# Learn Skills IAStudio

> Adaptacion del repo `NeverSight/learn-skills.dev` para Saul IA Studios.

Fuente principal: https://github.com/NeverSight/learn-skills.dev

## Que es

`learn-skills.dev` es una app/catalogo para descubrir AI Agent Skills. Permite buscar, instalar, copiar y compartir skills compatibles con herramientas como Claude Code, Cursor, OpenClaw y otros agentes.

El repo funciona como crawler e indice:
- Toma rankings de proveedores como `skills.sh`.
- Mantiene listas all-time, trending y hot.
- Permite agregar skills manuales.
- Genera JSON/RSS/feed web.
- Cachea `SKILL.md` desde repos GitHub.

## Valor para IAStudio

Hasta ahora IAStudio viene integrando repos uno por uno. `learn-skills.dev` aporta una capa de descubrimiento:

- Buscar skills existentes antes de crear una propia.
- Separar skills populares de skills nuevas.
- Monitorear tendencias.
- Cachear `SKILL.md` para evaluacion offline.
- Crear una watchlist por necesidades de agencia.
- Evitar instalar skills solo por curiosidad.

## Piezas relevantes

### Fuentes

Actual:
- `skills.sh`: all-time, trending y hot.

Planeadas segun README:
- GitHub Trending.
- Awesome lists.

### Manual skills

Archivo:
- `data/manual_skills.json`

Uso:
- Registrar skills que ningun proveedor rastrea.
- Mantenerlas persistentes entre crawls.
- Deduplicar si despues aparecen en fuentes principales.

### Outputs

Archivos:
- `data/skills.json`: datos completos de leaderboards.
- `data/skills_index.json`: indice web-friendly.
- `data/feed.json`: top simplificado.
- `data/feed.xml`: RSS.
- `data/skills-md/`: cache de `SKILL.md`.

### Rutas comunes de SKILL.md

El crawler busca en rutas como:
- `skills/<skillId>/SKILL.md`
- `.claude/skills/<skillId>/SKILL.md`
- `.cursor/skills/<skillId>/SKILL.md`
- `.codex/skills/<skillId>/SKILL.md`
- `plugins/<plugin-name>/skills/<skillId>/SKILL.md`

Esto sirve para IAStudio cuando analiza repos nuevos: primero revisar estas rutas antes de concluir que no hay skill.

## Decision de adopcion

No instalar ni correr el crawler por ahora.

Motivos:
- Requiere Bun.
- Depende de red y fuentes externas.
- Puede necesitar `GITHUB_TOKEN` para evitar rate limits.
- La agencia aun esta definiendo su set base de skills.

Se adopta como:
- Radar de descubrimiento.
- Checklist de evaluacion.
- Watchlist de categorias.
- Fuente de inspiracion para futura biblioteca propia.

## Protocolo IAStudio para descubrir skills

Antes de crear una skill propia:

1. Definir problema.
2. Buscar skill existente por categoria.
3. Revisar `SKILL.md`, descripcion y dependencias.
4. Clasificar:
   - Adoptar.
   - Extender.
   - Referenciar.
   - Crear propia.
5. Evaluar seguridad y costo de contexto.
6. Probar en una tarea pequena.
7. Registrar resultado en `memory/habilidades.md`.

## Checklist de evaluacion

Para cada skill candidata:

- Fuente/repo confiable?
- Tiene `SKILL.md` claro?
- Tiene dependencias o scripts?
- Se puede usar sin credenciales?
- Toca archivos o es solo lectura?
- Tiene riesgo de guardar secretos?
- Solapa con una habilidad ya integrada?
- Aporta a venta, entrega, automatizacion, diseno, seguridad o datos?
- Tiene prueba pequena posible?
- Conviene instalar, copiar, resumir o solo observar?

## Reglas anti-ruido

- No instalar skills por moda.
- No duplicar habilidades ya cubiertas por Superpowers, ECC, Open Design o n8n-MCP.
- No usar rankings como criterio unico.
- No guardar tokens de GitHub ni APIs en memoria.
- Si una skill trae scripts, revisarlos antes de ejecutar.

## Que gana IAStudio

IAStudio gana una antena. En vez de depender solo de intuicion o repos sueltos, puede monitorear el ecosistema de skills, elegir mejores piezas y crear skills propias solo cuando valga la pena.
