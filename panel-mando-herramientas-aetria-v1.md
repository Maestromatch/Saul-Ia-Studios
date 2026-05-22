# Panel de Mando Herramientas - Aetria Studio V1

## Objetivo

Definir que herramientas usa Aetria Studio en cada servicio, que credenciales faltan y que conectores pueden mejorar la ejecucion desde este panel.

Regla: no vender tecnologia. La tecnologia se usa para entregar sistemas claros, medibles y mantenibles.

## Estado general

| Area | Herramienta base | Estado | Falta |
|---|---|---:|---|
| Web / landing | HTML estatico + Vercel | Activo | Migrar a Next.js cuando convenga |
| Versionado | GitHub | Activo | Mantener ramas por cambios grandes |
| Automatizacion | n8n | Activo / probado en proyectos | Checklist de ambientes dev/prod |
| IA texto | OpenAI API / ChatGPT / Claude | Activo | Definir costo por servicio |
| CRM simple | Google Sheets | Listo | Plantilla final Aetria |
| Base de datos | Supabase | Disponible | Definir por proyecto |
| Contenido visual | Canva / CapCut | Disponible | Plantillas Aetria controladas |
| Ads | Meta Business Suite / Ads Manager | Requiere acceso cliente | Checklist de IDs |
| Google local | Google Business Profile | Requiere acceso cliente | Checklist de permisos |
| Agenda | Calendly / Google Calendar | Pendiente URL real | Configurar evento diagnostico |
| Documentacion | Markdown en repo | Activo | Convertir SOPs clave a plantillas |

## Servicios y stack recomendado

### 1. Diagnostico IA Express

Herramientas:
- Checklist Aetria en Markdown.
- Google Sheets o CSV para registro.
- Capturas del negocio: WhatsApp, Instagram, Google Business, landing.
- ChatGPT/Codex para analisis y plan de accion.

Credenciales requeridas:
- Ninguna al inicio.
- Links publicos del negocio.

Entregable:
- Documento breve con fugas, prioridades y siguiente paso recomendado.

Checklist listo:
- [ ] Plantilla diagnostico.
- [ ] Formulario de datos iniciales.
- [ ] Mensaje de entrega.
- [ ] Opcion de descuento si escala a setup.

### 2. Setup Identidad Meta Legal

Herramientas:
- Meta Business Suite.
- Meta Business Manager.
- Ads Manager.
- Events Manager / Pixel.
- Documento checklist de activos.

Credenciales requeridas:
- Acceso del cliente a Instagram/Facebook.
- Acceso a Business Manager.
- Cuenta publicitaria.
- Dominio si existe.
- Datos legales/facturacion si aplica.

Entregable:
- Mapa de activos.
- Estado de permisos.
- Recomendaciones.
- Proximo paso para campanas.

Checklist listo:
- [ ] Checklist permisos Meta.
- [ ] Guia para encontrar Business ID, Ad Account ID y Pixel ID.
- [ ] Plantilla de reporte.

### 3. Bot WhatsApp + CRM Simple

Herramientas:
- WhatsApp Business.
- n8n.
- OpenAI API.
- Google Sheets o Supabase.
- Google Drive para materiales.

Credenciales requeridas:
- Numero WhatsApp Business del cliente.
- Preguntas frecuentes.
- Servicios/precios desde.
- Responsable humano.
- Google Account o base de datos del proyecto.

Entregable:
- Bot inicial.
- CRM con estados.
- Mensajes de seguimiento.
- Guia de uso.

Checklist listo:
- [ ] Plantilla n8n bot base.
- [ ] Plantilla CRM Aetria.
- [ ] Prompt de bot por rubro.
- [ ] Casos de prueba.

### 4. Landing Express

Herramientas:
- HTML/CSS o Next.js segun proyecto.
- GitHub.
- Vercel.
- Canva o assets propios.
- Google Search Console cuando exista dominio.

Credenciales requeridas:
- Dominio o subdominio.
- Logo/fotos.
- Oferta.
- WhatsApp.
- Testimonios autorizados si existen.

Entregable:
- Landing publicada.
- SEO basico.
- CTA WhatsApp/Calendly.
- Politicas si captura datos.

Checklist listo:
- [ ] Plantilla landing Aetria.
- [ ] Checklist SEO local.
- [ ] Checklist mobile.
- [ ] Checklist enlaces.

### 5. Pack IA Express

Herramientas:
- Landing o formulario.
- Bot WhatsApp.
- CRM simple.
- n8n.
- OpenAI API.
- Google Sheets/Supabase.
- Vercel.

Credenciales requeridas:
- Todo lo de bot + landing.

Entregable:
- Sistema minimo viable de captacion, atencion y seguimiento.

Checklist listo:
- [ ] SOP de implementacion 7 dias.
- [ ] QA end-to-end.
- [ ] Documento de entrega.
- [ ] Soporte inicial.

### 6. Sistema de Captacion IA para Emprendedores

Herramientas:
- Meta Ads.
- Landing.
- WhatsApp Business.
- Bot IA.
- CRM.
- Pixel/Eventos si aplica.
- Reporte semanal.

Credenciales requeridas:
- Meta Business.
- Cuenta publicitaria.
- Pixel/dominio si aplica.
- Presupuesto de pauta.
- Oferta y materiales.

Entregable:
- Sistema de captacion conectado a seguimiento.

Checklist listo:
- [ ] Checklist Meta.
- [ ] Matriz de anuncios.
- [ ] Landing.
- [ ] Bot/CRM.
- [ ] Reporte.

### 7. Content Engine IA

Herramientas:
- Google Drive.
- Canva.
- CapCut.
- ChatGPT/Claude para copy.
- n8n publicador si aplica.
- Instagram/Facebook/Google Business.

Credenciales requeridas:
- Carpeta de fotos/videos.
- Acceso a redes si publicamos.
- Lineamientos de marca.

Entregable:
- Posts, captions, reels/carruseles y calendario.

Checklist listo:
- [ ] Carpeta Drive.
- [ ] Plantilla calendario.
- [ ] Plantillas Canva.
- [ ] Flujo aprobacion.

### 8. Ads Growth Management

Herramientas:
- Meta Ads Manager.
- Events Manager.
- Landing/WhatsApp.
- CRM.
- Looker Studio o reporte simple.

Credenciales requeridas:
- Acceso cuenta publicitaria.
- Presupuesto mensual.
- Pixel/eventos si aplica.
- Creativos.
- Oferta activa.

Entregable:
- Gestion, aprendizaje y optimizacion mensual.

Checklist listo:
- [ ] Estructura campanas.
- [ ] Naming convention.
- [ ] Rutina semanal.
- [ ] Reporte mensual.

## Plugins / conectores utiles desde este panel

### Ya disponible o usado

- Canva: generar y revisar piezas, aunque el diseno premium debe controlarse manualmente.
- Git/GitHub via CLI: versionado y push.
- Browser/local preview si se activa servidor.

### Recomendados para instalar/conectar cuando toque

- GitHub plugin: revisar PRs, issues, ramas y cambios con mas control.
- Google Drive plugin: leer carpetas de assets de clientes, fotos/videos y documentos.
- Google Calendar plugin: gestionar diagnosticos y disponibilidad.
- Gmail plugin: seguimiento comercial si se usa correo.
- Slack/Teams: solo si Aetria crea equipo.
- OpenAI Developers plugin: revisar API, costos y configuracion cuando empaquetemos bots.
- Figma plugin: si decidimos crear sistema visual profesional fuera de Canva.

## Credenciales que NO deben pegarse en chat

- OpenAI API keys.
- Meta access tokens.
- n8n API key.
- Supabase service role.
- Passwords de correos.
- Tokens de Google.
- Credenciales de clientes.

Usar archivos `.local.md` o gestores de secretos. No commitear.

## Fase actual

Estamos entrando en Fase Herramientas y Operacion.

Prioridad:
1. Cerrar checklist por servicio.
2. Definir plantillas base.
3. Conectar calendario real.
4. Preparar CRM interno.
5. Ejecutar prospeccion con Diagnostico IA Express.

