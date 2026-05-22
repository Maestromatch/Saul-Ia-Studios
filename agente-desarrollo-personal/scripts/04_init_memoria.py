"""
04_init_memoria.py
Inicializa la base de datos SQLite con el esquema de memoria del usuario.

Tres capas:
1) PERFIL — datos semánticos del usuario (creencias, patrones, valores, metas).
2) EPISODIOS — cada conversación / journal / check-in con timestamp.
3) PATRONES — señales detectadas (bucles, contradicciones, evolución).

Diseño pensado para auto-aprendizaje: el agente lee y escribe aquí en cada turno.
"""
import sqlite3
from pathlib import Path

DB_PATH = Path("data/memoria.db")
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

SCHEMA = """
-- =========================================================
-- PERFIL DEL USUARIO (capa semántica, evoluciona en el tiempo)
-- =========================================================
CREATE TABLE IF NOT EXISTS perfil (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    version INTEGER NOT NULL,
    creado_en TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    -- secciones del perfil en JSON, una fila = una versión completa
    valores_centrales TEXT,        -- JSON: lo que más importa
    metas_actuales TEXT,           -- JSON: 1-5 metas concretas con fecha
    creencias_limitantes TEXT,     -- JSON: lista con evidencia
    creencias_potenciadoras TEXT,  -- JSON: lista con evidencia
    fortalezas TEXT,               -- JSON
    areas_estancamiento TEXT,      -- JSON: dominios donde se repite el bucle
    relaciones_clave TEXT,         -- JSON: personas que aparecen frecuentemente
    disparadores_emocionales TEXT, -- JSON
    nota_libre TEXT
);

-- =========================================================
-- EPISODIOS (capa episódica, append-only)
-- =========================================================
CREATE TABLE IF NOT EXISTS episodios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    tipo TEXT NOT NULL,           -- 'chat' | 'checkin_diario' | 'journal' | 'review_semanal'
    contenido TEXT NOT NULL,      -- texto crudo de lo que el usuario dijo
    respuesta_agente TEXT,        -- lo que el agente respondió
    estado_emocional TEXT,        -- ej: 'frustrado', 'esperanzado'
    nivel_vibracion INTEGER,      -- 1-10 (escala alineada al marco de los audios)
    temas TEXT,                   -- JSON array de tags
    util INTEGER                  -- feedback: -1, 0, 1 (acertado/neutro/erróneo)
);

CREATE INDEX IF NOT EXISTS idx_episodios_ts ON episodios(timestamp);
CREATE INDEX IF NOT EXISTS idx_episodios_tipo ON episodios(tipo);

-- =========================================================
-- PATRONES DETECTADOS (output del análisis periódico)
-- =========================================================
CREATE TABLE IF NOT EXISTS patrones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    detectado_en TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    tipo TEXT NOT NULL,           -- 'bucle_recurrente' | 'incoherencia_dicho_hecho'
                                  -- 'lenguaje_victima' | 'evitacion' | 'cambio_positivo'
    descripcion TEXT NOT NULL,
    evidencia TEXT,               -- JSON: ids de episodios + citas textuales
    severidad INTEGER,            -- 1-5
    estado TEXT NOT NULL DEFAULT 'activo',  -- 'activo' | 'en_trabajo' | 'resuelto'
    intervencion_sugerida TEXT,   -- qué propone el agente para romper el bucle
    referencia_audios TEXT        -- JSON: días del programa que aplican
);

CREATE INDEX IF NOT EXISTS idx_patrones_estado ON patrones(estado);

-- =========================================================
-- COMPROMISOS (el usuario dijo que haría X)
-- =========================================================
CREATE TABLE IF NOT EXISTS compromisos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    creado_en TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    fecha_objetivo TEXT,
    descripcion TEXT NOT NULL,
    contexto TEXT,                -- de qué episodio salió
    cumplido INTEGER,             -- NULL = pendiente, 0 = no, 1 = sí
    nota_cierre TEXT,
    episodio_origen_id INTEGER,
    FOREIGN KEY(episodio_origen_id) REFERENCES episodios(id)
);

-- =========================================================
-- RESÚMENES PERIÓDICOS (semanales/mensuales)
-- =========================================================
CREATE TABLE IF NOT EXISTS resumenes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    periodo TEXT NOT NULL,        -- 'semanal' | 'mensual'
    desde TEXT NOT NULL,
    hasta TEXT NOT NULL,
    resumen TEXT NOT NULL,
    foco_proximo_periodo TEXT,
    patrones_destacados TEXT      -- JSON ids
);
"""

def main():
    con = sqlite3.connect(DB_PATH)
    con.executescript(SCHEMA)
    
    # Perfil inicial vacío (versión 1)
    cur = con.execute("SELECT COUNT(*) FROM perfil")
    if cur.fetchone()[0] == 0:
        con.execute("""
            INSERT INTO perfil (version, valores_centrales, metas_actuales,
                creencias_limitantes, creencias_potenciadoras, fortalezas,
                areas_estancamiento, relaciones_clave, disparadores_emocionales,
                nota_libre)
            VALUES (1, '[]','[]','[]','[]','[]','[]','[]','[]',
                'Perfil inicial - se irá enriqueciendo con cada conversación')
        """)
    con.commit()
    con.close()
    print(f"Memoria inicializada en {DB_PATH.resolve()}")

if __name__ == "__main__":
    main()
