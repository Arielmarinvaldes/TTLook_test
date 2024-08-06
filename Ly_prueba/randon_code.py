import requests
import json
import time

current_timestamp = int(time.time() * 1000)
url = "https://euapi.ttlock.com/v3/keyboardPwd/get"

# Datos de la solicitud
data = {
    'clientId': '???',
    'accessToken': '????',
    'lockId': "???",
    'keyboardPwdType': 3,
    'keyboardPwdName': 'test',
    'startDate': "???",
    'endDate':"???",
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



