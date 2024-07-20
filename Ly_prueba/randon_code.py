import requests
import json
import time

current_timestamp = int(time.time() * 1000)

# Calcula la duración de 24 horas en milisegundos
duration_24_hours = 24 * 60 * 60 * 1000
end_timestamp = current_timestamp + duration_24_hours

url = "https://euapi.ttlock.com/v3/keyboardPwd/get"

# Datos de la solicitud
data = {
    'clientId': 'f9f9006b506248278f857f0734d1cc34',
    'accessToken': '010e282e4c9fb698f23c114c3d7ddd2b',
    # 'lockId': 10463855, # tio
    'lockId': 13345048,
    'keyboardPwdType': 3,
    'keyboardPwdName': 'test',
    'startDate': "2024-20-19 09:59:00",
    'endDate':"2025-10-18 00:00:00",
    'date': current_timestamp
}

# Realizar la solicitud POST
response = requests.post(url, data=data)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    try:
        # Intentar cargar el JSON solo si la respuesta no está vacía
        result = response.json()
        keyboard_pwd = result.get('keyboardPwd')
        keyboard_pwd_id = result.get('keyboardPwdId')
        print(f"Response Content: {response.text}")
        print(f"Passcode: {keyboard_pwd}")
        print(f"Passcode ID: {keyboard_pwd_id}")
    except json.decoder.JSONDecodeError as e:
        print(f"Error al decodificar JSON: {e}")
else:
    print(f"Error en la solicitud. Código de estado: {response.status_code}")
    # Imprimir el contenido de la respuesta en caso de un código de estado 400
    if response.status_code == 400:
        print(f"Contenido de la respuesta: {response.text}")
