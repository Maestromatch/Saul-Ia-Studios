# Agente de Desarrollo Personal — Base de Conocimiento + Memoria

Este paquete contiene todo lo necesario para construir tu agente personal
basado en los 14 audios del programa (Día 2 al Día 15).

## Qué hace este paquete

1. **Transcribe** los 14 audios MP3 a texto con timestamps (Whisper).
2. **Limpia y chunkea** las transcripciones en piezas listas para RAG.
3. **Crea un índice de embeddings** local con ChromaDB.
4. **Inicializa la memoria del usuario** (perfil + episódica) en SQLite.
5. **Te entrega prompts del sistema** listos para conectar a Claude o GPT.

## Cómo usarlo (orden de ejecución)

```bash
# 1) Instala dependencias
pip install -r requirements.txt

# 2) Pon tus 14 audios en ./audios/
#    (los nombres pueden mantenerse: Di_a_2_..., Di_a_3_..., etc.)

# 3) Transcribe (toma 1-2h en CPU, 10-20min en GPU/Mac)
python scripts/01_transcribir.py

# 4) Limpia y chunkea
python scripts/02_chunkear.py

# 5) Construye índice vectorial
python scripts/03_indexar.py

# 6) Inicializa memoria del usuario
python scripts/04_init_memoria.py

# 7) Probar el agente
python scripts/05_chat.py
```

## Estructura final

```
agente_pkg/
├── audios/                  <- tus 14 mp3 aquí
├── data/
│   ├── transcripciones/     <- txt + json con timestamps
│   ├── chunks/              <- chunks listos para RAG
│   ├── chroma_db/           <- índice vectorial
│   └── memoria.db           <- SQLite con tu perfil y episodios
├── scripts/                 <- pipeline completo
├── prompts/                 <- system prompts del agente
└── requirements.txt
```

## Decisiones importantes documentadas en `docs/`

- `arquitectura.md` — visión general y diagrama de capas
- `memoria.md` — diseño del esquema de memoria
- `deteccion_patrones.md` — cómo detecta tus bucles
- `seguridad.md` — privacidad y manejo de datos sensibles
