# SOP — Cómo subir fotos/videos de clientes para publicar via Zernio

> AetriaStudio · Versión 1.0 · Mayo 2026

---

## Problema que resuelve este SOP

Instagram API rechaza URLs de Google Drive, Dropbox, OneDrive e iCloud.
Cuando el cliente manda fotos por WhatsApp o las tiene en Drive, hay que subirlas
a una URL CDN directa antes de pasarlas a Zernio para publicar.

---

## Opción A — Supabase Storage (RECOMENDADA para producción)

Supabase URLs funcionan de forma nativa con Zernio. No requiere configuración extra.

### Paso 1 — Subir la foto a Supabase

En Supabase dashboard (supabase.com/dashboard):
1. Ir al proyecto → Storage → Bucket del cliente (ej: `carneslolol-media`)
2. Click "Upload file" → subir la imagen desde el PC
3. Click en el archivo subido → "Get URL" → copiar la URL pública

Formato URL resultante:
```
https://[proyecto].supabase.co/storage/v1/object/public/[bucket]/[archivo.jpg]
```

### Paso 2 — Usar la URL en /post-contenido

```
/post-contenido "descripcion del contenido" --url [URL_SUPABASE] --client carneslolol --platforms instagram,gmb
```

### Crear bucket para cliente nuevo

```sql
-- En Supabase SQL Editor:
INSERT INTO storage.buckets (id, name, public) VALUES ('carneslolol-media', 'carneslolol-media', true);
```

O desde el dashboard: Storage → New bucket → nombre: `carneslolol-media` → activar "Public bucket".

---

## Opción B — Zernio Media Upload (más rápida, sin Supabase)

Zernio tiene su propio endpoint de upload. El archivo se sube temporalmente y
Zernio devuelve una URL que puede usar directamente para publicar.

### Via Zernio MCP en Claude Code

```
Sube este archivo a Zernio para usarlo en una publicación:
archivo: C:\path\al\archivo\foto.jpg
cliente: carneslolol
```

Claude Code usará el Zernio MCP para subir y devolver la URL.

### Via API directa (para n8n o scripts)

```bash
curl -X POST https://api.zernio.com/v1/media/upload \
  -H "Authorization: Bearer sk_TU_CLAVE" \
  -F "file=@foto.jpg"
```

Respuesta:
```json
{ "url": "https://media.zernio.com/uploads/xxx/foto.jpg", "mediaId": "..." }
```

Usar esa URL en el paso de createPost.

---

## Opción C — CDN pública directa

Si el cliente ya tiene las fotos en su web o en algún CDN accesible, se puede
usar la URL directa sin subir nada.

**Verificación rápida:** abrir la URL en ventana de incógnito.
- Si abre el archivo directo (imagen/video) → ✓ funciona
- Si abre una página web → ✗ no funciona, hay que subirla

---

## Flujo recomendado por caso

| Caso | Solución |
|---|---|
| Cliente manda foto por WhatsApp | Descargar → subir a Supabase → usar URL |
| Cliente tiene carpeta en Drive | Descargar desde Drive → subir a Supabase → usar URL |
| Foto en Instagram del cliente | Screenshot o usar IG Graph API → subir a Supabase |
| Foto ya en CDN del cliente | Verificar en incógnito → usar URL directa |
| Urgente, sin acceso a Supabase | Upload via Zernio MCP → usar URL temporal |

---

## Checklist antes de publicar

- [ ] URL de la foto/video abre el archivo directo (no una página web) en incógnito
- [ ] Imagen: JPEG o PNG, máximo 8MB
- [ ] Video: MP4 o MOV, máximo 300MB (feed), 100MB (story)
- [ ] Reel: vertical 9:16, máximo 90 segundos, H.264, 30fps
- [ ] Caption Instagram: primeros 125 caracteres tienen el CTA o gancho principal
- [ ] Caption GMB: más formal, máximo 1.500 caracteres
- [ ] Precios verificados con el cliente antes de publicar
- [ ] Publicación revisada en --draft antes de publicar en cuentas activas

---

## Errores comunes y solución rápida

| Error Zernio | Causa | Fix |
|---|---|---|
| "No se puede procesar el video desde esta URL" | URL de Drive/Dropbox | Subir a Supabase |
| "Error al obtener archivo, reintentando..." | URL no pública o detrás de redirect | Verificar URL en incógnito |
| "Instagram bloqueó la solicitud" | Detección de automatización | Reducir frecuencia, variar contenido |
| "Contenido duplicado" | Post idéntico reciente | Cambiar caption o foto |
| "Token caducado" | OAuth expirado | Reconectar cuenta en Zernio dashboard |

---

## Buckets Supabase por cliente

| Cliente | Bucket | Plataformas |
|---|---|---|
| Carnes Lolol | `carneslolol-media` | Instagram, GMB |
| Saúl el Constructor | `constructor-saul-media` | Instagram |
| [Nuevo cliente] | `[nombre]-media` | Crear al onboardear |

---

## Notas de seguridad

- Los buckets deben ser **públicos** para que Instagram API pueda leerlos.
- No subir documentos privados ni datos de clientes a estos buckets.
- Usar solo para medios de publicación (fotos/videos de productos/local).
