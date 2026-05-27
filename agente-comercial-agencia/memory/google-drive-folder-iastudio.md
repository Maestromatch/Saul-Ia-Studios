# Google Drive Folder IAStudio

> Registro de intento de integracion de una carpeta Google Drive entregada por el usuario.

## Fuente

- URL: https://drive.google.com/drive/folders/1PoxECZTHbmA0B6Rndwve_JWQSmzJJiC6?usp=drive_link
- Folder ID: `1PoxECZTHbmA0B6Rndwve_JWQSmzJJiC6`
- Fecha de intento: 2026-05-22
- Tipo: carpeta Google Drive externa
- Estado: pendiente de acceso legible

## Resultado del intento

El enlace no se pudo leer desde acceso web directo. Google Drive puede requerir permisos, sesion autenticada, cookies o interfaz JavaScript aunque el link exista.

Por seguridad y trazabilidad, esta fuente queda registrada como pendiente. No se debe afirmar que el contenido fue integrado hasta poder leer los archivos reales.

## Como continuar

Opciones validas:

1. Cambiar permisos de la carpeta a "Anyone with the link can view" y volver a enviar el link.
2. Descargar la carpeta como ZIP y dejarla en una ruta local accesible, por ejemplo `C:\Users\Usuario 01\Documents\Downloads\...`.
3. Copiar los archivos relevantes dentro de `IAStudio_Lanzamiento\_inbox\` o una carpeta equivalente.
4. Enviar enlaces directos a archivos individuales de Google Docs/PDF/TXT si el folder completo no lista contenido.
5. Pegar aqui el indice de archivos para priorizar que analizar primero.

## Protocolo de ingesta cuando haya acceso

1. Listar archivos y tipos: docs, pdf, txt, imagenes, videos, hojas, prompts, zips.
2. Clasificar cada archivo:
   - memoria,
   - oferta,
   - SOP,
   - prompt,
   - skill,
   - asset visual,
   - automatizacion,
   - cliente,
   - pendiente/descartar.
3. Extraer solo lo reusable para IAStudio.
4. Crear fichas de memoria por tema si hay capacidades nuevas.
5. Actualizar `habilidades.md`, `evolucion.md` y `observations-index.md`.
6. No guardar secretos, telefonos privados, credenciales, datos sensibles o contenido de cliente sin sanitizar.

## Regla anti-confusion

Este archivo registra el enlace y el estado de acceso, no el contenido del Drive.

Cuando el contenido se pueda leer, crear una nueva entrada de integracion con estado `Integrado` y citar archivos concretos.

## Que ganamos por ahora

IAStudio gana un protocolo para tratar carpetas Drive como fuentes de memoria sin mezclar "link recibido" con "contenido integrado". Esto evita perder trazabilidad y evita inventar capacidades que todavia no fueron leidas.
