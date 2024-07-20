import json
import requests
import time
current_timestamp = int(time.time() * 1000)
url = "https://euapi.ttlock.com/v3/group/list"

# Datos de la solicitud
data = {
    'clientId': 'f9f9006b506248278f857f0734d1cc34',
    'accessToken': '010e282e4c9fb698f23c114c3d7ddd2b',
    'name': 'The 4th floor',
    'date': current_timestamp
}

# Realizar la solicitud POST
response = requests.post(url, data=data)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    try:
        # Intentar cargar el JSON solo si la respuesta no está vacía
        result = response.json()
        group_id = result.get('groupId')
        group_name = result.get('name')
        print(f"Response Content: {response.text}")
        print(f"Group ID: {group_id}")
        print(f"Group Name: {group_name}")
    except json.decoder.JSONDecodeError as e:
        print(f"Error al decodificar JSON: {e}")
else:
    print(f"Error en la solicitud. Código de estado: {response.status_code}")
    # Imprimir el contenido de la respuesta en caso de un código de estado 400
    if response.status_code == 400:
        print(f"Contenido de la respuesta: {response.text}")
