"""
03_indexar.py
Crea índice vectorial local con ChromaDB usando embeddings multilingües.

Modelo de embeddings: intfloat/multilingual-e5-base
- Excelente para español
- 768 dims, balance calidad/velocidad
- 100% local, gratis, sin API key

Alternativa más fuerte: intfloat/multilingual-e5-large (1024 dims, más lento)
"""
import json
from pathlib import Path
import chromadb
from chromadb.utils import embedding_functions

CHUNKS_FILE = Path("data/chunks/chunks.jsonl")
DB_DIR = "data/chroma_db"
COLLECTION = "audios_programa"
EMB_MODEL = "intfloat/multilingual-e5-base"

def main():
    chunks = [json.loads(l) for l in CHUNKS_FILE.read_text(encoding="utf-8").splitlines()]
    print(f"Cargados {len(chunks)} chunks")

    client = chromadb.PersistentClient(path=DB_DIR)
    emb_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name=EMB_MODEL
    )
    # E5 espera prefijo "passage:" para los documentos indexados
    # y "query:" para las búsquedas. Lo manejamos en el wrapper de consulta.
    
    try:
        client.delete_collection(COLLECTION)
    except Exception:
        pass
    coll = client.create_collection(
        name=COLLECTION,
        embedding_function=emb_fn,
        metadata={"hnsw:space": "cosine"},
    )

    BATCH = 64
    for i in range(0, len(chunks), BATCH):
        batch = chunks[i:i+BATCH]
        coll.add(
            ids=[c["id"] for c in batch],
            documents=[f"passage: {c['text']}" for c in batch],
            metadatas=[{
                "dia": c["dia"],
                "titulo": c["titulo"],
                "indice_chunk": c["indice_chunk"],
                "start_s": c["start_s"],
                "end_s": c["end_s"],
                "timestamp_inicio": c["timestamp_inicio"],
                "timestamp_fin": c["timestamp_fin"],
            } for c in batch],
        )
        print(f"  indexados {min(i+BATCH, len(chunks))}/{len(chunks)}")

    print(f"\nÍndice listo en {DB_DIR}")
    
    # Smoke test
    res = coll.query(query_texts=["query: cómo identificar patrones que me estancan"], n_results=3)
    print("\n--- Prueba: 'patrones que me estancan' ---")
    for i, doc in enumerate(res["documents"][0]):
        md = res["metadatas"][0][i]
        print(f"\n[Día {md['dia']} · {md['timestamp_inicio']}] {md['titulo']}")
        print(doc[:200].replace("passage: ", ""), "...")

if __name__ == "__main__":
    main()
