import requests
import json
import time
current_timestamp = int(time.time() * 1000)
url = "https://euapi.ttlock.com/v3/lock/list"

# Datos de la solicitud
params = {
    'clientId': '196767a6f0e14a58ad4bddd75ae14c79',
    'accessToken': '51c4131921dc7d4c5874ffac76857ab3',
    'pageNo': 1,
    'pageSize': 20,
    'date': current_timestamp,
    # 'groupId': 618038
}
# Realizar la solicitud GET
response = requests.get(url, params=params)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    try:
        # Intentar cargar el JSON solo si la respuesta no está vacía
        result = response.json()
        
        # Imprimir información sobre los candados
        locks_list = result.get('list', [])

        if locks_list:
            print("List of Locks:")
            for lock in locks_list:
                print(f"Lock ID: {lock.get('lockId')}")
                print(f"Lock Name: {lock.get('lockName')}")
                print(f"Lock Alias: {lock.get('lockAlias')}")
                print(f"Lock MAC: {lock.get('lockMac')}")
                print(f"Electric Quantity: {lock.get('electricQuantity')}")
                print(f"Feature Value: {lock.get('featureValue')}")
                print(f"Has Gateway: {lock.get('hasGateway')}")
                print(f"Group ID: {lock.get('groupId')}")
                print(f"Group Name: {lock.get('groupName')}")
                print(f"Lock Init Time: {lock.get('date')}")
                print("\n")

        else:
            print("No locks found.")
    except json.decoder.JSONDecodeError as e:
        print(f"Error al decodificar JSON: {e}")
else:
    print(f"Error en la solicitud. Código de estado: {response.status_code}")
    # Imprimir el contenido de la respuesta en caso de un código de estado 400
    if response.status_code == 400:
        print(f"Contenido de la respuesta: {response.text}")