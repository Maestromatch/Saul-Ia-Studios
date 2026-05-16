# SOP de implementacion - Piloto optica

## Fase 1 - Preparacion

Entrada:
- Anticipo recibido (boleta de honorarios o factura emitida).
- Onboarding completado (cuestionario lleno).
- Accesos basicos: numero WhatsApp Business, link Instagram, Google Calendar si aplica.

Acciones:
- Crear carpeta del cliente: `IAStudio_Lanzamiento/clientes/[nombre-optica]/`.
- Crear copia del CRM template (Google Sheets) y compartir con el cliente con permisos de edicion.
- Definir version del paquete: basico, recomendado o completo.
- Revisar tono y reglas de respuesta acordadas en onboarding.
- Confirmar fechas de capacitacion.

Salida:
- Alcance confirmado por escrito (correo de inicio).
- Preguntas frecuentes clasificadas por categoria.

## Fase 2 - Diseno del flujo

Crear flujo base:

1. Saludo + identificacion del tipo de consulta (lente nuevo / examen / reparacion / convenio / otra).
2. Si es lente nuevo: pregunta tipo (opticos con receta / sol / contacto).
3. Si es opticos con receta: pregunta si tiene receta vigente o necesita examen.
4. Captura: nombre, telefono, comuna, convenio (Isapre / Caja / particular), horario que prefiere.
5. Si pidio agenda: confirma horario disponible y registra cita.
6. Derivacion a humano para casos delicados (recetas complejas, reclamos, ventas grandes).
7. Registro del caso en CRM con estado y proximo paso.

Reglas:
- No prometer descuentos no autorizados.
- No dar diagnostico visual.
- No inventar precios finales (solo "desde").
- No prometer plazo de entrega exacto sin validar stock.
- Derivar siempre reclamos y problemas con compras anteriores.

## Fase 3 - Construccion

Entregables:
- Base de respuestas por categoria (precios, convenios, marcas, tiempos, garantia).
- CRM simple con dropdown de estados.
- Landing/formulario si aplica (con boton WhatsApp y formulario de agendamiento).
- Mensajes de seguimiento (confirmacion, recordatorio 24h, recuperacion, post-venta).
- Mini dashboard si aplica.
- Integracion con Google Calendar si aplica.

Pruebas obligatorias:
- Caso 1: cliente quiere examen visual y agendar.
- Caso 2: cliente cotiza multifocales (precio desde + derivacion a humano).
- Caso 3: cliente con Isapre pregunta cobertura.
- Caso 4: cliente quiere reparar marco.
- Caso 5: cliente fuera de comuna pregunta entrega.
- Caso 6: cliente molesto por compra anterior (debe derivar humano de inmediato).

## Fase 4 - Capacitacion

Sesion 1 (60 min, antes de lanzar):
- Tour del CRM.
- Como revisar nuevos leads.
- Como cambiar estados.
- Como confirmar/reagendar citas.
- Que puede y no puede hacer la IA.
- Como reportar fallas del flujo.

Sesion 2 (30 min, dia 5-7 del piloto):
- Revision de casos reales.
- Ajustes a respuestas que no funcionaron.
- Definicion de mejoras para mantencion mensual.

## Fase 5 - Cierre

Checklist final:
- [ ] Flujo probado con 6 casos reales.
- [ ] CRM creado y poblado con leads de la primera semana.
- [ ] Mensajes de seguimiento listos y aprobados.
- [ ] Cliente capacitado (sesiones 1 y 2 hechas).
- [ ] 7 dias de ajustes explicados.
- [ ] Pago final solicitado y emitida la boleta/factura.
- [ ] Testimonio pedido en video.
- [ ] Pedido de 3 referidos hecho explicitamente.

## Solicitud de testimonio

Mensaje:

Gracias por confiar en Saul IA Studios. Para seguir mejorando y mostrar casos reales, ¿me podrias dejar un testimonio corto en video (40-60 segundos) sobre como fue la implementacion, que problema te ayudo a ordenar y que cambio en estos 7 dias? Con eso me ayudas mucho a llegar a otras opticas.

## Pedido de referidos

Mensaje (Hormozi - "presentacion directa a tres"):

Antes de cerrar, una ultima cosa: ¿conoces a 3 opticas o negocios similares que podrian beneficiarse de esto? Me gustaria que me los presentaras. Por cada uno que se transforme en cliente, te doy un mes de mantencion gratis (o el equivalente que prefieras).
