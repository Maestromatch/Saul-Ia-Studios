# Setup MCP Zernio en Claude Code — AetriaStudio

> Instrucciones para conectar Zernio al Claude Code CLI.
> Ejecutar una sola vez. La conexion persiste entre sesiones.

---

## Tu API key Zernio

Obtenida en: zernio.com/dashboard → API Keys → Generate New Key

Formato: empieza con `sk_...`

IMPORTANTE: Guarda esta clave en un lugar seguro. Si la perdiste,
genera una nueva en zernio.com/dashboard/api-keys.

---

## Metodo 1 — Via CLI (recomendado)

Ejecutar en PowerShell (sintaxis exacta verificada):

```bash
claude mcp add --transport sse --scope user zernio "https://mcp.zernio.com/sse" --header "Authorization: Bearer sk_TU_CLAVE_AQUI"
```

El flag `--scope user` lo hace disponible en todos los proyectos de la maquina.

Verificar que quedo guardado:
```bash
claude mcp list
```

Debe aparecer: `zernio — https://mcp.zernio.com/sse`

---

## Metodo 2 — Via archivo .mcp.json en el proyecto

Crear `C:\Users\Usuario 01\IAStudio_Lanzamiento\.mcp.json`:

```json
{
  "mcpServers": {
    "zernio": {
      "type": "sse",
      "url": "https://mcp.zernio.com/sse",
      "headers": {
        "Authorization": "Bearer sk_TU_CLAVE_AQUI"
      }
    }
  }
}
```

IMPORTANTE: Agregar `.mcp.json` al `.gitignore` antes de hacer push,
ya que contiene la API key.

---

## Verificacion de instalacion exitosa

En Claude Code escribir:
```
Usa Zernio para listar mis cuentas conectadas
```

Respuesta esperada: lista de redes sociales conectadas a la cuenta Zernio.

Si no responde o da error:
1. Verificar que la API key es correcta.
2. Reiniciar Claude Code.
3. Verificar plan Zernio (necesita Plan Pro para API completa).

---

## Conectar cuentas de clientes en Zernio dashboard

### Para Carnes Lolol

1. Ir a zernio.com/dashboard/connections
2. Click "Add connection" → Instagram
3. Iniciar sesion con credenciales de @carneslolol
4. Aprobar permisos de publicacion
5. Verificar check verde

PREREQUISITO: @carneslolol debe ser cuenta de empresa (no personal).
Si es personal: ir a Instagram → Configuracion → Cuenta → Cambiar a cuenta profesional → Empresa.

Para Google Business:
1. Click "Add connection" → GMB (Google My Business)
2. Iniciar sesion con la cuenta Google del dueño de Carnes Lolol
3. Seleccionar el perfil "Carnes Lolol"
4. Aprobar permisos

PREREQUISITO: El dueño debe haber reclamado el perfil Google Business primero.
Instrucciones: google.com/business → "Gestionar ahora" → buscar "Carnes Lolol"

---

## Prueba rapida post-setup

```
/post-contenido --draft "Hola barrio! Carnes Lolol tiene disponible [PRODUCTO] esta semana.
Pasate por Av. Padre Hurtado 11868 o escribe al 9 7999 9709"
--client carneslolol --platforms instagram
```

Si genera el borrador correctamente → todo listo para empezar a publicar.

---

## Seguridad

- No subir la API key a GitHub.
- Agregar `.mcp.json` al `.gitignore` si se usa Metodo 2.
- Rotar la API key si se sospecha que fue expuesta.
- Usar una API key por entorno (dev vs produccion) cuando escale.
