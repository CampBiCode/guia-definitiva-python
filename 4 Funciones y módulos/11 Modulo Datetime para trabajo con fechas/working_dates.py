import datetime as dt

# Introducción a datetime

## el paquete incluye tres módulos
dt.date # almacena datos de año, mes y día
dt.time # almacena datos de tiempo hora, minuto, segundo y microsegundo
dt.datetime # es una combinación de la fecha y tiempo, tiene todos las funcionalidades de los dos

## crear fechas y horas
print(dt.date(year = 2020, month = 1, day = 31))
print(dt.time(hour = 13, minute = 14, second = 31))
print(dt.datetime(year = 2020, month = 1, day = 31, hour = 13, minute = 14, second = 31))

hoy = dt.date.today()
ahora = dt.datetime.now()

## convertir cadenas de texto a fechas
fecha_texto = "2020-01-31" # debe seguir el formato ISO 8601 (YYYY-MM-DD HH:MM:SS)
print(dt.date.fromisoformat(fecha_texto)) 

### convertir texto que no esta en formato ISO 8601
fecha_texto = "01-31-2020 14:45:37"
formato_fecha = "%m-%d-%Y %H:%M:%S"
fecha_convertida = dt.datetime.strptime(fecha_texto, formato_fecha)
print(fecha_convertida)



# Configurar zonas horarias
## pip install python-dateutil
from dateutil import tz
print(fecha_convertida.replace(tzinfo = tz.gettz("America/New_York")))



# Operaciones de tiempo
## se utiliza la función timedelta
ahora = dt.datetime.now()
mañana = dt.timedelta(days = 1)
print(ahora + mañana)
print(ahora - dt.timedelta(days = 100))
print(ahora + dt.timedelta(days = 1, hours = -5))
