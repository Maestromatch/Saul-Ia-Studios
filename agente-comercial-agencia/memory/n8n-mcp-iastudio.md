# n8n-MCP IAStudio

> Adaptacion del repo `czlonkowski/n8n-mcp` para Saul IA Studios.

Fuente principal: https://github.com/czlonkowski/n8n-mcp

## Que es

`n8n-mcp` es un servidor MCP que conecta asistentes IA con el ecosistema n8n. Entrega documentacion de nodos, propiedades, operaciones, ejemplos reales, templates y herramientas de validacion. Tambien puede gestionar workflows en una instancia n8n si se configura `N8N_API_URL` y `N8N_API_KEY`.

Version revisada:
- Repo: `czlonkowski/n8n-mcp`
- Paquete: `n8n-mcp`
- Version: `2.54.0`
- Licencia: MIT
- Stack: TypeScript, Node.js, MCP SDK, Express, Docker, n8n packages.

## Valor para IAStudio

IAStudio usa n8n como motor de automatizaciones. Esta herramienta reduce el riesgo de crear flujos rotos porque permite:

- Buscar templates antes de construir.
- Buscar nodos y ejemplos reales.
- Leer propiedades obligatorias de cada nodo.
- Validar nodos antes de armar el workflow.
- Validar conexiones, expresiones y estructura completa.
- Gestionar workflows via API si se configura con permisos.
- Auditar una instancia n8n y revisar ejecuciones.

## Decision de adopcion

No se instala ni conecta todavia.

Se adopta primero como SOP:
- Disenar con templates/documentacion.
- Configurar parametros explicitamente.
- Validar por niveles.
- Probar fuera de produccion.
- Solo conectar API cuando exista ambiente seguro.

## Clasificacion ECC

- Adoptar: workflow de validacion y regla templates first.
- Extender: checklist n8n propio para entregas IAStudio.
- Componer: combinar con Superpowers para spec/plan y con Claude-Mem para registrar aprendizajes.
- Construir: workflows propios de agencia sobre esta disciplina.

## Protocolo IAStudio para workflows n8n

### 1. Preparar antes de construir

Definir:
- Objetivo del workflow.
- Trigger.
- Datos de entrada.
- Datos de salida.
- Credenciales necesarias.
- Sistemas conectados.
- Error esperado y fallback humano.
- Ambiente: demo, desarrollo o produccion.

### 2. Templates first

Antes de crear desde cero:
- Buscar template por tarea.
- Buscar template por nodos.
- Buscar template por servicio requerido.
- Si se usa un template, registrar atribucion y validar porque puede estar desactualizado.

### 3. Node discovery

Para cada nodo:
- Buscar nodo correcto.
- Pedir ejemplos cuando existan.
- Revisar propiedades esenciales.
- Revisar autenticacion.
- Revisar expresiones.
- Evitar Code node si un nodo estandar resuelve el caso.

### 4. Never trust defaults

Regla:
- No confiar en valores por defecto si controlan comportamiento.
- Configurar explicitamente resource, operation, selectores, IDs, URLs, campos requeridos, headers, branches y outputs.

Aplicacion IAStudio:
- WhatsApp.
- Google Sheets.
- Supabase.
- HTTP Request.
- OpenAI/LangChain.
- Webhook.
- IF/Switch.
- Respond to Webhook.

### 5. Validacion multinivel

Antes de entregar:

1. Validar cada nodo en modo minimo.
2. Validar cada nodo en modo completo con perfil runtime.
3. Validar workflow completo.
4. Validar conexiones y expresiones.
5. Si esta desplegado, validar workflow por ID.
6. Ejecutar prueba real o mock.
7. Revisar ejecuciones y errores.

### 6. No produccion directo

Reglas:
- Nunca editar workflow productivo directo con IA.
- Crear copia antes de cambios.
- Exportar backup JSON.
- Probar en ambiente de desarrollo.
- Validar antes de activar.
- Mantener rollback.

### 7. Batch updates

Si se usa gestion via API:
- Preferir operaciones batch en `n8n_update_partial_workflow`.
- Evitar muchas llamadas separadas.
- Para conexiones, usar `source`, `target`, `sourcePort`, `targetPort`.
- En IF nodes, indicar branch `true` o `false`.

## Configuracion segura recomendada

### Modo documentacion primero

Usar sin `N8N_API_KEY` cuando solo se necesita:
- Buscar nodos.
- Leer documentacion.
- Validar JSON de workflow.
- Disenar arquitectura.

### Modo gestion n8n

Usar solo si hay:
- Ambiente de desarrollo.
- API key controlada.
- Backup exportado.
- Token fuerte.
- Herramientas peligrosas deshabilitadas si no se necesitan.
- Telemetria evaluada/desactivada si corresponde.

Variables relevantes:
- `N8N_API_URL`
- `N8N_API_KEY`
- `AUTH_TOKEN`
- `MCP_AUTH_TOKEN`
- `DISABLED_TOOLS`
- `WEBHOOK_SECURITY_MODE`
- `N8N_MCP_TELEMETRY_DISABLED=true`

## Riesgos

- Quien tenga acceso al MCP con API key tiene poderes similares a esa API key de n8n.
- Workflows pueden incluir Code nodes con impacto real.
- Datos de workflow o ejecuciones pueden contener informacion sensible.
- Prompt injection puede venir desde nombres, descripciones o outputs de workflows.
- Defaults pueden romper ejecuciones aunque la estructura parezca correcta.

## Checklist de entrega n8n IAStudio

- Workflow exportado como backup.
- Ambiente de prueba usado antes de produccion.
- Credenciales fuera del repo.
- Nodos con parametros explicitos.
- IF/Switch con branches correctos.
- HTTP nodes con timeout y manejo de error.
- Webhooks con respuesta clara.
- CRM/Sheet/Supabase probado con lead ficticio.
- Handoff humano probado.
- Error path probado.
- Execution log revisado.
- Cliente recibe explicacion simple, no jerga tecnica.

## Aplicacion inmediata

Workflow candidato:
- Lead capturado por landing o WhatsApp.
- Validar datos minimos.
- Registrar en CRM.
- Enviar alerta interna.
- Agendar o pedir dato faltante.
- Crear follow-up automatico.
- Registrar estado.

## Que gana IAStudio

IAStudio gana una forma profesional de construir automatizaciones: menos prueba/error, menos workflows rotos, mas validacion, mas seguridad y entregas mas confiables para clientes.
