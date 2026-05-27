# Override - Dashboard CRM

## Objetivo

Mostrar al cliente que sus leads estan ordenados, priorizados y con proximo paso claro.

## Patron

- `Sales Intelligence Dashboard`
- `Real-Time Monitoring` si hay bot o WhatsApp activo.

## Informacion prioritaria

- Leads nuevos.
- Leads calificados.
- Cotizaciones pendientes.
- Seguimientos vencidos.
- Tiempo promedio de respuesta.
- Fuente del lead.
- Proximo paso.
- Valor potencial cuando exista.

## Componentes recomendados

- Filtros por estado, fuente y fecha.
- Tabla densa pero legible.
- Cards de metricas solo para KPIs accionables.
- Chips de estado.
- Panel lateral de detalle del lead.
- Timeline de interacciones.

## Reglas visuales

- Denso pero ordenado.
- No usar graficos si no ayudan a decidir.
- Estados deben ser consistentes.
- Proximo paso debe estar mas visible que decoracion.

## Checklist especifico

- Un usuario debe entender que atender primero en menos de 10 segundos.
- Cada lead debe tener responsable o siguiente accion.
- No mostrar datos sensibles innecesarios.
- Responsive: en mobile priorizar lista por estado sobre tabla completa.
