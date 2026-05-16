# Flujo del bot — [NOMBRE_OPTICA]

> Base: `../../../sop-entrega-piloto-opticas.md` Fase 2.

## Saludo + identificación

```
Hola, soy el asistente de [NOMBRE_OPTICA]. ¿Te ayudo con?
1️⃣ Lente nuevo
2️⃣ Examen visual
3️⃣ Reparación
4️⃣ Convenios / FONASA / Isapre
5️⃣ Otra consulta
```

## Ruta 1 — Lente nuevo

Pregunta tipo:
- Ópticos con receta
- Lentes de sol
- Lentes de contacto

Si ópticos con receta:
- ¿Tiene receta vigente?
  - Sí → seguir a captura
  - No → ofrecer agendar examen

## Ruta 2 — Examen visual

Captura: nombre, teléfono, comuna, fecha/hora preferida → confirmar cupo desde Google Calendar.

## Ruta 3 — Reparación

Pedir foto del marco + datos contacto → derivar a humano para cotización.

## Ruta 4 — Convenios

Responder lista de convenios del cliente. NO inventar.

## Ruta 5 — Otra / casos delicados

Derivar a humano de inmediato:
- Recetas complejas / problemas visuales
- Reclamos
- Garantías en curso
- Compras anteriores

## Captura estándar (al final de cualquier ruta de compra/examen)

- Nombre:
- Teléfono:
- Comuna:
- Convenio (Isapre/Caja/particular):
- Horario que prefiere:

## Reglas duras (no negociar)

- ❌ NO dar diagnóstico visual
- ❌ NO inventar precios finales (solo "desde")
- ❌ NO prometer plazo exacto sin validar stock
- ❌ NO prometer descuentos no autorizados
- ✅ SIEMPRE derivar reclamos y garantías

## Mensajes automáticos del cliente al lead

- Confirmación de captura:
- Recordatorio 24h antes de cita:
- Recuperación 48h sin respuesta:
- Post-venta (día +3 tras entrega):
