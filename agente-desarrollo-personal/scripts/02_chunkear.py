"""
02_chunkear.py
Convierte las transcripciones en chunks listos para RAG.

Estrategia:
- Chunks ~600 tokens (~450 palabras en español), overlap 80 palabras.
- Cada chunk conserva timestamp de inicio y fin del audio (útil para citar).
- Metadata: día, título, posición, rango temporal.

Por qué este tamaño: contenido reflexivo/coaching tiene ideas que se desarrollan
en 2-3 minutos. 600 tokens captura una idea completa sin trocearla.
"""
import json
import re
from pathlib import Path

IN_DIR = Path("data/transcripciones")
OUT_DIR = Path("data/chunks")
OUT_DIR.mkdir(parents=True, exist_ok=True)

WORDS_PER_CHUNK = 450
OVERLAP_WORDS = 80

def chunk_segments(segmentos, target=WORDS_PER_CHUNK, overlap=OVERLAP_WORDS):
    """Agrupa segmentos en chunks por número de palabras, respetando límites de segmento."""
    chunks = []
    buf = []
    buf_words = 0
    buf_start = None

    for seg in segmentos:
        words = seg["text"].split()
        if buf_start is None:
            buf_start = seg["start"]
        buf.append(seg)
        buf_words += len(words)

        if buf_words >= target:
            text = " ".join(s["text"] for s in buf)
            chunks.append({
                "start": buf_start,
                "end": buf[-1]["end"],
                "text": text,
                "n_words": buf_words,
            })
            # overlap: conservar últimos N palabras como semilla del siguiente chunk
            tail_words = []
            tail_segs = []
            count = 0
            for s in reversed(buf):
                w = s["text"].split()
                count += len(w)
                tail_segs.insert(0, s)
                if count >= overlap:
                    break
            buf = tail_segs
            buf_words = sum(len(s["text"].split()) for s in buf)
            buf_start = buf[0]["start"]

    if buf and buf_words > 50:  # último resto si vale la pena
        chunks.append({
            "start": buf_start,
            "end": buf[-1]["end"],
            "text": " ".join(s["text"] for s in buf),
            "n_words": buf_words,
        })
    return chunks

def fmt_ts(seconds):
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"

def main():
    json_files = sorted(IN_DIR.glob("dia_*.json"))
    all_chunks = []

    for jf in json_files:
        data = json.loads(jf.read_text(encoding="utf-8"))
        dia = data["dia"]
        titulo = data["titulo"]
        chunks = chunk_segments(data["segmentos"])

        for i, c in enumerate(chunks):
            chunk_id = f"dia{dia:02d}_c{i:03d}"
            all_chunks.append({
                "id": chunk_id,
                "dia": dia,
                "titulo": titulo,
                "indice_chunk": i,
                "start_s": c["start"],
                "end_s": c["end"],
                "timestamp_inicio": fmt_ts(c["start"]),
                "timestamp_fin": fmt_ts(c["end"]),
                "n_words": c["n_words"],
                "text": c["text"],
            })
        print(f"Día {dia}: {len(chunks)} chunks")

    out = OUT_DIR / "chunks.jsonl"
    with out.open("w", encoding="utf-8") as f:
        for c in all_chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    print(f"\nTotal: {len(all_chunks)} chunks guardados en {out}")

if __name__ == "__main__":
    main()
