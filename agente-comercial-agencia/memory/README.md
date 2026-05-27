# Memoria operativa - Saul IA Studios

Esta carpeta guarda la memoria persistente para que el agente de este chat pueda evolucionar la agencia con cada repo, guia o aprendizaje nuevo.

## Como usar esta memoria

Cuando el usuario entregue un repositorio de GitHub:

1. Registrar el repo en `repos-github.md`.
2. Leer su README, estructura, stack y piezas reutilizables.
3. Extraer habilidades utiles hacia `habilidades.md`.
4. Registrar cambios, decisiones y aprendizajes en `evolucion.md`.
5. Si el repo trae codigo, plantillas o automatizaciones copiables, proponer donde integrarlas dentro de `IAStudio_Lanzamiento`.

Cuando el usuario entregue un texto, prompt o documento local:

1. Registrar la fuente en `fuentes-internas.md`.
2. Extraer reglas, checklist, formato de salida y criterio reusable.
3. Crear una ficha de memoria especifica si aporta una capacidad nueva.
4. Actualizar `habilidades.md`, `evolucion.md` y `observations-index.md`.
5. Adaptar el contenido a IAStudio sin copiar mecanicamente instrucciones que choquen con el flujo real.

Cuando el usuario entregue una carpeta Google Drive:

1. Intentar abrir el enlace.
2. Si no lista archivos, registrar en `fuentes-drive.md` como pendiente.
3. No integrar contenido no leido.
4. Pedir acceso publico, ZIP local o archivos individuales.
5. Cuando haya acceso, procesar cada archivo como fuente interna o externa segun corresponda.

## Criterio de integracion

- No copiar por copiar: transformar cada repo en oferta, SOP, demo, plantilla, prompt, stack o check reutilizable.
- Priorizar lo que ayude a vender, entregar mejor o reducir trabajo manual.
- Mantener trazabilidad: cada habilidad nueva debe apuntar al repo o archivo que la inspiro.
- Cuidar datos sensibles: nunca guardar tokens, credenciales, secretos ni informacion privada de clientes.

## Archivos

- `repos-github.md`: bitacora de repos recibidos y estado de integracion.
- `habilidades.md`: capacidades internas que el agente puede aplicar.
- `evolucion.md`: decisiones, cambios de estrategia y aprendizaje acumulado.
- `reference_tips_iastudio.md`: indice de los tips propios existentes.
- `superpowers-iastudio.md`: protocolo operativo inspirado en `obra/superpowers`.
- `ecc-iastudio.md`: sistema de operacion agentica inspirado en `affaan-m/ECC`.
- `ui-ux-pro-max-iastudio.md`: protocolo de diseno UI/UX inspirado en `nextlevelbuilder/ui-ux-pro-max-skill`.
- `open-design-iastudio.md`: pipeline de produccion visual inspirado en `nexu-io/open-design`.
- `grida-iastudio.md`: radar tecnico para Grida: canvas, Figma rendering, forms y Supabase CMS.
- `learn-skills-iastudio.md`: radar de skills inspirado en `NeverSight/learn-skills.dev`.
- `skill-radar-watchlist.md`: categorias de skills que IAStudio debe monitorear.
- `cult-ui-iastudio.md`: banco de componentes shadcn/motion para landings, demos, dashboards y artefactos IA.
- `agency-agents-iastudio.md`: router de auto-invocacion de agentes especialistas para crear o modificar proyectos.
- `prompt-agente-web-premium-iastudio.md`: protocolo premium para propuestas web, landing pages y redisenos.
- `claude-seo-iastudio.md`: protocolo SEO/GEO para auditorias, SEO local, schema, CWV y reportes.
- `remotion-skills-iastudio.md`: protocolo de video programatico con Remotion para demos, ads, reportes y motion assets.
- `claude-code-setup-iastudio.md`: protocolo de auditoria read-only inspirado en la guia de TodoDeIA y el plugin oficial `claude-code-setup`.
- `fuentes-web.md`: paginas externas no-repo integradas a la memoria.
- `fuentes-internas.md`: textos, prompts y documentos locales integrados a la memoria.
- `fuentes-drive.md`: carpetas/archivos Drive recibidos y su estado de acceso.
- `google-drive-folder-iastudio.md`: registro pendiente de la carpeta Drive entregada el 2026-05-22.
- `claude-mem-iastudio.md`: protocolo de memoria progresiva inspirado en `thedotmack/claude-mem`.
- `n8n-mcp-iastudio.md`: protocolo para disenar, validar y operar workflows n8n con MCP.
- `observations-index.md`: indice ligero de aprendizajes con IDs para recuperar contexto sin cargar todo.

## Sistemas complementarios

- `../design-system/MASTER.md`: fuente visual base para landing, demos y paneles IAStudio.
- `../design-system/DESIGN.md`: version compatible con el esquema `DESIGN.md` de Open Design.
- `../design-system/critique-rubric.md`: autocritica visual de 5 dimensiones para entregas.
- `../design-system/pages/`: overrides por pagina o tipo de entregable.

## Regla de memoria progresiva

Antes de abrir archivos largos, revisar `observations-index.md` para ubicar el aprendizaje por ID. Si hace falta detalle, abrir solo el archivo especifico enlazado en la fila.
