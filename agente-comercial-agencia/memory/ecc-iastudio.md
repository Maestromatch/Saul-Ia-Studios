# ECC IAStudio

> Adaptacion selectiva del repo `affaan-m/ECC` para Saul IA Studios.

Fuente principal: https://github.com/affaan-m/ECC

## Que es

ECC se presenta como un sistema operativo para trabajo agentico: skills, reglas, agentes, comandos, hooks, memoria persistente, MCP configs, seguridad, research-first development, verificacion, dashboard y optimizacion de contexto.

La metadata revisada declara:
- Plugin Codex: `ecc`, version `2.0.0-rc.1`.
- Paquete npm: `ecc-universal`, version `2.0.0-rc.1`.
- Licencia: MIT.
- Capacidades: lectura, escritura, skills, MCP configs, TDD, seguridad, code review, automation y workflows.

## Lectura estrategica para IAStudio

ECC es demasiado grande para copiar completo en esta fase. El valor no esta en meter 200+ skills de golpe, sino en adoptar el sistema mental:

- Investigar antes de construir.
- Instalar o copiar solo componentes necesarios.
- Mantener memoria por proyecto para evitar contaminacion.
- Convertir aprendizajes repetidos en skills internas.
- Cerrar entregas con verificacion y seguridad.
- Controlar el contexto para sesiones largas.

## Relacion con Superpowers

`obra/superpowers` aporta disciplina de desarrollo:
- spec
- plan
- TDD
- review
- verificacion

ECC aporta capa operacional:
- catalogo de skills
- reglas por lenguaje/herramienta
- research-first
- memoria continua
- seguridad
- optimizacion de contexto
- MCP configs
- dashboards/status

Para IAStudio:
- Superpowers = como ejecutar bien una tarea.
- ECC = como operar un sistema de agentes y memoria a largo plazo.

## Principios adoptados

### 1. Search-first

Antes de construir algo nuevo, decidir:

- Adoptar: si ya existe una solucion buena.
- Extender: si existe una base buena pero necesita ajuste.
- Componer: si 2-3 piezas resuelven mejor que una sola.
- Construir: si no hay opcion adecuada o el servicio exige control propio.

Aplicacion:
- Repos GitHub que entregue el usuario.
- MCPs.
- Workflows n8n.
- Bots WhatsApp.
- Plantillas de landing.
- Automatizaciones de CRM.

### 2. Memoria por scope

No todo aprendizaje debe ser global.

Scopes IAStudio:
- `cliente`: aprendizaje solo valido para un cliente.
- `nicho`: opticas, constructoras, servicios tecnicos, formalizacion.
- `agencia`: regla general de Saul IA Studios.
- `global`: principio reutilizable en cualquier proyecto.

Regla:
- Un aprendizaje se vuelve global solo si se repite en al menos 2 contextos o si es seguridad/operacion basica.

### 3. Instincts manuales

ECC usa "instincts": comportamientos atomicos con trigger, accion, evidencia y confianza.

Adaptacion manual:

```markdown
### Instinct: nombre

- Trigger:
- Accion:
- Scope: cliente / nicho / agencia / global
- Confianza: 0.3 / 0.5 / 0.7 / 0.9
- Evidencia:
- Fuente:
```

Ejemplo:

```markdown
### Instinct: validar secretos antes de entregar

- Trigger: cuando una entrega use APIs, Supabase, n8n, WhatsApp o Vercel.
- Accion: revisar que no existan tokens, claves ni datos sensibles en el repo.
- Scope: global.
- Confianza: 0.9.
- Evidencia: ECC security-review + practica recomendada del stack IAStudio.
- Fuente: affaan-m/ECC `security-review`.
```

### 4. Security review minimo

Antes de entregar recursos con datos o APIs:

- No hardcodear secretos.
- `.env` fuera del repo.
- `.env.example` sin valores reales.
- Validar inputs de formularios/bots.
- No loggear telefonos, tokens ni datos sensibles sin necesidad.
- Revisar permisos de Supabase/RLS cuando aplique.
- Revisar webhooks n8n y URLs publicas.
- Revisar dependencias si hay app con Node/Python.

### 5. Verification loop ligero

Por tipo de recurso:

Landing:
- Abrir local o URL desplegada.
- Revisar CTA WhatsApp.
- Revisar responsive movil.
- Revisar que no haya placeholders.

Bot:
- Ejecutar casos de prueba.
- Probar objeciones.
- Confirmar que captura datos minimos.
- Confirmar handoff humano.

Workflow n8n:
- Ejecutar flujo completo.
- Confirmar credenciales.
- Confirmar registro en CRM/Supabase/Sheet.
- Confirmar manejo de error.

CRM:
- Crear lead de prueba.
- Cambiar estado.
- Registrar seguimiento.
- Exportar o revisar historial.

Documento comercial:
- Revisar ICP.
- Revisar promesa.
- Revisar precio y alcance.
- Revisar siguiente accion.

### 6. Context budget

Para no saturar sesiones:

- Guardar aprendizajes en `memory/` al terminar cada repo.
- No cargar todos los skills de un repo enorme.
- Leer solo README, manifests y skills relevantes.
- Consolidar duplicados cada varios repos.
- Separar investigacion, integracion y resumen.

## Reglas de adopcion

### Se adopta

- Research-first.
- Instincts manuales con scope.
- Security review.
- Verification loop.
- Context budget.
- Skill catalog como inspiracion.

### No se adopta todavia

- Instalacion completa del plugin.
- Hooks globales.
- Dashboard ECC.
- MCP configs externos.
- ECC Pro.
- Automatismos que escriban fuera del proyecto IAStudio.

## Como usar con el proximo repo

1. Leer README, manifest y estructura.
2. Clasificar: adoptar / extender / componer / construir.
3. Extraer 1-3 skills utiles, no mas.
4. Registrar scope y evidencia.
5. Crear recurso IAStudio si aporta valor real.
6. Definir prueba de uso.

## Que gana IAStudio

IAStudio gana un sistema de memoria y operaciones mas serio: no solo acumula links, sino que aprende con criterio, cuida seguridad, evita reinventar y mantiene el contexto liviano.
