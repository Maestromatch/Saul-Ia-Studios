"""
05_chat.py
Conversa con el agente. Combina:
  - RAG sobre los 14 audios (ChromaDB)
  - Memoria del usuario (SQLite)
  - LLM (Anthropic Claude por defecto; alternar a OpenAI fácil)

Uso:
    export ANTHROPIC_API_KEY=sk-ant-...
    python scripts/05_chat.py

Cada turno:
1. Recupera 5 chunks relevantes de los audios para tu mensaje.
2. Carga tu perfil + últimos 10 episodios + patrones activos.
3. Llama al LLM con todo eso como contexto.
4. Guarda el turno como episodio nuevo.
"""
import os
import json
import sqlite3
from pathlib import Path
from datetime import datetime
import chromadb
from chromadb.utils import embedding_functions
from anthropic import Anthropic

DB_PATH = Path("data/memoria.db")
CHROMA_DIR = "data/chroma_db"
COLLECTION = "audios_programa"
EMB_MODEL = "intfloat/multilingual-e5-base"
MODEL = "claude-opus-4-7"  # o "claude-sonnet-4-6"

SYSTEM_PROMPT = Path("prompts/system.md").read_text(encoding="utf-8")

def get_chroma():
    client = chromadb.PersistentClient(path=CHROMA_DIR)
    emb_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=EMB_MODEL)
    return client.get_collection(COLLECTION, embedding_function=emb_fn)

def recuperar_audios(coll, query, k=5):
    res = coll.query(query_texts=[f"query: {query}"], n_results=k)
    out = []
    for i, doc in enumerate(res["documents"][0]):
        md = res["metadatas"][0][i]
        out.append({
            "dia": md["dia"],
            "titulo": md["titulo"],
            "ts": md["timestamp_inicio"],
            "texto": doc.replace("passage: ", ""),
        })
    return out

def cargar_contexto_usuario(con):
    perfil = con.execute(
        "SELECT * FROM perfil ORDER BY version DESC LIMIT 1"
    ).fetchone()
    cols = [d[0] for d in con.description]
    perfil_d = dict(zip(cols, perfil)) if perfil else {}

    episodios = con.execute("""
        SELECT timestamp, tipo, contenido, estado_emocional, nivel_vibracion
        FROM episodios ORDER BY id DESC LIMIT 10
    """).fetchall()

    patrones = con.execute("""
        SELECT descripcion, severidad, intervencion_sugerida
        FROM patrones WHERE estado = 'activo' ORDER BY severidad DESC LIMIT 5
    """).fetchall()

    compromisos = con.execute("""
        SELECT descripcion, fecha_objetivo, cumplido
        FROM compromisos WHERE cumplido IS NULL ORDER BY id DESC LIMIT 5
    """).fetchall()
    
    return perfil_d, episodios, patrones, compromisos

def construir_contexto(audios, perfil, episodios, patrones, compromisos):
    ctx = ["## Material del programa (citas relevantes)\n"]
    for a in audios:
        ctx.append(f"[Día {a['dia']} · {a['ts']}] {a['titulo']}\n«{a['texto']}»\n")
    
    ctx.append("\n## Perfil actual del usuario")
    ctx.append(json.dumps({
        "valores": json.loads(perfil.get("valores_centrales") or "[]"),
        "metas": json.loads(perfil.get("metas_actuales") or "[]"),
        "creencias_limitantes": json.loads(perfil.get("creencias_limitantes") or "[]"),
        "areas_estancamiento": json.loads(perfil.get("areas_estancamiento") or "[]"),
    }, ensure_ascii=False, indent=2))

    if episodios:
        ctx.append("\n## Últimos episodios")
        for e in episodios:
            ctx.append(f"- [{e[0]}] ({e[1]}) {e[2][:200]}")
    
    if patrones:
        ctx.append("\n## Patrones activos detectados")
        for p in patrones:
            ctx.append(f"- (sev {p[1]}) {p[0]}  →  intervención: {p[2]}")
    
    if compromisos:
        ctx.append("\n## Compromisos abiertos")
        for c in compromisos:
            ctx.append(f"- {c[0]} (objetivo: {c[1]})")
    
    return "\n".join(ctx)

def guardar_episodio(con, user_msg, resp):
    con.execute("""
        INSERT INTO episodios (tipo, contenido, respuesta_agente)
        VALUES ('chat', ?, ?)
    """, (user_msg, resp))
    con.commit()

def main():
    client = Anthropic()
    coll = get_chroma()
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row

    print("Agente listo. Escribe 'salir' para terminar.\n")
    historial = []

    while True:
        user = input("Tú: ").strip()
        if not user or user.lower() in {"salir", "exit", "quit"}:
            break

        audios = recuperar_audios(coll, user, k=5)
        perfil, episodios, patrones, compromisos = cargar_contexto_usuario(con)
        contexto = construir_contexto(audios, perfil, episodios, patrones, compromisos)

        historial.append({"role": "user", "content": f"{user}\n\n---\n{contexto}"})

        resp = client.messages.create(
            model=MODEL,
            max_tokens=1500,
            system=SYSTEM_PROMPT,
            messages=historial,
        )
        texto = resp.content[0].text
        historial.append({"role": "assistant", "content": texto})

        print(f"\nAgente: {texto}\n")
        guardar_episodio(con, user, texto)

    con.close()

if __name__ == "__main__":
    main()
