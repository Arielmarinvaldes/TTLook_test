import requests
import json
import hashlib


url = "https://euapi.ttlock.com/oauth2/token"

# Datos de la solicitud
data = {
    # 'clientId': '196767a6f0e14a58ad4bddd75ae14c79', # tio
    'clientId': 'f9f9006b506248278f857f0734d1cc34',
    'clientSecret': '73b7b5036fb27868ab559687e25ffb48',
    # 'clientSecret': '80abd30a306d4a7774318cc3f4ee4920',# tio
    'username': 'h_1708279453702',
    # 'username': 'h_1700474729996', # tio
    'password': hashlib.md5('Ariel.01'.encode()).hexdigest()
    # 'password': hashlib.md5('Gollo@tthotel.24'.encode()).hexdigest() # tio
}
#  12345678901234567890123456789012

# Realizr la solicitud POST
response = requests.post(url, data=data)

# Verifica si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    try:
        # Intentar cargar el JSON solo si la respuesta no está vacía
        result = response.json()
        access_token = result.get('access_token')
        uid = result.get('uid')
        expires_in = result.get('expires_in')
        refresh_token = result.get('refresh_token')
        print(f"Response Content: {response.text}")
        print(f"Access Token: {access_token}")
        print(f"User ID: {uid}")
        print(f"Expires In: {expires_in} seconds")
        print(f"Refresh Token: {refresh_token}")
    except json.decoder.JSONDecodeError as e:
        print(f"Error al decodificar JSON: {e}")
else:
    print(f"Error en la solicitud. Código de estado: {response.status_code}")
    # Imprimir el contenido de la respuesta en caso de un código de estado 400
    if response.status_code == 400:
        print(f"Contenido de la respuesta: {response.text}")