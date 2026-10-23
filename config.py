"""
Configuración del negocio. Ajusta estos datos con el peluquero.
"""

NOMBRE_NEGOCIO = "Peluquería de prueba"
ZONA_HORARIA = "Europe/Madrid"

# Servicios: clave interna -> nombre visible y duración en minutos
SERVICIOS = {
    "corte": {"nombre": "Corte de pelo", "duracion": 30},
    "corte_barba": {"nombre": "Corte + barba", "duracion": 45},
    "barba": {"nombre": "Arreglo de barba", "duracion": 20},
    "tinte": {"nombre": "Tinte", "duracion": 60},
}

# Horario semanal: 0 = lunes ... 6 = domingo. Lista vacía = cerrado.
HORARIO = {
    0: [],                                         # lunes cerrado
    1: [("09:30", "13:30"), ("16:30", "20:00")],
    2: [("09:30", "13:30"), ("16:30", "20:00")],
    3: [("09:30", "13:30"), ("16:30", "20:00")],
    4: [("09:30", "13:30"), ("16:30", "20:00")],
    5: [("09:00", "14:00")],                       # sábado solo mañana
    6: [],                                         # domingo cerrado
}

# Cada cuántos minutos se ofrecen horas de inicio (10:00, 10:15, 10:30...)
INTERVALO_HUECOS = 15

# Con cuánta antelación mínima se puede reservar (minutos) y hasta cuántos días vista
ANTELACION_MINIMA = 60
DIAS_VISTA = 30