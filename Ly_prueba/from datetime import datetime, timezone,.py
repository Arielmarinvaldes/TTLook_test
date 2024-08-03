# from datetime import datetime, timezone, timedelta
import time

# # Tiempo en milisegundos
# time_in_milliseconds = 1721409921000

# # Convertir milisegundos a segundos
# time_in_seconds = time_in_milliseconds / 1000

# # Convertir segundos a un objeto datetime
# converted_date = datetime(1970, 1, 1, tzinfo=timezone.utc) + timedelta(seconds=time_in_seconds)

# # Formatear la fecha y hora en una cadena legible
# formatted_date = converted_date.strftime('%d/%m/%Y %H:%M:%S.%f')[:-3]

# print(f"Fecha y hora convertida: {formatted_date}")


x = 1721409921000

from datetime import datetime

# Definir las fechas
y = "2024-07-19 19:15:00"
z = "2024-07-21 19:15:00"

# Formato de las fechas
date_format = "%Y-%m-%d %H:%M:%S"

# Convertir las cadenas de fecha a objetos datetime
y_datetime = datetime.strptime(y, date_format)
z_datetime = datetime.strptime(z, date_format)

# Convertir los objetos datetime a milisegundos desde la época (epoch)
y_milliseconds = int(y_datetime.timestamp() * 1000)
z_milliseconds = int(z_datetime.timestamp() * 1000)

print("Fecha de inicio en milisegundos:", y_milliseconds)
print("Fecha de fin en milisegundos:", z_milliseconds)



def fecha_hora_a_milisegundos(fecha_str, hora_str):
    """
    Convierte una fecha y hora dadas en formato de cadena a un timestamp en milisegundos.
    Args:
        fecha_str (str): Fecha en formato 'dd-mm-yyyy'.
        hora_str (str): Hora en formato 'HH:MM:SS'.
    Returns:
        int: Timestamp en milisegundos.
    """
    # Convertir la fecha y la hora en un objeto datetime
    dt = datetime.strptime(f"{fecha_str} {hora_str}", "%d-%m-%Y %H:%M:%S")
    # Obtener el timestamp en segundos y convertirlo a milisegundos
    timestamp_milisegundos = int(dt.timestamp() * 1000)
    return timestamp_milisegundos