# Claude-Mem IAStudio

> Adaptacion manual del repo `thedotmack/claude-mem` para la memoria de Saul IA Studios.

Fuente principal: https://github.com/thedotmack/claude-mem

## Que es

`claude-mem` es un sistema de memoria persistente para agentes. Captura actividad de sesiones, la comprime en observaciones, la guarda en una base local y permite recuperar contexto en sesiones futuras mediante busqueda por capas.

La version revisada declara:
- Paquete: `claude-mem`
- Version: `13.2.0`
- Licencia: Apache-2.0
- Plugin Codex: `claude-mem`
- Stack: TypeScript, Node.js, Bun, Express, React, SQLite/FTS5, Chroma opcional, MCP, hooks.

## Decision de adopcion

No se instala completo por ahora.

Motivos:
- Activa hooks y worker local.
- Guarda observaciones de sesiones en una base persistente.
- Puede capturar informacion sensible si no se usa con disciplina.
- Requiere Node/Bun/uv y servicios de fondo.

Se adopta como arquitectura manual:
- Indice ligero.
- IDs de observaciones.
- Recuperacion por capas.
- Politica anti-secretos.
- Contexto por carpeta solo cuando sea necesario.

## Modelo adoptado

### Capa 1 - Indice

Archivo:
- `memory/observations-index.md`

Uso:
- Revisar IDs, titulo, tipo, scope, fuente y archivo de detalle.
- No abrir archivos largos hasta saber que ID importa.

### Capa 2 - Timeline

Archivo:
- `memory/evolucion.md`

Uso:
- Entender secuencia de decisiones.
- Ver que cambio en la agencia y que queda pendiente.

### Capa 3 - Detalle

Archivos:
- `memory/repos-github.md`
- `memory/habilidades.md`
- `memory/*.md`
- `design-system/*.md`
- Carpetas de cliente cuando aplique.

Uso:
- Abrir solo el detalle relacionado con IDs relevantes.

## Formato de observacion IAStudio

```markdown
| ID | Fecha | Tipo | Scope | Titulo | Fuente | Detalle | Leer |
| --- | --- | --- | --- | --- | --- | --- | --- |
| OBS-YYYYMMDD-001 | YYYY-MM-DD | decision / skill / recurso / riesgo | agencia / nicho / cliente / global | Titulo corto | repo/documento | archivo.md | ~tokens |
```

Tipos recomendados:
- `decision`
- `skill`
- `recurso`
- `riesgo`
- `protocolo`
- `diseno`
- `seguridad`
- `venta`
- `entrega`

Scopes:
- `cliente`
- `nicho`
- `agencia`
- `global`

## Politica anti-secretos

Nunca guardar en `memory/`:
- API keys.
- Tokens.
- Passwords.
- Credenciales de Meta, Vercel, Supabase, n8n o correo.
- Telefonos personales de clientes sin necesidad operativa.
- Datos sensibles de prospectos.
- Logs completos con datos privados.
- Contexto temporal que no deba quedar como decision.

Si algo es necesario para una sesion pero no debe persistir:
- Marcarlo como privado en la conversacion.
- Resumirlo sin valores reales.
- Guardar solo el aprendizaje general.

Ejemplo:

```markdown
No guardar: SUPABASE_SERVICE_ROLE=...
Guardar: el proyecto requiere configurar `SUPABASE_SERVICE_ROLE` como secreto de entorno en Vercel, nunca hardcodeado.
```

## Regla de uso en sesiones futuras

Antes de trabajar:
1. Abrir `memory/observations-index.md`.
2. Identificar 1-3 IDs relevantes.
3. Abrir solo los detalles necesarios.
4. Al terminar, registrar nueva observacion si hubo aprendizaje, decision o recurso reusable.

## Contexto por carpeta

`claude-mem` puede generar `CLAUDE.md` por carpeta con actividad reciente. Para IAStudio no se activa automaticamente.

Regla local:
- Usar notas por carpeta solo si el proyecto crece y ayuda a entregar.
- No generar `CLAUDE.md` automaticos en subcarpetas.
- No ensuciar Git con contexto cambiante.
- Mantener la memoria principal en `memory/`.

## Como se combina con lo anterior

- Superpowers: ejecuta tareas con spec, plan, pruebas y verificacion.
- ECC: organiza operaciones, seguridad y scopes.
- UI UX Pro Max: da criterio visual y checklist UI/UX.
- Claude-Mem: organiza memoria por capas e IDs.

## Que gana IAStudio

IAStudio gana memoria recuperable. No dependemos de recordar conversaciones completas: podemos buscar por ID, abrir solo lo necesario y mantener continuidad sin contaminar el contexto.
