# 6 casos de prueba obligatorios

> Base: `../../../sop-entrega-piloto-opticas.md` Fase 3. **No entregar sin pasar los 6.**

## Caso 1 — Cliente quiere examen visual y agendar

| Item | Resultado esperado | OK |
|---|---|---|
| Bot identifica intención | Ruta "examen visual" | ☐ |
| Captura: nombre, teléfono, comuna, horario | Los 4 campos | ☐ |
| Confirma cupo desde Google Calendar | Sí, con fecha y hora | ☐ |
| Crea evento en calendar del cliente | Sí | ☐ |
| Manda recordatorio 24h antes | Programado | ☐ |

**Transcripción real del test**:
```

```

## Caso 2 — Cotiza multifocales

| Item | Resultado esperado | OK |
|---|---|---|
| Bot da precio "desde" | NO precio final | ☐ |
| Pregunta si tiene receta | Sí | ☐ |
| Deriva a humano para precio exacto | Sí, con nombre del encargado | ☐ |
| Registra el lead en CRM | Sí, estado "cotizando" | ☐ |

```

```

## Caso 3 — Cliente con Isapre pregunta cobertura

| Item | Resultado esperado | OK |
|---|---|---|
| Bot responde si trabaja esa Isapre | Sí/No claro | ☐ |
| Si sí, explica proceso (orden médica, bonificación) | Sí | ☐ |
| Si no, no inventa cobertura | Sí | ☐ |

```

```

## Caso 4 — Reparar marco

| Item | Resultado esperado | OK |
|---|---|---|
| Pide foto del marco | Sí | ☐ |
| Captura datos contacto | Sí | ☐ |
| Deriva a humano para cotización | Sí | ☐ |
| NO promete precio sin ver | Sí | ☐ |

```

```

## Caso 5 — Fuera de comuna pregunta entrega

| Item | Resultado esperado | OK |
|---|---|---|
| Bot consulta comuna del cliente | Sí | ☐ |
| Responde si atienden esa comuna | Sí | ☐ |
| Si entrega a domicilio, lo explica | Sí | ☐ |

```

```

## Caso 6 — Cliente molesto por compra anterior

| Item | Resultado esperado | OK |
|---|---|---|
| Bot detecta reclamo | Sí, palabras clave | ☐ |
| Deriva a humano de INMEDIATO | Sí, sin pedir más datos | ☐ |
| NO intenta resolver | Sí, escalado limpio | ☐ |
| Manda mensaje empático mientras llega humano | Sí | ☐ |

```

```

## Cierre

Solo si los 6 están OK → pasar a Fase 4 (Capacitación).
