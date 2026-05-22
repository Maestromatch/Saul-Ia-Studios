# Privacidad y manejo de datos sensibles

Este agente va a saber de ti más que casi cualquiera. Tómate esto en serio.

## Reglas mínimas

1. **El archivo `data/memoria.db` es oro.** Hace backup diario a un disco
   externo o nube cifrada (Cryptomator, rclone con encryption).
2. **No subas el repo a GitHub público con `data/` adentro.** Añade `data/` a
   `.gitignore` desde el día uno.
3. **Si usas API de Claude/OpenAI**, esos turnos pasan por sus servidores.
   Anthropic y OpenAI tienen políticas de no-entrenamiento con datos de API,
   pero los logs existen 30 días. Si te incomoda, usa modelos locales con
   Ollama.
4. **Cifra el disco de tu máquina** (FileVault en Mac, BitLocker en Windows,
   LUKS en Linux). Sin esto, todo lo demás da igual.

## Si decides ir 100% local

Stack alternativo sin API externa:
- Ollama + Llama 3.1 70B (o 8B si tu máquina es modesta)
- Embeddings ya son locales (e5)
- Chroma ya es local
- Whisper ya es local

Único trade-off: la calidad del coach es algo menor que Claude Opus 4.7 o
GPT-5. En español hace la diferencia.

## Modo "purga"

Añade un script `scripts/purgar.py` que permita borrar episodios anteriores
a X días. Recomendación: conserva resúmenes semanales/mensuales (sintéticos)
y purga el detalle crudo después de 90 días. El agente sigue funcionando con
los resúmenes y tu perfil sigue intacto.

## Señales de crisis

El system prompt incluye una regla: si el usuario describe ideación suicida,
violencia, o crisis de salud mental, el agente sale del modo coach y entrega
recursos profesionales. Mantén esa regla intacta.
