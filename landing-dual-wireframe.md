# Wireframe Landing Dual - Saul IA Studios

Wireframe low-fidelity (ASCII) para evolucionar `index.html` actual a landing con 3 productos. NO romper la jerarquía existente — solo sumar.

## Estructura nueva del flujo de página

Orden de secciones (top → bottom):

1. **Topbar** (sin cambios) + nav: Pack IA Express · Formaliza · Emprendedor 360 · WhatsApp
2. **Hero** (igual que hoy: H1 promesa + chat demo + CTA primario) + agregar tag de prueba social/urgencia
3. **Sección "Para quién es"** (NUEVA, breve) — 3 cards: "Tu negocio ya opera" / "Necesitas formalizar" / "Empiezas de cero"
4. **Pack IA Express** (sección actual `#oferta` mantiene su lugar)
5. **Demo flujo** (sección actual `#demo` muted)
6. **Formaliza Tu Negocio** (NUEVA — 3 tiers DIY/Híbrido/Llave en mano)
7. **Pack Emprendedor 360** (NUEVA — flagship, 1 sola card grande con anclaje al WhatsApp)
8. **Plan 7 días** (sección actual `#proceso`)
9. **Footer** (sin cambios pero agregar IG + año + privacidad)

## Wireframe ASCII — Sección Formaliza

```
┌────────────────────────────────────────────────────────────────────┐
│  FORMALIZA TU NEGOCIO          [eyebrow: Servicio standalone]      │
│  Constituye tu empresa sin perder semanas en trámites.             │
│                                                                    │
│  Te dejamos con SpA + inicio actividades + cuenta bancaria +       │
│  factura electrónica funcionando. Vía abogado y contador aliados.  │
└────────────────────────────────────────────────────────────────────┘

┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│   DIY GUIADO     │  │    HÍBRIDO       │  │  LLAVE EN MANO   │
│   $89.000 CLP    │  │   $249.000 CLP   │  │  $590.000 CLP    │
│   ─────────────  │  │   ─────────────  │  │  ─────────────   │
│  • PDF + 1 zoom  │  │  + revisión      │  │  + abogado +     │
│    60 min        │  │    abogado       │  │    contador      │
│  • Tú ejecutas   │  │  + setup oficina │  │    coordinados   │
│  • Plantillas    │  │    virtual       │  │  + cuenta banco  │
│                  │  │  + chat soporte  │  │  + cert digital  │
│                  │  │                  │  │  + 1er F29       │
│  [Pedir info]    │  │  [Pedir info]    │  │  [Pedir info]    │
└──────────────────┘  └──────────────────┘  └──────────────────┘
                          [⭐ MÁS ELEGIDO]

¿Por qué esto no lo hace cualquiera?
✓ Saul lo vivió: aprendió constituyendo Saul IA Studios SpA paso a paso
✓ Aliados de confianza: abogado y contador chilenos, no plataforma genérica
✓ Garantía: si SII rechaza por error nuestro, lo solucionamos sin costo
```

## Wireframe ASCII — Sección Pack Emprendedor 360 (flagship)

```
┌────────────────────────────────────────────────────────────────────┐
│ [eyebrow: PROGRAMA BANDERA]                                        │
│                                                                    │
│  PACK EMPRENDEDOR 360                                              │
│  De idea a negocio operando en 45 días.                           │
│                                                                    │
│  Para quien tiene talento pero NO tiene empresa, NO tiene          │
│  presencia digital y NO tiene clientes.                            │
│                                                                    │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│  Incluye:                                                          │
│  ✓ Formaliza Tu Negocio (Tier Híbrido o Llave en mano)            │
│  ✓ Pack IA Express (landing + bot WhatsApp + CRM)                 │
│  ✓ 2 a 4 sesiones de asesoría comercial                           │
│  ✓ Acompañamiento hasta primeros clientes                          │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│                                                                    │
│  Esencial $590K · Pro $890K · 50% anticipo / 50% contra entrega  │
│                                                                    │
│  [▶  Quiero el camino completo en 45 días]                        │
└────────────────────────────────────────────────────────────────────┘
```

## 3 decisiones críticas de UX a resolver antes de implementar

### 1. ¿Una sola landing larga o landing dividida?
- **Opción A — landing larga única**: una scroll-page con todos los productos. Pro: SEO concentrado, narrativa unificada. Contra: el visitante específico (ya con empresa, solo quiere bot) tiene que scrollear mucho.
- **Opción B — home + 3 sub-páginas** (`/pack-ia-express`, `/formaliza`, `/emprendedor-360`): cada producto su URL. Pro: anuncios Meta Ads pueden llevar a la página exacta. Contra: más mantenimiento, más decisión de UX.
- **Recomendación**: A para esta semana (rapidez), B para semana 3-4 cuando tengas anuncios pagos.

### 2. ¿Cómo se decide el "para quién es"?
Si el visitante no sabe cuál de los 3 productos elegir, perdemos la conversión. Solución: agregar **micro-quiz arriba de las ofertas** (3 preguntas, 30 segundos): "¿Tu negocio ya opera?" / "¿Tienes empresa constituida?" / "¿Tienes clientes hoy?". Cada combinación lleva al CTA correcto.
- **Acción esta semana**: implementar versión simple (3 cards en sección "Para quién es") como filtro visual. El quiz interactivo queda para semana 2-3.

### 3. ¿Pack Emprendedor 360 destacado o discreto?
Es el flagship pero también el ticket más alto ($590K-$890K). Si lo pones primero, asustas. Si lo escondes, no convierte.
- **Recomendación**: Pack Emprendedor 360 va **DESPUÉS de Formaliza**, con tratamiento visual diferenciado (banda full-width, color acento más fuerte, "Programa Bandera" como eyebrow). El flujo natural del visitante "empezando de cero" lo lleva ahí: Formaliza ($249K) → "ah pero también necesito web/clientes" → 360 ($590K). Upgrade natural.

## Notas de implementación

- Mantener variables CSS actuales (`--accent`, `--accent-dark`, etc.) — no inventar paleta nueva.
- `style.css` actual ya tiene `.steps`, `.timeline`, `.offer-grid`, `.closing-band`, `.price-card`. Reusar estas clases. Solo agregar:
  - `.pricing-3-tier` (grid 3 columnas → 1 en móvil) para Formaliza
  - `.flagship-band` (banda destacada) para Emprendedor 360
- Modal/quiz queda para semana 2.
- Tracking: cada CTA WhatsApp debe llevar mensaje pre-llenado distinto para identificar de dónde vino el lead.
