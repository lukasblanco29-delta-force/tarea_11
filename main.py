#!/usr/bin/env python3
# ============================================================
# main.py — Orquestador principal de DolarTrack
# Reto 3: Economía "Dolar-Track"
# Arquitectura: Backend (SQLite) ↔ Frontend (Tkinter + Pillow)
# ============================================================

import os
import sys
import sqlite3
from datetime import datetime

# ── Rutas del proyecto ──────────────────────────────────────
BASE_DIR     = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR  = os.path.join(BASE_DIR, "Backend")
FRONTEND_DIR = os.path.join(BASE_DIR, "Frontend")
DB_PATH      = os.path.join(BACKEND_DIR, "dolar_track.db")

sys.path.insert(0, BACKEND_DIR)
sys.path.insert(0, FRONTEND_DIR)

from datos import TRM_HISTORICA, EUR_HISTORICA, INVERSIONISTAS_INICIALES


# ════════════════════════════════════════════════════════════
#  INICIALIZACIÓN DE LA BASE DE DATOS
# ════════════════════════════════════════════════════════════
def crear_base_de_datos():
    """Crea tablas y carga datos semilla si la BD no existe."""
    primera_vez = not os.path.exists(DB_PATH)
    con = sqlite3.connect(DB_PATH)
    con.execute("PRAGMA foreign_keys = ON")

    con.executescript("""
        CREATE TABLE IF NOT EXISTS trm (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha   TEXT    NOT NULL,
            moneda  TEXT    NOT NULL DEFAULT 'USD',
            trm     REAL    NOT NULL,
            UNIQUE(fecha, moneda)
        );
        CREATE TABLE IF NOT EXISTS inversionistas (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre      TEXT    NOT NULL,
            capital_cop REAL    NOT NULL,
            perfil      TEXT    NOT NULL
        );
        CREATE TABLE IF NOT EXISTS operaciones (
            id               INTEGER PRIMARY KEY AUTOINCREMENT,
            id_inversionista INTEGER NOT NULL REFERENCES inversionistas(id),
            moneda           TEXT    NOT NULL,
            tipo             TEXT    NOT NULL,
            monto_usd        REAL    NOT NULL,
            trm              REAL    NOT NULL,
            monto_cop        REAL    NOT NULL,
            fecha            TEXT    NOT NULL
        );
        CREATE TABLE IF NOT EXISTS alertas (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            moneda      TEXT    NOT NULL,
            tipo_alerta TEXT    NOT NULL,
            trm         REAL    NOT NULL,
            promedio    REAL    NOT NULL,
            fecha       TEXT    NOT NULL
        );
    """)
    con.commit()

    if primera_vez:
        print("  ✅  Base de datos creada. Cargando datos iniciales...")
        for r in TRM_HISTORICA + EUR_HISTORICA:
            try:
                con.execute(
                    "INSERT INTO trm (fecha, moneda, trm) VALUES (?,?,?)",
                    (r["fecha"], r["moneda"], r["trm"]),
                )
            except sqlite3.IntegrityError:
                pass
        for inv in INVERSIONISTAS_INICIALES:
            con.execute(
                "INSERT INTO inversionistas (nombre, capital_cop, perfil) VALUES (?,?,?)",
                (inv["nombre"], inv["capital_cop"], inv["perfil"]),
            )
        con.commit()
        print("  ✅  Datos iniciales cargados correctamente.\n")

    con.close()


# ════════════════════════════════════════════════════════════
#  PUNTO DE ENTRADA
# ════════════════════════════════════════════════════════════
def main():
    print("""
  ╔══════════════════════════════════════════════════╗
  ║     💵  DOLAR-TRACK — Analítica Cambiaria  💵   ║
  ║         Reto 3: Economía y Finanzas             ║
  ╚══════════════════════════════════════════════════╝
    """)
    print(f"  📂  Base de datos : {DB_PATH}")

    # 1. Inicializar BD
    crear_base_de_datos()

    # 2. Lanzar GUI
    print("  🖥   Iniciando interfaz gráfica DolarTrack...\n")
    from interfaz import iniciar
    iniciar()


if __name__ == "__main__":
    main()
