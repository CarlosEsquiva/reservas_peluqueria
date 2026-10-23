"""
Prueba de conexión con Google Calendar.
1. Lista los eventos de los próximos 7 días.
2. Crea una cita de prueba mañana a las 10:00 (30 min).

Requisitos:
    pip install google-api-python-client google-auth
"""
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from google.oauth2 import service_account
from googleapiclient.discovery import build

CREDENCIALES = "credenciales.json"  # clave JSON de la cuenta de servicio (¡nunca a Git!)
CALENDAR_ID = "PEGA_AQUI_EL_ID@group.calendar.google.com"
TZ = ZoneInfo("Europe/Madrid")
SCOPES = ["https://www.googleapis.com/auth/calendar"]

creds = service_account.Credentials.from_service_account_file(CREDENCIALES, scopes=SCOPES)
service = build("calendar", "v3", credentials=creds)

ahora = datetime.now(TZ)

# 1. Listar eventos de los próximos 7 días
resultado = service.events().list(
    calendarId=CALENDAR_ID,
    timeMin=ahora.isoformat(),
    timeMax=(ahora + timedelta(days=7)).isoformat(),
    singleEvents=True,
    orderBy="startTime",
).execute()

eventos = resultado.get("items", [])
print(f"Eventos próximos 7 días: {len(eventos)}")
for ev in eventos:
    inicio = ev["start"].get("dateTime", ev["start"].get("date"))
    print(f"  - {inicio}  {ev.get('summary', '(sin título)')}")

# 2. Crear cita de prueba mañana a las 10:00
inicio = (ahora + timedelta(days=1)).replace(hour=10, minute=0, second=0, microsecond=0)
fin = inicio + timedelta(minutes=30)

evento = {
    "summary": "PRUEBA - Corte de pelo (Juan, 600000000)",
    "description": "Reserva creada desde el sistema de citas",
    "start": {"dateTime": inicio.isoformat(), "timeZone": "Europe/Madrid"},
    "end": {"dateTime": fin.isoformat(), "timeZone": "Europe/Madrid"},
}

creado = service.events().insert(calendarId=CALENDAR_ID, body=evento).execute()
print(f"\nCita creada: {creado.get('htmlLink')}")
