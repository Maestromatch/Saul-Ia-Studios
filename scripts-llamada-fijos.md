# Scripts de llamada — 4 fijos pendientes

> Llamar en horario hábil ópticas: **martes a jueves 10:00-12:00 y 16:00-18:00** (evita lunes caos semanal y viernes que nadie quiere compromisos nuevos). Tono: relajado, sin vender en el teléfono.

## Dos modos de operación

**MODO A — Conseguir WhatsApp** (approach actual AetriaStudio): cuando ya tienes mensaje personalizado listo y quieres enviar la demo. Objetivo: solo conseguir el número.

**MODO B — Conseguir reunión de diagnóstico** (approach Divisual): cuando quieres ir directo a una visita presencial o videollamada de 20 min. Objetivo: agenda una reunión. **Presencial cierra 3x más que videollamada**. Usar cuando el negocio está en la zona.

> **La frase maestra (Divisual):** "No vendes IA por teléfono. Vendes 20 minutos de su tiempo para un diagnóstico. La IA se vende sola cuando la enseñas en directo."

---

## MODO A — Objetivo: conseguir el WhatsApp

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

## Reglas duras (MODO A)

- ❌ NO vender en la llamada.
- ❌ NO pedir reunión por teléfono al primer contacto.
- ❌ NO dejar precio sin contexto.
- ❌ NO insistir si dicen "no" claro 2 veces.
- ✅ La meta es **un WhatsApp**, no una venta.
- ✅ Si te dicen "mándame info por correo", **redirige a WhatsApp** ("por WhatsApp es más rápido, ¿cuál usan?").

---

## MODO B — Objetivo: conseguir reunión de diagnóstico presencial

Fuente: Guión de Llamada en Frío de Divisual Project (Juan Pe Navarro) — mentoría feb 2026.

### Antes de marcar el teléfono

1. Investiga 2 minutos: web, redes, Google Maps. Busca **un problema concreto y visible** ("no tienen chatbot", "responden WhatsApps a mano").
2. Identifica al decisor: dueño, encargado, gerente. NUNCA pidas "alguien de marketing".
3. Define si eres nuevo (Versión A) o tienes casos (Versión B).
4. Si el negocio está en tu zona: objetivo = presencial. Si no: videollamada.

### Si atiende un empleado / recepcionista

> "Hola, buenos días. Necesito hablar un momento con **[NOMBRE DEL DUEÑO/ENCARGADO]**. ¿Está disponible?"

*Dices el nombre propio. El empleado asume que ya se conocen. Si no sabes el nombre, búscalo antes de llamar.*

Si preguntan "¿De parte de quién?":
> "Soy **Saúl**, de **AetriaStudio**. Le llamo porque he visto algo en su óptica que creo que le va a interesar. Son 2 minutos."

**ERROR COMÚN: nunca expliques el servicio al empleado.** Si dices "es sobre inteligencia artificial", el empleado no entiende, no decide, y perdiste la llamada.

### Ya tienes al decisor — los primeros 10 segundos

**VERSIÓN A — Si estás empezando:**
> "Hola [NOMBRE], soy Saúl. Mira, te voy a ser totalmente sincero: acabo de montar mi agencia de automatización e inteligencia artificial. Estoy buscando mis primeros clientes y he visto vuestra óptica. He detectado algo que creo que os puede ahorrar bastante tiempo. ¿Te puedo robar 2 minutos?"

*La sinceridad rompe el patrón. Baja la guardia. No suenas a vendedor, suenas a persona.*

**VERSIÓN B — Con experiencia (cuando ya tengas casos):**
> "Hola [NOMBRE], soy Saúl, de AetriaStudio. Llevamos [X] meses ayudando a ópticas de la zona a automatizar la atención por WhatsApp. He estado mirando vuestra web y he visto algo que les puede interesar. ¿Tienes un par de minutos?"

### Si dice "Sí, dime" — el pitch del diagnóstico

> "Perfecto. He estado viendo **[ALGO CONCRETO: su web, sus redes, su proceso de reservas]** y detecté que **[PROBLEMA ESPECÍFICO]**.
>
> Lo que hacemos es un diagnóstico inicial: analizamos cómo están recibiendo consultas, detectamos dónde pierden tiempo, y les mostramos en 20 minutos cómo se vería el sistema en su óptica.
>
> No les vendo nada por teléfono. Solo propongo **[pasar un café de 20 min / una videollamada de 15 min]** para mostrarles en vivo lo que detectamos. Sin compromiso. ¿Esta semana?"

### Manejo de objeciones

| Objeción | Respuesta |
|----------|-----------|
| "No me interesa / no tengo tiempo" | "Lo entiendo. ¿Me dejas enviarte un audio de 1 minuto explicando lo que detecté en tu óptica? Si no te interesa, no te vuelvo a molestar. ¿A qué WhatsApp te lo mando?" |
| "Ya tenemos alguien que nos lleva eso" | "Genial, significa que entienden el valor. Lo nuestro es complementario — hacemos un diagnóstico que revisa todo el negocio. Igual merece un café rápido para ver si hay algo no cubierto. ¿Esta semana?" |
| "Envíame info por email / WhatsApp" | "Claro. Pero lo que te envío es un análisis personalizado de su óptica, no un PDF genérico. Por eso necesito 15-20 minutos para mostrártelo. ¿Jueves o viernes?" |
| "¿Cuánto cuesta?" | "Depende del alcance, necesito ver su caso concreto. ¿Quedamos 20 min y lo explico sin compromiso?" |
| "No sé qué es la IA" | "Normal. Imagina que todo lo repetitivo — responder mensajes, agendar citas, confirmar horarios — se hiciera solo, 24 horas. Nosotros analizamos dónde les beneficiaría más. ¿15 min para mostrártelo?" |

### Cerrar la reunión

**Si es presencial (zona sur RM — siempre preferir):**
> "Perfecto. ¿Qué te parece si me paso el [DÍA] por la mañana? Son 20 minutos, te muestro en mi portátil lo que detectamos en su óptica. Sin compromiso. Si no convence, tan amigos."

**Si es videollamada:**
> "Perfecto. Te mando un enlace para el [DÍA] a las [HORA]. Son 15 minutos donde te muestro en pantalla cómo se vería el sistema. Sin compromiso. ¿Te parece?"

**Después de colgar (en los siguientes 60 seg):**
1. Presencial → WhatsApp confirmando día, hora y nombre de la óptica.
2. Videollamada → enlace por WhatsApp + recordatorio el día antes.

### El arma secreta: vídeo Loom

Cuando dicen "no me interesa", graba un Loom de 2 min mostrando SU óptica en pantalla y explicando qué diagnosticarías. **Convierte el "no" en reunión el 30% de las veces.** Grabarlo justo después de colgar mientras tienes el contexto fresco.

### 7 reglas de oro (Divisual)

1. La llamada dura menos de 2 minutos — si hablas más, estás vendiendo y vas a perder.
2. Presencial > Videollamada. Siempre (zona sur RM = ventaja competitiva de Saúl).
3. Vendes el diagnóstico/demo, no la implementación.
4. Si eres nuevo, dilo. La sinceridad conecta.
5. Lo concreto gana: "vi que responden WhatsApps a mano" > "podemos mejorar su eficiencia".
6. El "no" rápido es mejor que el "ya te cuento" que nunca llega.
7. Llamar martes a jueves, 10:00-12:00 y 16:00-18:00.
