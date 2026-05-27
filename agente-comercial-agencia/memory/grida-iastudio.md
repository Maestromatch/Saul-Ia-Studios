# Grida IAStudio

> Adaptacion del repo `gridaco/grida` para Saul IA Studios.

Fuente principal: https://github.com/gridaco/grida

## Que es

Grida es un proyecto open-source que combina editor/canvas 2D, motor de render, Database/CMS y Forms. Su canvas usa Rust, Skia y WASM, con backends DOM y Skia. Tambien ofrece `@grida/refig`, un renderer headless para documentos Figma.

Licencia:
- Apache-2.0

Stack revisado:
- TypeScript
- React / Next.js
- Rust
- Skia
- WASM
- FlatBuffers
- Supabase
- pnpm monorepo

## Valor para IAStudio

Grida aporta ideas practicas para tres areas:

1. Exportar y renderizar disenos.
2. Crear formularios mas potentes.
3. Prototipar sistemas data-first conectados a Supabase.

No es una dependencia inmediata. Es radar tecnico para cuando IAStudio empiece a necesitar herramientas propias mas alla de landings HTML, Google Sheets y n8n.

## Piezas relevantes

### Canvas

Grida Canvas es un motor/editor 2D basado en nodos y propiedades.

Valor para IAStudio:
- Futuro editor de creatividades o plantillas.
- Visual builder para dashboards o componentes.
- No usar aun en produccion pagada porque el SDK esta en alpha.

### Refig

`@grida/refig` renderiza documentos Figma a PNG, JPEG, WebP, PDF o SVG en Node.js o navegador.

Valor para IAStudio:
- Exportar assets de Figma sin capturas manuales.
- Generar thumbnails para propuestas.
- Automatizar previews de disenos.
- Renderizar desde `.fig` offline o JSON de Figma REST.

Uso futuro:
- Solo cuando exista archivo `.fig` o flujo de diseno real.
- No usar para reemplazar implementacion HTML/CSS.

### Database / CMS

Grida tiene editor de base de datos/CMS conectado a Supabase:
- Tables
- Views
- Storage
- Auth
- CSV export
- Filter, sort, search
- Gallery/List/Charts views

Valor para IAStudio:
- Inspiracion para dashboards CRM.
- CMS simple para clientes con datos.
- Paneles sobre Supabase.

### Forms

Grida Forms incluye:
- 30+ inputs.
- File upload.
- Signature.
- Rich text.
- SMS verification.
- Logic blocks.
- Hidden fields.
- Search param seeding.
- Partial submissions.
- Supabase sync.
- Custom CSS.
- API-only/headless usage.

Valor para IAStudio:
- Reemplazo futuro de Google Forms/Typeform en leads complejos.
- Formularios de onboarding.
- Captura de cotizaciones con archivos/fotos.
- Flujos con firma o evidencia.

## Decision de adopcion

No instalar ahora.

Motivos:
- Monorepo grande.
- Requiere Node 22+ y pnpm 10+.
- Usa Rust/WASM para canvas.
- Canvas SDK alpha.
- Muchas partes son plataforma, no servicio listo para pyme.

Adoptar como:
- Criterio de arquitectura.
- Radar tecnico para formularios y CMS.
- Posible herramienta para export Figma.
- Inspiracion para dashboards data-first.

## Como se compara con lo actual

### Hoy

- Landing HTML.
- WhatsApp.
- n8n.
- Supabase.
- Google Sheets CRM.
- Demos manuales.

### Con Grida como radar

- Formularios avanzados conectados a Supabase.
- Export de assets desde Figma.
- CMS/dashboard mas visual.
- Prototipos data-first antes de app completa.

## Reglas de uso IAStudio

- No usar Grida para el primer piloto si HTML + n8n + Sheets resuelve.
- Evaluar Grida Forms cuando el formulario necesita uploads, firmas, logica o partial submissions.
- Evaluar `@grida/refig` si hay diseno Figma y se necesitan exports repetibles.
- Evitar Canvas SDK en cliente pagado hasta probarlo aislado.
- Mantener datos sensibles fuera del repo y de exports.

## Que gana IAStudio

IAStudio gana vision de producto: no todo debe ser landing + bot. Para clientes con datos, formularios y contenido, podemos pensar en sistemas data-first conectados a Supabase y con assets/export mas profesionales.
