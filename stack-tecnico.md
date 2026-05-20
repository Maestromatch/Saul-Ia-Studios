# Stack técnico — Saul IA Studios

Documento de referencia interno. Sirve para:
1. Responder al prospecto cuando pregunta "¿con qué lo haces?"
2. Planificar entregas de pilotos
3. Estimar costos reales mes a mes

> Regla del playbook: NO mencionar nombres técnicos al prospecto al inicio (no vender tecnología, vender resultados). Solo abrir el detalle si el cliente insiste o es técnico.

## Cómo se construye lo que vendemos

| Pieza del piloto | Herramienta principal | Costo Saul | Costo cliente |
|---|---|---|---|
| Bot WhatsApp (atención + agenda + captura) | **n8n** + **OpenAI API (gpt-4o-mini)** | Compartido VPS | $0 (vive en VPS Saul) |
| Memoria del bot / historial | **Supabase** (plan free) | $0 | $0 (puede migrar después) |
| Conexión a WhatsApp | API oficial WhatsApp Business o WhatsApp Web vía n8n | $0 hasta volumen | Depende de su WA |
| Mini landing / formulario | HTML estático + GitHub + Vercel/Easypanel | $0 | Dominio opcional ~$15K/año |
| CRM básico (incluido en todos los packs) | Google Sheets con plantilla | $0 | $0 |
| Dashboard de leads (Pack Completo $450K+) | HTML + Supabase Auth (construido por Claude Code) | Tiempo dev | $0 |
| Agenda integrada | Google Calendar API vía n8n | $0 | $0 |
| Recordatorios automáticos 24h | n8n workflow programado | Tiempo dev | $0 |
| Agente de voz (no incluido en IA Express base) | **Retell AI** | Pago por uso | Por proyecto |

## Infraestructura propia (vive en VPS Saul)

| Servicio | Para qué | Costo mensual Saul |
|---|---|---|
| **Contabo VPS** | Servidor físico donde vive todo | ~$8 USD |
| **Easypanel** | Panel para administrar el VPS sin terminal | $0 (free tier) |
| **Cloudflare** | CDN + protección + dominios | $0 (free) |
| **n8n autohospedado** | Motor de automatizaciones | $0 (corre en VPS) |
| **Supabase free** | Base de datos hasta 500MB / 50K usuarios | $0 |
| **GitHub** | Versionado del código | $0 |
| **OpenAI API** | Costo por mensaje del bot (gpt-4o-mini) | Variable, ~$0.0001-0.001 por respuesta |
| **Claude / Claude Code** | Construcción asistida | Suscripción personal |
| **Total infra fija** | | **~$8 USD = ~$8.000 CLP/mes** |

Margen: con 1 cliente activo de mantención básica ($80K), la infra se paga 10 veces.

## Herramientas de construcción (uso interno)

- **Claude Code** — escribir/modificar código del bot, landing, dashboard
- **Antigravity** — gestión de proyectos código con tablero visual
- **Stitch** — diseño visual inicial de landings antes de codear
- **Flow** — generación de imágenes IA (logos, ads)
- **Canva** — edición manual de creatividades
- **CapCut** — edición de videos demo/testimonios

## Lo que se le pide al cliente antes de arrancar

1. **WhatsApp Business activado** en su número operativo (no WhatsApp normal). Si no lo tiene, ayudamos a migrar — toma 10 min.
2. **Cuenta Google del negocio** para conectar Google Calendar y Sheets.
3. **Logo en PNG fondo transparente** (si quiere landing/material gráfico).
4. **Acceso a las 15-20 preguntas frecuentes** que reciben hoy (cuestionario onboarding lo extrae).
5. **Listado de precios "desde"** + convenios + marcas.
6. **Decidir un encargado** que va a usar el CRM y recibir las alertas.

## Lo que NO se promete técnicamente (manejar expectativas)

- ❌ NO se ofrece **WhatsApp API oficial pagada** (Meta Cloud API): se usa la vía API alternativa via n8n. Si el cliente quiere oficial, se cotiza aparte.
- ❌ NO se integra a sistemas ERP/CRM privados del cliente (Defontana, Bsale, etc.) en el pack base. Esa integración es proyecto a parte.
- ❌ NO se ofrece **app móvil propia**. El bot vive en WhatsApp y el panel es web responsive.
- ❌ NO se garantiza **0% downtime**: el VPS Contabo tiene ~99.5% de uptime histórico, suficiente para pyme. Para SLA empresarial se cotiza otro plan.
- ❌ NO se promete **respuesta a cualquier pregunta**: el bot responde lo que cargamos en su base. Lo que sale del guion se deriva a humano.

## Cómo se entrega el bot al cliente

1. El bot vive en **el VPS de Saul** (no en el celular del cliente).
2. Conectado al WhatsApp Business del cliente vía n8n.
3. Mientras el cliente esté en mantención, el bot opera 24/7.
4. Si el cliente cancela mantención: se le entrega backup del flujo n8n + planilla CRM exportada. Si quiere seguir solo, tendría que levantarlo en su propio VPS.

> Esto crea **lock-in suave**: el cliente puede irse pero no es trivial. La mejor retención sigue siendo entregar valor y mantener mejoras mensuales.

## Cuando el prospecto pregunta directamente

**"¿Con qué tecnología lo haces?"**
> Lo construimos con herramientas profesionales: OpenAI para la inteligencia, n8n para las automatizaciones, Supabase para guardar los datos y WhatsApp Business como canal. Todo corre en un servidor propio que administramos por ti. Lo importante: tú no tienes que aprender nada de eso — yo lo dejo funcionando.

**"¿Y si quiero llevármelo a otra persona después?"**
> Sin problema. Te entrego el backup del flujo y la planilla con los datos. Lo que pierdes es la mantención y mejoras que hago mes a mes — pero el sistema base es portable.

**"¿Es ChatGPT?"**
> En el fondo usamos el motor de OpenAI (la misma tecnología detrás de ChatGPT), pero adaptado a tu negocio. La diferencia con ChatGPT general es que solo responde lo que sabe de tu óptica/taller/etc., no inventa cosas fuera de tu guion.

**"¿Y si OpenAI sube los precios?"**
> El costo por mensaje hoy es centavos. Si subiera 10x, sigue siendo marginal vs. el valor de no perder clientes. Si en algún momento se vuelve caro, hay alternativas (Claude, Gemini, modelos open source). Yo me adapto, el cliente no se entera.

## Actualizaciones de stack

| Fecha | Cambio | Razón |
|---|---|---|
| 2026-05-16 | Documento inicial | Consolidar antes del primer cierre |
| 2026-05-19 | n8n-MCP como herramienta interna de diseno y validacion | Reducir errores al crear workflows n8n, validar nodos/conexiones y evitar tocar produccion directo con IA |

## Herramienta interna: n8n-MCP

`n8n-MCP` queda como herramienta interna posible para construir y revisar automatizaciones n8n.

Uso recomendado:
- Primero en modo documentacion/validacion, sin `N8N_API_KEY`.
- Solo usar modo gestion con API si existe ambiente de desarrollo, backup y permisos controlados.
- Nunca editar workflows productivos directamente con IA.
- Buscar templates antes de crear desde cero.
- Configurar parametros explicitamente; no confiar en defaults.
- Validar nodo por nodo y luego workflow completo antes de entregar.
- Desactivar o limitar herramientas peligrosas si no se necesitan.

No se menciona al prospecto salvo que pregunte por el stack tecnico. Para venta, el mensaje sigue siendo: "dejamos el sistema funcionando, probado y con seguimiento".
