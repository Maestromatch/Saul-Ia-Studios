# Scripts de llamada — 4 fijos pendientes

> Llamar en horario hábil ópticas: **lunes-viernes 10:30-13h o 15:30-18:30h** (evita primera hora donde están abriendo). Tono: relajado, sin vender en el teléfono, solo pedir contacto correcto.

## Objetivo de la llamada

**Conseguir el WhatsApp directo del encargado/dueño** para luego enviar el mensaje personalizado que ya está armado. NO vender en la llamada.

## Guion universal (adaptar a cada óptica)

### Apertura (15 seg)

> "Hola, buen día / buenas tardes. Hablo con [Nombre óptica]?
>
> Soy Saúl Constructor de Saul IA Studios. Estoy contactando ópticas de la zona porque armé una propuesta corta de un sistema con IA para ordenar consultas por WhatsApp, y prefiero coordinarlo con el dueño o encargado directamente.
>
> ¿Con quién podría hablar y por qué WhatsApp les llega más rápido?"

### Si dicen "yo soy el encargado/dueña"

> "Perfecto. Mira, no quiero ocuparte tiempo por teléfono — preparé una demo cortita de 1 minuto, te la mando por WhatsApp y la revisas cuando puedas. ¿Te la mando al mismo número desde donde llamo o tienes otro WhatsApp para esto?"

### Si dicen "está la dueña pero no puede atender"

> "Sin problema, no es urgente. ¿Me puedes pasar su WhatsApp directo así le mando una propuesta corta para que la vea cuando tenga 2 minutos? También sirve si me dices a qué hora suele estar más libre."

### Si dicen "déjame tu número y yo te llamo"

> "Claro, te paso el mío: +56 9 6817 1774, Saúl. Pero más eficiente para todos: si me das el WhatsApp del encargado, le mando un audio de 1 minuto y se evita una llamada. ¿Lo manejan ustedes por WhatsApp habitual?"

### Si preguntan "¿de qué se trata?"

> "Es un sistema simple para que cuando la gente les escriba por WhatsApp preguntando precios, convenios, horarios — el bot responda al toque y agende, sin que ustedes tengan que estar pendientes del celular. Cuesta entre 250 y 450 mil pesos según alcance. Lo mando por WhatsApp y lo ven cuando puedan, no es por teléfono."

### Si dicen "no nos interesa"

> "Te entiendo perfecto. ¿Le puedo dejar la propuesta de todas formas para que la vean ustedes cuando tengan 1 minuto? Si después de verla siguen sin interés, no insisto más. ¿Cuál es el WhatsApp por el que reciben los clientes?"

### Cierre (si te dan el WhatsApp)

> "Buenísimo, lo anoto. Te mando ahora mismo. Si después tienen alguna duda, escribes ahí y nos arreglamos. Que les vaya bien."

### Cierre (si no te dan WhatsApp)

> "Sin problema. Si en algún momento les interesa ver la demo, mi WhatsApp es +56 9 6817 1774 a nombre de Saúl. Que tengan buen día."

---

## Caso 1 — Optica San Bernardo (+56228561528)

**Contexto a recordar**:
- Multiservicio: lentes + contactología + audífonos + prótesis
- Web: opticasanbernardo.cl
- Dolor que apuntamos: consultas mezcladas entre servicios

**Mensaje que se va a mandar** (tener listo): mensaje #4 en `mensajes-personalizados-opticas-dia1.md`

**Si preguntan más del precio**: $250K-$450K según alcance, "armo propuesta exacta después de ver tu caso". No dar precio final por teléfono.

---

## Caso 2 — Optica Futuro La Cisterna (+56225279588)

**Contexto**:
- Óptica + fonoaudiología (servicios mixtos)
- Web: optica-futuro.cl
- IG: @opticafuturolacisterna
- Dolor: consultas de óptica y audiología mezcladas

**Mensaje a mandar**: mensaje #9 en archivo personalizado.

---

## Caso 3 — New Glasses San Miguel (+56225517908)

**Contexto**:
- Centro de contactología especializado
- 30+ años, 30.000 adaptaciones de lentes contacto
- Web: newglasses.cl
- Dolor: alto volumen de clientes con seguimientos manuales de adaptación

**Mensaje a mandar**: mensaje #17.

**Importante**: este es un negocio establecido. Si la persona en el fijo es secretaria, pedir el WhatsApp del **especialista** o **encargado comercial**, no el general.

---

## Caso 4 — Optica Gran Avenida (+56232326797)

**Contexto**:
- Óptica de barrio
- Sin web fuerte
- Dolor: canales digitales no ordenados

**Mensaje a mandar**: mensaje #14.

---

## Tracking post-llamada

Después de cada llamada, actualizar `tracker-prospeccion-opticas.csv`:

| Campo | Si conseguiste WhatsApp | Si NO conseguiste |
|---|---|---|
| `whatsapp` | El número que te dieron | "Llamado - sin WA disponible" |
| `estado` | `WhatsApp obtenido` | `Llamado sin éxito` |
| `ultimo_mensaje` | Fecha llamada | Fecha llamada |
| `proximo_paso` | Enviar mensaje #N | Reintentar en 30 días |
| `fecha_proximo_paso` | Hoy | Hoy + 30 días |
| `observaciones` | "Hablé con [Nombre], encargado/dueño" | Razón del rechazo |

## Reglas duras

- ❌ NO vender en la llamada.
- ❌ NO pedir reunión por teléfono al primer contacto.
- ❌ NO dejar precio sin contexto.
- ❌ NO insistir si dicen "no" claro 2 veces.
- ✅ La meta es **un WhatsApp**, no una venta.
- ✅ Si te dicen "mándame info por correo", **redirige a WhatsApp** ("por WhatsApp es más rápido, ¿cuál usan?").
