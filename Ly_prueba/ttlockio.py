# ttlockwrapper.py

import requests

class TTLock:
    def __init__(self, clientId, accessToken=None):
        self.clientId = clientId
        self.accessToken = accessToken

    def create_user(self, clientSecret, username, password, token=False):
        url = "https://euopen.ttlock.com/api/oauth2/user/register"
        data = {
            "client_id": self.clientId,
            "client_secret": clientSecret,
            "username": username,
            "password": password,
            "token": token
        }
        response = requests.post(url, data=data)
        return response.json()

    def refresh_access_token(self, clientSecret, refreshToken):
        url = "https://euopen.ttlock.com/api/oauth2/token"
        data = {
            "client_id": self.clientId,
            "client_secret": clientSecret,
            "refresh_token": refreshToken,
            "grant_type": "refresh_token"
        }
        response = requests.post(url, data=data)
        return response.json()

# Example Usage
if __name__ == "__main__":
    # Replace these with your actual values
    clientId = 'f9f9006b506248278f857f0734d1cc34'
    clientSecret = '73b7b5036fb27868ab559687e25ffb48'
    username = 'h_1708279453702'
    password = 'Ariel.01'

    ttlock = TTLock(clientId)

    # Create a user
    user_creation_result = ttlock.create_user(clientSecret, username, password, token=True)
    print("User Creation Result:", user_creation_result)

    if 'access_token' in user_creation_result:
        # Access token obtained, refresh when required
        accessToken = user_creation_result['access_token']
        refreshToken = user_creation_result['refresh_token']

        # Refresh access token
        refresh_result = ttlock.refresh_access_token(clientSecret, refreshToken)
        print("Token Refresh Result:", refresh_result)

        if 'access_token' in refresh_result:
            # Test your user or perform other actions
            print("Testing User:")
            # Your logic to test the user can go here
