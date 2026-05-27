# Fuentes Drive Integradas - IAStudio

> Carpetas y archivos de Google Drive recibidos para convertir en memoria operativa.

## Tabla maestra

| Fecha | Fuente | Tipo | Estado | Integracion | Pendiente |
| --- | --- | --- | --- | --- | --- |
| 2026-05-22 | https://drive.google.com/drive/folders/1PoxECZTHbmA0B6Rndwve_JWQSmzJJiC6?usp=drive_link | Carpeta Drive | Pendiente de acceso | Registrado como fuente pendiente en `memory/google-drive-folder-iastudio.md` | Habilitar acceso publico o compartir archivos individuales |
| 2026-05-25 | https://drive.google.com/drive/folders/1M4N2tXA3vW-yWPgeng2CcF9Hn95Zn20p | Carpeta Drive pública — La Tribu Divisual | ACCEDIDO — archivos listados, binarios pendientes descarga | 15 recursos clasificados en `memory/la-tribu-recursos-iastudio.md` (7 JSONs n8n, 4 PDFs, 1 docx, 1 Google Doc, 12 carpetas video) | Saúl descarga archivos a `_inbox/la-tribu/` y avisa a Claude para procesar |

## Regla

- No marcar como integrado si no se leyeron archivos.
- Mantener folder ID, fecha y estado.
- Al tener acceso, listar archivos antes de extraer contenido.
- Sanitizar datos sensibles antes de persistir aprendizajes.
