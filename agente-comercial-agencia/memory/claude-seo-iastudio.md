# Claude SEO IAStudio

> Adaptacion operativa de `AgriciDaniel/claude-seo` para Saul IA Studios.

## Fuente

- Repo: https://github.com/AgriciDaniel/claude-seo
- Codex port relacionado: https://github.com/AgriciDaniel/codex-seo
- Licencia: MIT
- Fecha de lectura: 2026-05-21

## Que es

Claude SEO es una skill suite para Claude Code orientada a auditorias SEO completas. Incluye un orquestador, sub-skills y subagentes para SEO tecnico, contenido, schema, sitemaps, imagenes, Core Web Vitals, SEO local, mapas, backlinks, GEO/AEO para busqueda con IA, clustering semantico, SXO, drift monitoring, ecommerce, hreflang, APIs de Google y reportes PDF/HTML.

El repo tambien apunta a `AgriciDaniel/codex-seo` como port nativo para Codex. Para IAStudio se integra primero como protocolo y matriz de auditoria; la instalacion se evaluara despues.

## Valor para IAStudio

IAStudio gana una capa SEO/GEO para que cada landing, demo o sitio de cliente no solo se vea bien, sino que pueda:

- indexar correctamente,
- cargar rapido,
- explicar bien su entidad/servicio,
- aparecer en busquedas locales,
- tener schema valido,
- ser citable por IA,
- mantener baseline antes/despues de cambios,
- generar backlog priorizado.

Esto refuerza ofertas como:

- Auditoria SEO Express.
- Setup SEO local para pymes.
- Optimizar landing antes de lanzar ads.
- GEO/AEO para aparecer en respuestas de IA.
- Reporte mensual de salud web.
- Paquete "Landing + SEO tecnico + schema".

## Protocolo IAStudio para paginas publicas

Usar cuando se cree o modifique:

- `index.html`
- demos por nicho
- landing de cliente
- product site
- pagina de servicios
- blog/articulo
- pagina local por ciudad
- sitio que recibira ads

### 1. Preflight SEO tecnico

- `title` unico y con intencion clara.
- `meta description` concreta.
- Canonical si aplica.
- Robots/indexabilidad revisados.
- Headings ordenados.
- Links internos con anchors descriptivos.
- Open Graph/Twitter cards si se comparte por WhatsApp/redes.
- Sitemap/robots si el sitio tiene varias paginas.

### 2. Performance / Core Web Vitals

Objetivos:

- LCP menor a 2.5s.
- INP menor a 200ms.
- CLS menor a 0.1.

Checks:

- imagenes lazy-load cuando corresponda,
- dimensiones reservadas para evitar CLS,
- CSS/JS sin peso innecesario,
- animaciones con `transform` y `opacity`,
- fuentes con pesos limitados.

### 3. Schema

Prioridad para IAStudio:

- `Organization`
- `LocalBusiness` / subtipo segun cliente
- `Service`
- `Product` si aplica
- `FAQPage` solo con criterio: no venderlo como rich result comercial general, sino como estructura util para IA/citabilidad cuando aporte
- `BreadcrumbList`
- `WebSite`
- `SoftwareSourceCode` si se documenta una herramienta/codigo abierto

Evitar recomendar schema deprecado o restringido como si fuera ventaja directa.

### 4. SEO local

Para pymes locales:

- NAP consistente: nombre, direccion, telefono.
- `tel:` visible y correcto.
- ciudad/comuna/servicio en title, H1 o copy cuando tenga sentido.
- Google Business Profile referenciado si existe.
- resenas recientes y visibles si el cliente las tiene.
- fotos reales del negocio/servicio.
- pagina dedicada por servicio principal.
- LocalBusiness schema.
- citaciones basicas: Google, Bing Places, Apple Business Connect, Facebook, directorios de industria.

Regla anti-doorway:
- No crear paginas de comuna/ciudad intercambiables.
- Si se cambia el nombre de la ciudad y el texto sigue funcionando igual, la pagina es debil.

### 5. GEO / AI Search

Para aparecer mejor en respuestas de IA:

- entidad clara: quien es, que hace, donde opera, para quien.
- secciones con respuestas directas a preguntas reales.
- pruebas, casos, proceso y limites del servicio.
- datos estructurados cuando aporten.
- autor/contacto/empresa visibles.
- paginas rastreables sin depender solo de JS cliente.
- contenido que pueda citarse, no solo slogans.

### 6. SXO

SEO no termina en ranking. Revisar:

- intencion de busqueda,
- promesa del hero,
- CTA visible,
- prueba/confianza,
- friccion del formulario,
- camino a WhatsApp,
- respuesta a objeciones,
- velocidad para tomar accion.

### 7. Drift monitoring

Antes de cambios grandes:

- registrar baseline: title, H1, meta, schema, CWV, indexabilidad, canonical, principales CTAs.

Despues:

- comparar cambios,
- detectar regresiones,
- documentar si el cambio mejora conversion pero baja SEO, o viceversa.

## Router de agentes SEO para IAStudio

Cuando se use `agency-agents-iastudio.md`, activar estos roles si aplica:

- SEO Strategist
- Technical SEO Auditor
- Content/E-E-A-T Reviewer
- Schema Specialist
- Performance Benchmarker
- Visual/Above-the-fold Reviewer
- Local SEO Specialist
- GEO/AEO Specialist
- Backlink/Citation Analyst
- SXO Reviewer
- Drift Monitor
- Report Generator

Si existen subagentes reales en el entorno, delegar por area. Si no, usar esta lista como checklist.

## Instalacion futura

No instalar automaticamente. Si se decide instalar:

1. Preferir revisar `AgriciDaniel/codex-seo` por ser port nativo para Codex.
2. Clonar y revisar scripts antes de ejecutar.
3. No usar one-liners remotos sin inspeccion.
4. Mantener credenciales fuera del repo.
5. Separar modo sin credenciales, modo Google API y modo extensiones premium.

## Credenciales y seguridad

No guardar en memoria ni repo:

- Google API keys.
- OAuth client secrets.
- Service accounts.
- GA4 configs privadas.
- DataForSEO credentials.
- Firecrawl tokens.
- Ahrefs/Semrush/Moz/Bing API keys.

Las integraciones con GSC, PageSpeed, CrUX, GA4, DataForSEO o Firecrawl se activan solo con permiso explicito y ambiente controlado.

## Limitaciones importantes

- Sitios SPA sin SSR pueden dar falsos negativos si se audita solo HTML crudo.
- Para React/Vite/CSR, usar navegador/renderizado o verificar visualmente.
- Las recomendaciones SEO deben priorizarse por impacto comercial, no por checklist infinito.
- No prometer ranking garantizado.
- SEO local necesita datos reales: direccion, telefono, GBP, resenas y servicio.

## Que ganamos

IAStudio gana una capa de auditoria SEO/GEO lista para combinar con diseno premium, captacion por WhatsApp, ads y automatizacion. La landing deja de ser solo una pieza visual y pasa a ser un activo rastreable, medible y defendible ante cliente.
