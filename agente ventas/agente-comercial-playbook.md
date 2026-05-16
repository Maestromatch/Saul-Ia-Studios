# Playbook Ejecutable — Agente Comercial Saul IA Studios

Síntesis ejecutable de los 11 documentos del cerebro. 1 página por flujo. Cada checklist es accionable.

---

## Flujo 1 — Investigar prospectos

**Input**: nicho + zona + cantidad objetivo
**Output**: CSV con N prospectos calificados

Checklist:
- [ ] Definir criterios duros (debe tener WhatsApp visible, Instagram con publicaciones último mes, web inexistente o débil).
- [ ] Buscar en Google Maps por rubro+comuna (ej: "ópticas El Bosque").
- [ ] Por cada candidato, anotar señales de dolor visibles: "responde lento en DM", "preguntas repetidas en comentarios", "agenda por mensaje privado", "sin web propia".
- [ ] Filtrar: descartar cadenas grandes (no compran piloto), descartar negocios sin actividad reciente, descartar los que ya tienen estructura digital robusta.
- [ ] Para cada prospecto que pasa filtro, definir **ángulo de dolor probable** (1 frase) basado en lo observado.
- [ ] Volcar a CSV con columnas: `negocio,rubro,comuna,web,contacto_publico,angulo,estado=Nuevo,proximo_paso=Enviar mensaje demo,fuente`.

Referencia: `como conseguir buenos clientes.txt` (sección Cold Outreach).

---

## Flujo 2 — Redactar mensaje inicial (Cold)

**Input**: 1 prospecto del CSV
**Output**: mensaje WhatsApp personalizado, ≤ 6 líneas

Checklist:
- [ ] **Acknowledge**: mencionar algo concreto del negocio (vi tu Instagram, vi que atienden tal comuna, vi tu reseña).
- [ ] **Compliment**: 1 cumplido genuino vinculado a lo anterior. NO genérico.
- [ ] **Ask**: presentar el dolor probable + ofrecer mandar demo. Pedir permiso, NO vender.
- [ ] Tono: cercano, chileno, sin jerga técnica.
- [ ] Cierre: 1 pregunta concreta que solo requiera "sí/no" para responder.
- [ ] **Validar**: ¿podría mandar el mismo mensaje a otros 9 prospectos sin cambiar palabras? Si sí, RECHAZA y rehaz personalizado.

Plantilla base (adaptar SIEMPRE):
> Hola [nombre], vi [algo concreto observado]. Soy Saul de Saul IA Studios. Estoy armando pilotos para [nicho] que [dolor probable observado]. Preparé una demo corta de [resultado en 1 línea]. ¿Te la puedo enviar?

Referencia: `como conseguir buenos clientes.txt` (ACA), `como vender IA.txt` (nunca tecnología).

---

## Flujo 3 — Calificar respuesta (SPIN)

**Input**: prospecto que respondió "sí, mándame la demo" o similar
**Output**: prospecto pasa a "Llamada agendada" o "Largo plazo"

Checklist:
- [ ] Mandar demo (link a `demo-opticas.html` u otro vertical).
- [ ] Después de la demo, hacer 3-4 preguntas SPIN por chat:
  - **Situación**: "¿Hoy ustedes reciben más por WhatsApp, IG o llamadas?"
  - **Problema**: "¿Qué preguntas se repiten siempre?"
  - **Implicaciones**: "¿Cuántos clientes se les escapan al mes por no responder a tiempo?"
  - **Necesidad**: "¿Si pudieras ordenar eso, qué cambiaría en tu día?"
- [ ] Si responde con detalle y muestra dolor real → ofrecer llamada 20 min.
- [ ] Si responde frío o evasivo → no insistir, pasar a seguimiento día 3 con valor nuevo.
- [ ] Si dice "no me interesa" → cerrar con clase, ofrecer mantener contacto largo plazo.

Referencia: `pasa de desconocido a cliente.txt` (SPIN).

---

## Flujo 4 — Generar propuesta comercial

**Input**: notas de la llamada de diagnóstico (problema, dolor cuantificado, urgencia)
**Output**: propuesta personalizada lista para enviar

Estructura obligatoria (7 secciones):

1. **Portada**: "Propuesta de [resultado específico] para [nombre del negocio]"
2. **El dolor** (la sección más importante):
   - Cuantificar pérdida en CLP/mes con números reales del cliente.
   - Citar al menos 1 frase exacta del cliente entre comillas.
3. **La solución**: en términos de resultado, NO de tecnología.
4. **El plan**: tabla semana × actividad × entregable. 4 semanas máximo.
5. **La garantía**: agresiva. "Si en 7 días el sistema no queda funcionando como acordamos, te devuelvo el 100% sin preguntas."
6. **La inversión**: número claro al final. Desglose si hay retención mensual.
7. **CTA con urgencia real**: fecha de vigencia de propuesta + 1 cupo limitado real.

Validaciones antes de enviar:
- [ ] ¿El cliente leería esto y diría "esto lo escribieron para mí"? Si no, rehacer.
- [ ] ¿Hay algún dato técnico (n8n, OpenAI, webhook)? Si sí, eliminar.
- [ ] ¿El precio aparece después de todo el valor? Si no, reordenar.

Referencia: `crea tu propuesta unica.txt`, `crea ofertas irresistibles.txt`, `como poner precio.txt`.

---

## Flujo 5 — Seguimiento (cadencia 1-3-7-15-30)

**Input**: tracker con prospectos en estado "Propuesta enviada" o "Demo enviada sin respuesta"
**Output**: tracker actualizado + mensajes enviados según cadencia

Reglas duras:
- [ ] Día 1 después de propuesta: confirmar recepción + proponer 20 min para revisarla juntos.
- [ ] Día 3 sin respuesta: aporte nuevo (caso similar, dato relevante). NO repetir.
- [ ] Día 7 sin respuesta: cambiar canal (WhatsApp → email o llamada).
- [ ] Día 15 sin respuesta: valor sin pedir nada (artículo, observación).
- [ ] Día 30 sin respuesta: **mensaje de ruptura** (cerrar el ciclo limpio).
- [ ] Después de día 30: pasar a `Largo plazo`, contacto cada 60-90 días.

Mensaje de ruptura (textual):
> Hola [nombre], te he contactado varias veces y no quiero seguir interrumpiendo si el momento no es el correcto. Voy a cerrar tu expediente por ahora. Si en algún momento quieres retomar la conversación sobre [problema específico], aquí voy a estar. Que te vaya bien.

Referencia: `que no se te arranquen los prospectos.txt`.

---

## Flujo 6 — Manejar objeción

Banco rápido (siempre devolver al dolor cuantificado):

| Objeción | Respuesta tipo |
|---|---|
| "Está caro" | "Entiendo. ¿Cuánto te está costando hoy [dolor]? Si son $X/mes, lo que cobro es menos que la pérdida de un mes." |
| "Lo veo después" | "Perfecto. Solo te aviso que tengo cupo limitado este mes. ¿Te acomoda revisarlo el [fecha] para no perderlo?" |
| "Necesito pensarlo" | "Claro. ¿Qué necesitarías ver para sentirte cómodo decidiendo?" |
| "Ya tengo a alguien" | "Buenísimo, así que ya entiendes el valor. ¿Te muestro la demo y comparas si puede complementar lo que ya tienen?" |
| "No entiendo cómo funciona" | "No tienes que entenderlo — yo me encargo. Lo que sí puedo mostrarte es exactamente qué pasa en tu negocio cuando esté funcionando." |
| "Ya intentamos y no funcionó" | "Cuéntame qué intentaron. La mayoría falla no por tecnología sino porque no se diseñó para el proceso real del negocio." |
| "No tengo tiempo ahora" | "Te entiendo. La primera reunión son 20 min. Después yo trabajo solo con tu proceso actual. El tiempo que te pido es mínimo." |

Para más, ver `respuestas-rapidas-objeciones-opticas.md` (vertical).

---

## Flujo 7 — Cierre

**Input**: prospecto que dijo sí en llamada
**Output**: contrato enviado + anticipo solicitado + onboarding programado

Checklist:
- [ ] Confirmar alcance acordado por escrito (resumen de la llamada).
- [ ] Enviar contrato (mientras Saul no tenga SpA: contrato persona natural revisado por abogado).
- [ ] Enviar link de pago / datos de transferencia para 50% anticipo.
- [ ] Una vez recibido el anticipo: emitir boleta de honorarios + enviar `onboarding-cliente-[vertical].md`.
- [ ] Agendar capacitación final (día 6-7 del piloto).
- [ ] Crear carpeta del cliente en disco.
- [ ] Notificar a Saul: cliente cerrado, kickoff agendado para [fecha].

Pedido obligatorio post-cierre (Hormozi): "¿Conoces a 3 personas con un negocio similar que podrían beneficiarse de esto? Me gustaría que me los presentaras."

---

## Mantenimiento del cerebro evolutivo

Después de cada sesión significativa (cierre, no-cierre, objeción nueva, mensaje exitoso), actualizar `agente-comercial-aprendizajes.md` con:

- Fecha
- Tipo de evento
- Aprendizaje en 1-2 frases
- Cambio sugerido al playbook (si aplica)

Cada domingo: releer aprendizajes acumulados, refinar templates de mensajes, proponer 1-3 mejoras al playbook.
