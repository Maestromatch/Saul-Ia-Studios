# Zernio Motor — AetriaStudio
# Motor de publicacion automatica de contenido para clientes

> Servicio interno y vendible.
> Fuente: Guia "Publica en Piloto Automatico con Zernio" (@diegoampuero2)
> Actualizado: 2026-05-24

---

## Que es Zernio y por que lo usa AetriaStudio

Zernio es un publicador omnicanal que centraliza la distribucion de contenido.
Con una sola integracion, publicamos automaticamente en 14+ plataformas.

Al conectarlo con Claude Code via MCP, el proceso se vuelve completamente autonomo:
- Claude genera el contenido adaptado por plataforma y tono del cliente.
- Zernio lo distribuye a todas las redes conectadas del cliente.
- Todo sin trabajo manual, sin copy-paste, sin errores de formato.

### Plataformas disponibles

Instagram, TikTok, Facebook, YouTube, LinkedIn, X (Twitter), Threads,
Bluesky, Pinterest, Reddit, Google Business, WhatsApp Status,
Telegram, Discord.

### Ventaja para AetriaStudio

Un solo plan Zernio Pro cubre multiples clientes.
El costo por cliente es marginal (~USD 10-15/mes).
El precio de venta del servicio de gestion mensual: $99.000-$299.000 CLP.
Margen del componente Zernio: ~90%.

---

## Setup tecnico — Conexion Zernio + Claude Code MCP

### PASO 1 — Configurar MCP en Claude Code

Ejecutar en terminal:
```bash
claude mcp add zernio --sse "https://mcp.zernio.com/sse" --header "Authorization: Bearer TU_API_KEY"
```

O crear/editar el archivo `.mcp.json` en el proyecto:
```json
{
  "mcpServers": {
    "zernio": {
      "type": "sse",
      "url": "https://mcp.zernio.com/sse",
      "headers": {
        "Authorization": "Bearer TU_API_KEY_ZERNIO"
      }
    }
  }
}
```

API key: obtener en zernio.com/dashboard → API Keys → Generate New Key.
Formato: empieza con 'sk_...' (no 'zrn_' como indica la guia antigua).

### PASO 2 — Verificar conexion

En Claude Code escribir:
```
"Usa Zernio para listar mis cuentas conectadas"
```

Si responde con la lista de redes conectadas → instalacion exitosa.

### PASO 3 — Conectar cliente en Zernio dashboard

Para cada cliente nuevo:
1. Ir a zernio.com/dashboard/connections.
2. Click en "Add connection" → seleccionar plataforma.
3. OAuth: iniciar sesion con las credenciales del cliente.
4. Aprobar permisos.
5. Verificar check verde en la lista.

Permisos requeridos:
- Instagram/Facebook: cuenta de empresa + acceso Meta Business Suite.
- Google Business: cuenta Google con perfil reclamado y verificado.
- TikTok: cuenta business con API habilitada.

---

## Skill /post-contenido — Comando de publicacion

Archivo: `~/.claude/commands/post-contenido.md`

Uso:
```
/post-contenido "foto de vitrina con pechuga entera" --client carneslolol --platforms instagram,gmb
/post-contenido --file foto.jpg --client constructor-saul --platforms instagram
/post-contenido --schedule "2026-05-30 10:00" --client carneslolol
/post-contenido --draft --client carneslolol
```

### Pipeline completo del comando

1. Recibe descripcion, archivo o URL del contenido.
2. Claude identifica el cliente y carga su perfil de tono y marca.
3. Claude genera captions adaptados por plataforma.
4. Zernio MCP publica en todas las plataformas del cliente.
5. Claude devuelve URL de cada publicacion + metricas iniciales.
6. Supabase registra el post (opcional, si el cliente tiene CRM activo).

---

## Workflows predefinidos para clientes locales

### Workflow LUNES — Oferta de semana

Prompt:
```
"Usando Zernio, publica en Instagram y Google Business de [CLIENTE]:
la oferta de la semana es [PRODUCTO] a $[PRECIO]. Tono: barrio, cercano,
invita a ir al local o escribir por WhatsApp. Incluir CTA y hashtags locales."
```

### Workflow VIERNES — Especial fin de semana

Prompt:
```
"Usando Zernio, programa para el viernes a las 11am en Instagram y Facebook
de [CLIENTE]: especial para el fin de semana. Producto: [DESCRIPCION].
Incluir horarios y direccion."
```

### Workflow FECHA ESPECIAL

Prompt:
```
"Usando Zernio, crea y publica un post de [OCASION] para [CLIENTE].
Tono festivo pero autentico. Mencionar los anos en el barrio si aplica.
Publicar en Instagram y Facebook."
```

### Workflow REPURPOSING — Reutilizar contenido

Prompt:
```
"Toma el post de mejor engagement de [CLIENTE] del ultimo mes en Zernio,
adapta el mensaje para la proxima semana con producto distinto,
y programalo para el lunes a las 10am."
```

---

## Plantilla de prompt base por cliente

### Carnes Lolol

```
Eres el community manager de Carnes Lolol, carniceria tradicional en El Bosque,
mas de 20 anos en el barrio. Tono: vecino a vecino, simple, directo, sin jerga
tecnica. CTA siempre a WhatsApp (9 7999 9709) o al local. Hashtags locales:
#carneslolol #carniceriaelBosque #elBosqueRM #carnesChile.
```

### Saul el Constructor

```
Eres el community manager de Constructor Saul SpA, constructora en El Bosque
con 12+ anos de experiencia. Tono: profesional pero cercano, confiable,
muestra el trabajo real. CTA siempre a WhatsApp o cotizacion. Hashtags:
#constructorsaul #remodelacioneschile #construccionelBosque #maestrosRM.
```

---

## Costos y precios del servicio

### Costos internos AetriaStudio

| Item | Costo |
|---|---|
| Zernio Pro (plan agencia) | USD ~29-49/mes (cubre todos los clientes) |
| Tiempo setup por cliente | 3-5 horas (incluido en setup fee) |
| Tiempo gestion mensual por cliente | 2-4 horas |
| Claude Code (ya incluido en plan) | $0 adicional |

### Precios de venta al cliente

| Servicio | Precio |
|---|---|
| Setup Zernio + conexion cuentas | Incluido en Oferta 2 Carniceria Local Express |
| Gestion mensual 8 posts | $79.000 CLP/mes |
| Gestion mensual 12-16 posts | $129.000 CLP/mes |
| Gestion mensual 20+ posts + Google Business | $199.000 CLP/mes |
| Calendario editorial mensual completo | $249.000 CLP/mes |

---

## Checklist de onboarding de cliente en Zernio

- [ ] Cliente tiene cuenta Instagram de empresa (no personal).
- [ ] Cliente tiene acceso a Meta Business Suite.
- [ ] Google Business reclamado y verificado.
- [ ] WhatsApp Business configurado (si aplica).
- [ ] Credenciales recibidas del cliente para OAuth.
- [ ] Conexion Instagram verificada en Zernio (check verde).
- [ ] Conexion Google Business verificada en Zernio (check verde).
- [ ] Test de publicacion realizado (borrador o post real).
- [ ] Banco inicial de 5+ fotos reales recibidas del cliente.
- [ ] Prompt base del cliente creado en archivo de perfil.
- [ ] Calendario editorial del primer mes aprobado.
- [ ] Cliente informado del proceso de aprobacion de posts.

---

## Integracion con el stack actual de AetriaStudio

```
Google Drive (cliente sube foto)
         ↓
n8n detecta archivo nuevo
         ↓
Claude Code analiza foto + genera captions con prompt del cliente
         ↓
Zernio MCP publica en Instagram + Google Business + Facebook
         ↓
Supabase registra: cliente, plataforma, fecha, URL publicacion
         ↓
Dashboard de metricas semanal (opcional)
```

Zernio reemplaza el uso directo de la Instagram Graph API en el Publicador Tanque V7.
Esta es la base del Publicador Tanque V8 mencionado en el catalogo de servicios.

---

## Clientes activos en Zernio (AetriaStudio)

| Cliente | Instagram | Google Business | Facebook | Estado |
|---|---|---|---|---|
| Carnes Lolol | @carneslolol | Av. Padre Hurtado 11868 | - | Pendiente conectar |
| Saul el Constructor | Por confirmar | Constructor Saul SpA | - | Pendiente conectar |
| Glowvision Punitaqui | Por confirmar | Por confirmar | - | Pendiente |

---

## Observacion OBS-20260524-001

Zernio MCP + Claude Code es el backbone tecnico del servicio "Content Engine IA"
y "Publicador Tanque V8" del catalogo de AetriaStudio. Documentado el 2026-05-24.
Referencia: guia @diegoampuero2 "Publica en Piloto Automatico con Zernio".
