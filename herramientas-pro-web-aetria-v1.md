# Herramientas pro web AETRIA - ruta de conexion

> Nota operativa para guiar a Saul cuando quiera pasar de landing estatica a stack pro de diseno, visualizacion, componentes y deploy.

## Objetivo

Conectar herramientas premium sin perder velocidad comercial: primero vender y validar, despues profesionalizar el stack donde aporte calidad, velocidad o confianza.

## Stack actual

- Web estatica en Vercel: `index.html` + `style.css` + JS vanilla.
- Deploy por push a GitHub/Vercel.
- Assets de marca AETRIA en raiz del proyecto.
- Ideal para probar copy, diseno, CTA y oferta rapido.

## Camino Next.js iniciado

- Carpeta paralela creada: `web-aetria-next/`.
- Stack instalado: Next.js 16, React 19, TypeScript, Tailwind 4 y ESLint.
- Assets copiados a `web-aetria-next/public/brand/`.
- Primera landing base creada en `web-aetria-next/src/app/page.tsx`.
- Este proyecto no reemplaza todavia el deploy actual. Sirve para migrar por componentes sin romper produccion.

### Notas de instalacion Windows

- `npm` necesito usar certificados del sistema:
  - PowerShell: `$env:NODE_OPTIONS='--use-system-ca'; npm install --no-audit --no-fund`
- Se agrego `.npmrc` local en `web-aetria-next/` con timeouts largos, SSL activo y sin audit/fund.
- No usar `strict-ssl=false` salvo emergencia justificada. Preferir certificados del sistema.

## Herramientas pro sugeridas

### 1. Figma

Uso:
- Pasar landing a mockup editable.
- Crear design system AETRIA: tokens, componentes, cards, hero, secciones, dashboard.
- Revisar responsive y variantes antes de codear.

Permiso/conexion:
- Conector Figma activo en Codex cuando se use URL de archivo Figma.
- Si se crea archivo nuevo, pedir confirmacion antes.

Cuando usar:
- Antes de redisenos grandes.
- Para presentar propuesta premium a cliente.
- Para convertir la identidad visual en sistema reusable.

### 2. Canva

Uso:
- Piezas de redes, portadas, flyers, propuestas visuales y branding rapido.
- Adaptar assets AETRIA a formatos Instagram, LinkedIn, WhatsApp y Facebook.

Permiso/conexion:
- Conector Canva activo si el diseno vive en Canva.
- No usar para tocar la web directamente; usarlo como motor de piezas comerciales.

Cuando usar:
- Campanas organicas.
- Material comercial para prospectos.
- Portadas y publicaciones del lanzamiento.

### 3. Visualizacion web / data storytelling

Uso:
- Mapas IA, flujos de automatizacion, dashboards, metricas y diagramas interactivos.
- Puede resolverse primero con HTML/CSS/SVG nativo.
- Si escala: D3, Observable Plot, Recharts o componentes React.

Permiso/conexion:
- Si aparece un plugin especifico de data visualization, verificar herramientas disponibles con `tool_search`.
- No instalar librerias pesadas sin justificar valor.

Cuando usar:
- Dashboard de resultados.
- Demo de sistema IA.
- Presentaciones comerciales con datos reales.

### 4. Next.js + React

Uso:
- Migrar landing a componentes: `HeroSection`, `ServicesSection`, `AiMapSection`, `FounderSection`, `MetricsSection`.
- Usar `next/image`, rutas, metadata, componentes reutilizables y deploy Vercel mas robusto.

Permiso/conexion:
- Requiere crear proyecto o migrar repo.
- Revisar Node/npm instalados.
- Definir si se migra el repo actual o se crea carpeta nueva.

Cuando usar:
- Cuando el diseno AETRIA ya este validado.
- Cuando haya mas paginas, dashboards, formularios o CMS.
- Cuando convenga mantener componentes en vez de HTML largo.

## Regla de decision

1. Si solo queremos probar mensaje y vender: HTML/CSS actual.
2. Si queremos mostrar diseno premium a cliente: Figma o Canva.
3. Si necesitamos interaccion o dashboards reales: Next.js + React.
4. Si hay datos complejos: libreria de visualizacion, elegida por caso.

## Checklist antes de activar Next.js

- Confirmar que Node.js y npm funcionan. Hecho: Node `v24.15.0`, npm `11.12.1`.
- Decidir dominio principal: `aetriastudio.cl` o Vercel temporal.
- Definir rutas: home, servicios, proyectos, privacidad, terminos, demos.
- Mover assets a `public/brand/`.
- Convertir secciones actuales a componentes.
- Mantener WhatsApp `+56968171774`.
- Probar mobile 375px, tablet 768px, desktop 1440px.
- Hacer deploy preview antes de reemplazar produccion.

## Transferibilidad OS

Este documento se puede convertir despues en SOP para migrar landing estatica a stack premium reusable de AETRIA.
