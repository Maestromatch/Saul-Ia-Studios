# Arquitectura del Agente

## Diagrama de capas

```
┌──────────────────────────────────────────────────────────┐
│  INTERFAZ (CLI / Telegram / Web)                         │
└────────────────────────┬─────────────────────────────────┘
                         │
┌────────────────────────▼─────────────────────────────────┐
│  ORQUESTADOR (scripts/05_chat.py)                        │
│  - recupera contexto                                     │
│  - llama LLM                                             │
│  - guarda episodio                                       │
└────┬────────────────┬────────────────────┬───────────────┘
     │                │                    │
┌────▼────┐      ┌────▼─────┐         ┌────▼─────┐
│  RAG    │      │ MEMORIA  │         │   LLM    │
│ Chroma  │      │ SQLite   │         │ Claude/  │
│ (audios)│      │ (perfil, │         │ GPT-4    │
│         │      │ episod., │         │          │
│         │      │ patrones)│         │          │
└─────────┘      └──────────┘         └──────────┘
                       ▲
                       │
              ┌────────┴─────────┐
              │ DETECTOR (job)   │
              │ scripts/06_...py │
              │ corre semanal    │
              └──────────────────┘
```

## ¿Por qué SQLite y no Postgres?

Para uso personal local, SQLite es perfecto: un solo archivo, cero
configuración, soporta tu volumen 1000x. Si después abres el agente a más
gente, migra a Postgres + pgvector (consolida vector + SQL en un solo motor).

## ¿Por qué ChromaDB?

100% local, sin servidor, archivo en disco. Cuando crezcas y quieras filtros
complejos sobre metadata o búsqueda híbrida (BM25 + vector), evalúa Qdrant o
Weaviate. Para empezar, Chroma es el camino.

## ¿Por qué multilingual-e5-base como embeddings?

- Excelente desempeño en español
- Tamaño manejable (1.1 GB)
- Gratis, local, sin API
- Mejor que sentence-transformers/all-MiniLM-L6-v2 en español por mucho

Alternativa más fuerte: `intfloat/multilingual-e5-large` (4x más pesado, ~10%
mejor en retrieval).

## Flujo de un mensaje

1. Usuario escribe.
2. Embebemos su mensaje con e5 + prefijo `query:`.
3. ChromaDB devuelve top-5 chunks de los audios.
4. SQLite devuelve: perfil actual, últimos 10 episodios, patrones activos,
   compromisos abiertos.
5. Todo eso va al system prompt + mensaje al LLM.
6. LLM responde con tono coach.
7. Guardamos el episodio (usuario + respuesta) en SQLite.

## Job semanal

Cron los lunes 8am. Lee episodios de últimos 7 días, llama a Claude con un
prompt analítico, obtiene patrones JSON, los inserta en la tabla `patrones`.
Esos patrones aparecen automáticamente en el contexto de las siguientes
conversaciones → el agente puede confrontarte con ellos.

## Coste estimado

- Transcripción: una sola vez, gratis (Whisper local).
- Embeddings: gratis (local).
- LLM por turno: con Claude Sonnet 4.6, ~$0.01-0.03 por mensaje incluyendo el
  contexto. Conversación de 30 turnos diarios = ~$0.50/día = ~$15/mes.
- Job semanal de patrones: ~$0.05/semana.

Si prefieres todo local, sustituye Claude por un modelo local vía Ollama
(Llama 3.1 70B o Qwen 2.5 32B funcionan bien para esto, en español).
