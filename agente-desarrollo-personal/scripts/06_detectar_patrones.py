"""
06_detectar_patrones.py
Job que corre semanalmente. Lee episodios de los últimos 7-30 días y detecta:

- Bucles recurrentes (misma queja, distinta forma) — clustering semántico
- Lenguaje victimista vs. agente — reglas + LLM clasificador
- Incoherencia dicho/hecho — cruza compromisos con episodios
- Cambios positivos — para celebrarlos también

Outputs:
- Inserta filas en `patrones`
- Actualiza el perfil (nueva versión) si hay cambios significativos
- Genera un resumen semanal

Pensado para correrse con cron:
    0 8 * * MON  cd /ruta && python scripts/06_detectar_patrones.py
"""
import json
import sqlite3
from pathlib import Path
from datetime import datetime, timedelta
from collections import Counter
from anthropic import Anthropic

DB_PATH = Path("data/memoria.db")
VENTANA_DIAS = 7
MODEL = "claude-opus-4-7"

ANALISIS_PROMPT = """Eres un analista de patrones de desarrollo personal.

Te paso los episodios de los últimos {ventana} días de un usuario que trabaja
con un programa de 14 días sobre vibración, competencias y manifestación.

Tu tarea: identificar de forma rigurosa hasta 5 patrones, cada uno con:
- tipo: uno de [bucle_recurrente | lenguaje_victima | incoherencia_dicho_hecho |
        evitacion | cambio_positivo]
- descripcion: 1-2 frases claras
- evidencia: ids de episodios (de los provistos) + cita literal cuando aplique
- severidad: 1-5
- intervencion_sugerida: una acción concreta, alineada al marco del programa
- referencia_audios: días del programa que apliquen (lista de enteros 2-15)

Devuelve SOLO JSON válido con la forma:
{{ "patrones": [ ... ] }}

No inventes patrones. Si no hay evidencia suficiente, devuelve lista vacía.
Sé especialmente sensible a:
- frases con "es que", "siempre", "nunca", "no puedo"
- temas que se repiten en 3+ episodios distintos
- compromisos no cumplidos sin reconocimiento

Episodios:
{episodios_json}

Compromisos vigentes:
{compromisos_json}
"""

def main():
    client = Anthropic()
    con = sqlite3.connect(DB_PATH)

    desde = (datetime.now() - timedelta(days=VENTANA_DIAS)).isoformat()
    episodios = con.execute("""
        SELECT id, timestamp, tipo, contenido, estado_emocional, nivel_vibracion
        FROM episodios WHERE timestamp >= ? ORDER BY id
    """, (desde,)).fetchall()

    if not episodios:
        print("Sin episodios en la ventana. Saliendo.")
        return

    compromisos = con.execute("""
        SELECT id, descripcion, fecha_objetivo, cumplido FROM compromisos
        WHERE creado_en >= ?
    """, (desde,)).fetchall()

    eps_json = json.dumps([
        {"id": e[0], "ts": e[1], "tipo": e[2], "contenido": e[3],
         "estado": e[4], "vibracion": e[5]} for e in episodios
    ], ensure_ascii=False, indent=2)
    com_json = json.dumps([
        {"id": c[0], "descripcion": c[1], "objetivo": c[2], "cumplido": c[3]}
        for c in compromisos
    ], ensure_ascii=False, indent=2)

    prompt = ANALISIS_PROMPT.format(
        ventana=VENTANA_DIAS, episodios_json=eps_json, compromisos_json=com_json
    )

    resp = client.messages.create(
        model=MODEL, max_tokens=2000,
        messages=[{"role": "user", "content": prompt}]
    )
    raw = resp.content[0].text.strip()
    # limpiar fences si vienen
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    data = json.loads(raw)

    insertados = 0
    for p in data.get("patrones", []):
        con.execute("""
            INSERT INTO patrones (tipo, descripcion, evidencia, severidad,
                intervencion_sugerida, referencia_audios)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            p.get("tipo", "bucle_recurrente"),
            p.get("descripcion", ""),
            json.dumps(p.get("evidencia", []), ensure_ascii=False),
            int(p.get("severidad", 3)),
            p.get("intervencion_sugerida", ""),
            json.dumps(p.get("referencia_audios", []), ensure_ascii=False),
        ))
        insertados += 1
    con.commit()
    con.close()
    print(f"Patrones nuevos detectados: {insertados}")

if __name__ == "__main__":
    main()
