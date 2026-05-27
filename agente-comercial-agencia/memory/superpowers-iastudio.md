# Superpowers IAStudio

> Adaptacion operativa del repo `obra/superpowers` para Saul IA Studios.

Fuente principal: https://github.com/obra/superpowers

## Que es

`superpowers` es un framework de habilidades y metodologia para agentes de desarrollo. Su idea central es que el agente no debe improvisar: primero entiende la intencion, luego disena una especificacion, despues arma un plan ejecutable, implementa con pruebas, revisa y recien al final declara listo con evidencia.

La version revisada del plugin declara version `5.1.0`, licencia MIT y soporte para entornos como Claude Code, Codex CLI, Codex App, Gemini CLI, OpenCode, Cursor y GitHub Copilot CLI.

## Por que importa para IAStudio

Saul IA Studios necesita vender y entregar rapido, pero sin perder control. Este repo aporta una forma de convertir ideas, repos y solicitudes de clientes en un sistema de ejecucion:

- Menos improvisacion al construir landings, bots, CRMs o workflows.
- Mas claridad antes de tocar archivos.
- Mejor separacion entre idea, spec, plan, ejecucion, review y entrega.
- Evidencia antes de decir "listo".
- Capacidad de crear skills internas propias para repetir servicios.

## Flujo adoptado

### 1. Diagnostico antes de construir

Usar cuando una solicitud sea ambigua, creativa o importante para cliente.

Salida esperada:
- Objetivo de negocio.
- Usuario final o cliente.
- Restricciones.
- Que cuenta como exito.
- Que no se hara en esta version.

Aplicacion IAStudio:
- Nuevo servicio.
- Nueva landing.
- Nuevo bot.
- Nueva automatizacion.
- Nueva plantilla comercial.

### 2. Spec corta

Antes de implementar, escribir una mini-spec cuando el trabajo tenga riesgo o multiples pasos.

Debe incluir:
- Problema.
- Solucion propuesta.
- Archivos a tocar.
- Flujo de usuario o proceso.
- Riesgos.
- Criterios de aceptacion.

Ubicacion recomendada:
- Para agencia: `memory/evolucion.md` o un archivo nuevo en `memory/`.
- Para cliente: `clientes/NOMBRE_CLIENTE/02-construccion/`.

### 3. Plan ejecutable

Convertir la spec en tareas pequenas.

Cada tarea debe decir:
- Archivo exacto.
- Cambio exacto.
- Como probar.
- Resultado esperado.

Regla IAStudio:
- Si el agente no puede verificar una tarea, la tarea esta mal definida.

### 4. Ejecucion con pruebas

Para codigo o automatizaciones, aplicar el espiritu TDD:

- Primero definir el caso que debe pasar.
- Ver que falla o que no existe.
- Implementar lo minimo.
- Verificar que pasa.
- Refactorizar solo despues.

No todo servicio de agencia requiere test automatizado. Pero todo servicio requiere prueba:
- Landing: abrir y revisar responsive/CTA.
- Bot: correr casos de prueba.
- Workflow n8n: probar ejecucion real o mock.
- CRM: probar alta, estado y seguimiento.
- Copy/oferta: revisar contra ICP y objeciones.

### 5. Review en dos capas

Antes de cerrar una entrega relevante:

1. Review de cumplimiento: lo hecho cumple la spec.
2. Review de calidad: lo hecho esta limpio, entendible, usable y sin deuda innecesaria.

Aplicacion IAStudio:
- En codigo: revisar diff, comportamiento y build.
- En comercial: revisar coherencia con oferta, nicho y siguiente accion.
- En cliente: revisar que no haya placeholders, datos falsos ni promesas imposibles.

### 6. Verificacion antes de cierre

No decir "listo" sin evidencia fresca.

Evidencias aceptadas:
- Comando ejecutado con exito.
- Captura o revision visual.
- Checklist de casos pasado.
- Link desplegado y probado.
- Registro en CRM actualizado.
- Mensaje/copy revisado contra objetivo.

Frases prohibidas sin evidencia:
- "deberia funcionar"
- "parece listo"
- "quedo ok"
- "lo mas probable es que pase"

## Como usarlo con repos nuevos

Cuando el usuario pase un repo:

1. Registrar repo en `memory/repos-github.md`.
2. Identificar si aporta codigo, metodo, prompt, plantilla, workflow o idea comercial.
3. Extraer una habilidad concreta.
4. Crear o actualizar recurso IAStudio.
5. Registrar que ganamos en `memory/evolucion.md`.
6. Definir una prueba real para validar el aprendizaje.

## Como usarlo con clientes

### Antes de vender

- Convertir dolor en mini-spec comercial.
- Definir resultado prometible en 7 dias.
- Separar oferta de entrada vs paquete grande.

### Durante construccion

- Trabajar por tareas pequenas.
- Probar cada pieza antes de avanzar.
- Guardar decisiones en carpeta de cliente.

### Antes de entregar

- Correr checklist.
- Registrar evidencia.
- Pedir testimonio si el cliente confirma valor.

## Skills internas a crear despues

Prioridad sugerida:

1. `auditoria-whatsapp-express`
2. `setup-identidad-meta-legal`
3. `landing-demo-nicho`
4. `bot-faq-leads-whatsapp`
5. `workflow-n8n-lead-alerta-seguimiento`

Cada skill interna debe tener:
- Cuando usarla.
- Inputs necesarios.
- Pasos.
- Entregable.
- Checklist de verificacion.
- Archivo fuente o ejemplo.

## Limites de la adopcion

- No se copia el framework completo dentro del proyecto.
- No se asume que el plugin esta instalado en Codex.
- No se fuerza TDD dogmatico en documentos comerciales simples.
- No se agregan procesos largos cuando la tarea es chica y de bajo riesgo.
- La regla central si se mantiene: pensar, planificar, ejecutar y verificar con evidencia.

## Resumen operativo

Superpowers se adopta como disciplina de ejecucion. Para IAStudio, esto significa pasar de "usar IA para hacer cosas" a "tener un sistema para que agentes produzcan entregables confiables".
