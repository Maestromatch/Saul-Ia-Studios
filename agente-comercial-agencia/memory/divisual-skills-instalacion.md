# Guía de Instalación — Divisual Skills Pack

> Cómo instalar las 17 skills de La Tribu en Claude Code para que estén disponibles en todos los proyectos.
> Fuente: `_inbox/la-tribu/` | Fecha: 2026-05-25

---

## Opción 1 — Instalación global (recomendada)

Las skills instaladas en `~/.claude/skills/` están disponibles en CUALQUIER proyecto.

```powershell
# Carpeta destino global de skills
$dest = "$env:USERPROFILE\.claude\skills"

# Crear si no existe
New-Item -ItemType Directory -Force -Path $dest

# Copiar divisual-skills-pack (skills 01-09)
$skillsBase = "C:\Users\Usuario 01\IAStudio_Lanzamiento\_inbox\la-tribu\divisual-skills-pack\skills"

Copy-Item "$skillsBase\03-prospeccion\.claude\skills\prospeccion" -Destination "$dest\prospeccion" -Recurse -Force
Copy-Item "$skillsBase\05-auditoria-negocio\.claude\skills\auditoria-negocio" -Destination "$dest\auditoria-negocio" -Recurse -Force
Copy-Item "$skillsBase\04-n8n-workflow-patterns\.claude\skills\n8n-workflow-patterns" -Destination "$dest\n8n-workflow-patterns" -Recurse -Force
Copy-Item "$skillsBase\02-seo-optimizer\.claude\skills\seo-optimizer" -Destination "$dest\seo-optimizer" -Recurse -Force
Copy-Item "$skillsBase\01-crear-skill\.claude\skills\crear-skill" -Destination "$dest\crear-skill" -Recurse -Force
Copy-Item "$skillsBase\06-create-briefing\.claude\skills\create-briefing" -Destination "$dest\create-briefing" -Recurse -Force
Copy-Item "$skillsBase\07-analyze-video\.claude\skills\analyze-video" -Destination "$dest\analyze-video" -Recurse -Force
Copy-Item "$skillsBase\08-claude-youtube\.claude\skills\youtube" -Destination "$dest\youtube" -Recurse -Force
```

**Para las skills del COWORK pack (7 SKILLS):**
```powershell
$coworkBase = "C:\Users\Usuario 01\IAStudio_Lanzamiento\_inbox\la-tribu\7 SKILLS CLAUDE COWORK"

Copy-Item "$coworkBase\skill-1-espia-tendencias" -Destination "$dest\espia-tendencias" -Recurse -Force
Copy-Item "$coworkBase\skill-2-scraping-competencia" -Destination "$dest\scraping-competencia" -Recurse -Force
Copy-Item "$coworkBase\skill-3-diseno-canva" -Destination "$dest\diseno-canva" -Recurse -Force
Copy-Item "$coworkBase\skill-4-dashboard-negocio" -Destination "$dest\dashboard-negocio" -Recurse -Force
Copy-Item "$coworkBase\skill-5-emails-venta" -Destination "$dest\emails-venta" -Recurse -Force
Copy-Item "$coworkBase\skill-6-auditor-seo" -Destination "$dest\auditor-seo" -Recurse -Force
Copy-Item "$coworkBase\skill-7-calendario-contenido" -Destination "$dest\calendario-contenido" -Recurse -Force
```

**Para las skills DEEPSEEK (landing + propuesta):**
```powershell
$deepseekBase = "C:\Users\Usuario 01\IAStudio_Lanzamiento\_inbox\la-tribu\DEEPSEEK V4 SKILLS CLAUDE CODE"

Copy-Item "$deepseekBase\landing-cliente-local.md" -Destination "$dest\landing-cliente-local\SKILL.md" -Force
Copy-Item "$deepseekBase\propuesta-cliente.md" -Destination "$dest\propuesta-cliente\SKILL.md" -Force
```

---

## Opción 2 — Instalación por proyecto

Instalar solo en el proyecto IAStudio (ya en el directorio `.claude/skills/` del proyecto):

```powershell
$dest = "C:\Users\Usuario 01\IAStudio_Lanzamiento\.claude\skills"
New-Item -ItemType Directory -Force -Path $dest
# Mismo proceso que arriba pero con esta ruta de destino
```

---

## Verificar que están activas

Después de instalar, **reiniciar Claude Code** y verificar:

```
/help
```

Las skills deben aparecer en el listado. Para invocar manualmente:

```
/prospeccion
/auditoria-negocio
/propuesta-cliente
/landing-cliente-local
```

---

## Skills más importantes para empezar (top 5)

### 1. `/propuesta-cliente` — Uso inmediato
Inputs mínimos: nombre cliente, proyecto, precio, timeline.
Genera PDF + email + follow-up en una sola pasada.

### 2. `/prospeccion` — Ampliar lista ópticas
```
Usa la skill prospeccion. Busca 30 ópticas en la zona sur RM
(El Bosque, San Bernardo, La Cisterna, San Miguel, Maipú)
para venderles un bot de WhatsApp para gestión de consultas.
```

### 3. `/auditoria-negocio` — Preparar visita Carnes Lolol
```
Usa la skill auditoria-negocio. URL: instagram.com/carneslolol
Servicio: bot WhatsApp + publicación RRSS con Zernio.
Competidores: carnicerías del Bosque.
```

### 4. `/landing-cliente-local` — Acelerar Pack IA Express
```
Usa la skill landing-cliente-local.
Cliente: [nombre óptica]. Tipo: óptica. Ciudad: [ciudad].
WhatsApp: [número]. Dirección: [dirección]. Horarios: [horarios].
```

### 5. `/n8n-workflow-patterns` — Workflows para clientes
```
Necesito un workflow n8n que reciba mensajes de WhatsApp
vía webhook, los procese con IA y responda automáticamente.
```

---

## Notas de seguridad al instalar

- Los JSONs de n8n contienen IDs de Google Sheets de otros usuarios y webhooks privados. Al importarlos, cambiar TODAS las credenciales y URLs antes de activar.
- Las skills no guardan datos de clientes — trabajan con inputs de cada sesión.
- El script `10-video-use` requiere Python, ffmpeg y ElevenLabs API key (tiene costo).

---

## Estado de instalación

| Skill | Estado |
|-------|--------|
| `prospeccion` | Disponible en sesión actual (detectada automáticamente) |
| `auditoria-negocio` | Disponible en sesión actual |
| `n8n-workflow-patterns` | Disponible en sesión actual |
| `create-briefing` | Disponible en sesión actual |
| Resto | Pendiente instalación global con los comandos de arriba |
