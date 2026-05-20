# Protocolo de memoria y verificacion — Saul IA Studios

> Basado en `memory/` y adoptado como regla operativa del proyecto.

## Objetivo

Evitar que la agencia crezca por intuicion dispersa. Cada aprendizaje, repo, servicio o cambio debe transformarse en una capacidad reutilizable.

## Regla de lectura

Antes de cambios grandes:

1. Leer `memory/observations-index.md`.
2. Abrir solo el archivo de detalle relevante.
3. Revisar `design-system/MASTER.md` si el cambio toca UI.
4. Ejecutar cambio.
5. Verificar con evidencia.
6. Registrar aprendizaje si aplica.

## Capas de memoria

### Capa 1 — Indice

Archivo:
- `memory/observations-index.md`

Uso:
- Ver IDs y decidir que leer.
- No cargar memoria larga sin necesidad.

### Capa 2 — Timeline

Archivo:
- `memory/evolucion.md`

Uso:
- Entender secuencia de decisiones.
- Ver que cambio y que queda pendiente.

### Capa 3 — Detalle

Archivos:
- `memory/habilidades.md`
- `memory/repos-github.md`
- `memory/*.md`
- `design-system/MASTER.md`
- `design-system/pages/*.md`

Uso:
- Aplicar protocolo, diseno, seguridad o habilidad especifica.

## Reglas adoptadas de memoria

- No guardar secretos.
- No copiar repos por copiar.
- Convertir repos en SOP, plantilla, oferta, skill, demo o checklist.
- Agregar observacion nueva cuando haya aprendizaje reusable.
- Mantener trazabilidad: fuente -> decision -> recurso creado.

## Protocolo de ejecucion agentica

Antes de implementar:

1. Diagnosticar.
2. Definir objetivo.
3. Crear plan corto.
4. Ejecutar.
5. Verificar.
6. Documentar.

## Verificacion por tipo

### Landing / UI

- Revisar `design-system/MASTER.md`.
- Revisar override si existe.
- Validar copy repetido.
- Validar mobile.
- Validar links.
- Validar CTA.

### Servicio / oferta

- Debe tener promesa.
- Precio.
- Para quien.
- Incluye/no incluye.
- Onboarding.
- SOP.
- Criterio terminado.
- Upsell natural.

### Workflow / automatizacion

- No hardcodear tokens.
- QA end-to-end.
- Logs o evidencia.
- Credenciales en `.local.md` o n8n credentials.
- Plan de rollback.

### Prospeccion / ventas

- ICP claro.
- Mensaje por nicho.
- CRM actualizado.
- Estado y proximo paso.
- Learning log.

## Cuando actualizar memoria

Actualizar si:

- nace un servicio nuevo.
- se integra un repo.
- cambia el modelo de agencia.
- aparece un riesgo.
- se valida una hipotesis comercial.
- se crea un proceso reutilizable.

## Formato de actualizacion

1. Agregar fila a `memory/observations-index.md`.
2. Agregar detalle a `memory/evolucion.md` o archivo especifico.
3. Si aplica, actualizar `memory/habilidades.md`.

## Regla final

La agencia mejora cuando cada ciclo deja un activo reutilizable.

Si una accion no deja aprendizaje, venta, entrega o reduccion de error, se esta acumulando ruido.
