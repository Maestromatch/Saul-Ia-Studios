"""
01_transcribir.py
Transcribe los 14 audios .mp3 a texto + JSON con segmentos timestampeados.

Usa faster-whisper (más rápido y eficiente que openai-whisper estándar).
Modelo recomendado: "medium" o "large-v3" para máxima calidad en español.
Si tu máquina es modesta, "small" da buen resultado.

GPU: si tienes CUDA, cambia device="cpu" a device="cuda".
Mac Apple Silicon: usa device="cpu" con compute_type="int8" (rápido).
"""
import json
import re
from pathlib import Path
from datetime import datetime
from faster_whisper import WhisperModel

# ---------- CONFIG ----------
AUDIO_DIR = Path("audios")
OUT_DIR = Path("data/transcripciones")
MODEL_SIZE = "medium"           # tiny | base | small | medium | large-v3
DEVICE = "cpu"                  # "cuda" si tienes GPU NVIDIA
COMPUTE_TYPE = "int8"           # "float16" en GPU, "int8" en CPU/Mac
LANGUAGE = "es"
# ----------------------------

OUT_DIR.mkdir(parents=True, exist_ok=True)

def parse_filename(fname):
    """Extrae día y título del nombre del archivo."""
    m = re.match(r"Di_a_(\d+)[\s_-]+_*(.+)\.mp3", fname)
    if not m:
        return None, fname
    dia = int(m.group(1))
    titulo = m.group(2).replace("_", " ").strip().strip("¿?¡!").strip()
    titulo = re.sub(r"\s+", " ", titulo)
    return dia, titulo

def main():
    archivos = sorted(
        AUDIO_DIR.glob("*.mp3"),
        key=lambda p: parse_filename(p.name)[0] or 0
    )
    if not archivos:
        print(f"No hay .mp3 en {AUDIO_DIR.resolve()}")
        return

    print(f"Cargando modelo: {MODEL_SIZE} ({DEVICE}, {COMPUTE_TYPE})...")
    model = WhisperModel(MODEL_SIZE, device=DEVICE, compute_type=COMPUTE_TYPE)
    print("Modelo cargado.\n")

    maestro = []
    for idx, audio in enumerate(archivos, 1):
        dia, titulo = parse_filename(audio.name)
        print(f"[{idx}/{len(archivos)}] Día {dia}: {titulo}")
        t0 = datetime.now()

        segments, info = model.transcribe(
            str(audio),
            language=LANGUAGE,
            beam_size=5,
            vad_filter=True,                # quita silencios
            vad_parameters=dict(min_silence_duration_ms=500),
            condition_on_previous_text=False,
        )

        segs = []
        texto_full = []
        for s in segments:
            segs.append({
                "start": round(s.start, 2),
                "end": round(s.end, 2),
                "text": s.text.strip(),
            })
            texto_full.append(s.text.strip())

        texto_full = " ".join(texto_full)
        elapsed = (datetime.now() - t0).total_seconds()

        # TXT
        (OUT_DIR / f"dia_{dia:02d}.txt").write_text(
            f"# Día {dia} — {titulo}\n\n{texto_full}\n", encoding="utf-8"
        )
        # JSON con timestamps
        (OUT_DIR / f"dia_{dia:02d}.json").write_text(
            json.dumps({
                "dia": dia,
                "titulo": titulo,
                "archivo": audio.name,
                "idioma": info.language,
                "duracion": round(info.duration, 1),
                "segmentos": segs,
                "texto_completo": texto_full,
            }, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )

        maestro.append({
            "dia": dia, "titulo": titulo, "archivo": audio.name,
            "n_segmentos": len(segs),
            "n_palabras": len(texto_full.split()),
            "duracion_s": round(info.duration, 1),
            "tiempo_proceso_s": round(elapsed, 1),
        })
        print(f"   → {len(segs)} segmentos · {len(texto_full.split())} palabras · {elapsed:.0f}s\n")

    (OUT_DIR / "maestro.json").write_text(
        json.dumps(maestro, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Listo. Transcripciones en {OUT_DIR.resolve()}")

if __name__ == "__main__":
    main()
