# Aetria Studio - Reglas activas del proyecto

## Stack

Next.js + Vercel. Dominio objetivo: `aetriastudio.cl`.

Nota operativa: el repo actual aun contiene HTML estatico. Mientras no exista estructura Next.js, las rutas publicas se implementan como carpetas estaticas compatibles con Vercel, por ejemplo `/privacidad/index.html` y `/terminos/index.html`.

## Identidad

- Agencia IA en Santiago.
- Tono: directo, sin adornos, espanol chileno.
- Color base: `#111111`.
- No agregar animaciones pesadas ni librerias nuevas.

## Lo que NO hacer

- No inventar metricas ni nombres de clientes.
- No cambiar el copy existente sin instruccion explicita.
- No romper secciones que ya funcionan.

## Pendientes activos

1. Reemplazar dominio en canonical, og:url y meta-author.
2. Agregar seccion testimonios con foto + nombre + resultado.
3. Crear seccion "Quien soy" con foto y LinkedIn.
4. Agregar Calendly como segundo CTA en hero y footer.
5. Crear `/privacidad` y `/terminos` con Ley 19.628 chilena.
6. Reemplazar rangos de precio por tabla comparativa.
7. Convertir "Laboratorio operativo" en caso de estudio real.

## Modulos mentales en raiz

- `agente-desarrollo-personal/`: modulo de desarrollo personal, memoria, patrones y compromisos del fundador.
- `agente-desarrollo-personal-INTEGRACION-AETRIA.md`: reglas de uso dentro de la mente de agencia.

Regla: no subir audios, transcripciones, embeddings, bases SQLite ni datos personales sensibles si contienen informacion privada.
