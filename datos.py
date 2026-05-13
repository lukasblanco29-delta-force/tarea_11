# ============================================================
# datos.py — Datos iniciales para DolarTrack
# Proyecto: Reto 3 - Economía "Dolar-Track"
# ============================================================

# Datos históricos de TRM (COP por 1 USD) - últimas semanas
TRM_HISTORICA = [
    {"fecha": "2025-04-01", "moneda": "USD", "trm": 4050.50},
    {"fecha": "2025-04-02", "moneda": "USD", "trm": 4075.25},
    {"fecha": "2025-04-03", "moneda": "USD", "trm": 4102.00},
    {"fecha": "2025-04-04", "moneda": "USD", "trm": 4088.75},
    {"fecha": "2025-04-07", "moneda": "USD", "trm": 4120.30},
    {"fecha": "2025-04-08", "moneda": "USD", "trm": 4135.10},
    {"fecha": "2025-04-09", "moneda": "USD", "trm": 4095.60},
    {"fecha": "2025-04-10", "moneda": "USD", "trm": 4060.40},
    {"fecha": "2025-04-11", "moneda": "USD", "trm": 4145.80},
    {"fecha": "2025-04-14", "moneda": "USD", "trm": 4180.90},
]

# Datos históricos EUR/COP
EUR_HISTORICA = [
    {"fecha": "2025-04-01", "moneda": "EUR", "trm": 4420.10},
    {"fecha": "2025-04-02", "moneda": "EUR", "trm": 4445.30},
    {"fecha": "2025-04-03", "moneda": "EUR", "trm": 4462.75},
    {"fecha": "2025-04-04", "moneda": "EUR", "trm": 4438.20},
    {"fecha": "2025-04-07", "moneda": "EUR", "trm": 4478.50},
    {"fecha": "2025-04-08", "moneda": "EUR", "trm": 4492.00},
    {"fecha": "2025-04-09", "moneda": "EUR", "trm": 4455.65},
    {"fecha": "2025-04-10", "moneda": "EUR", "trm": 4430.40},
    {"fecha": "2025-04-11", "moneda": "EUR", "trm": 4510.20},
    {"fecha": "2025-04-14", "moneda": "EUR", "trm": 4540.80},
]

# Inversionistas de ejemplo
INVERSIONISTAS_INICIALES = [
    {"nombre": "Carlos Mendez",    "capital_cop": 10_000_000, "perfil": "Conservador"},
    {"nombre": "Laura Jimenez",    "capital_cop": 25_000_000, "perfil": "Moderado"},
    {"nombre": "Andres Rios",      "capital_cop": 50_000_000, "perfil": "Agresivo"},
    {"nombre": "Maria Fernandez",  "capital_cop": 15_000_000, "perfil": "Moderado"},
]

# Umbrales para alertas
UMBRAL_VOLATILIDAD_ALTA = 2.0   # % de coeficiente de variación
UMBRAL_ALERTA_VENTA    = 1.02   # TRM > 2% sobre promedio → VENDER
UMBRAL_ALERTA_COMPRA   = 0.98   # TRM < 2% bajo promedio  → COMPRAR
