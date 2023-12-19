import requests
import json

def create_dev_token():
    try:
        # Replace 'YOUR_CLIENT_ID' and 'YOUR_CLIENT_SECRET' with your Discord application's client ID and client secret
        client_id = 'YOUR_CLIENT_ID'
        client_secret = 'YOUR_CLIENT_SECRET'

        # Discord API endpoint for token creation
        token_url = 'https://discord.com/api/oauth2/token'

        # Payload for token creation
        payload = {
            'client_id': client_id,
            'client_secret': client_secret,
            'grant_type': 'client_credentials',
            'scope': 'bot'
        }

        # Request a new token from Discord Dev API
        response = requests.post(token_url, data=payload)

        if response.status_code == 200:
            # Parse the response JSON and extract the access token
            access_token = json.loads(response.text)['access_token']
            return access_token
        else:
            print(f"Error creating Dev API token: {response.text}")
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None

def save_token_to_file(token, file_path='tokens.txt'):
    try:
        # Save the token in the specified file
        with open(file_path, 'a') as file:
            file.write(token + '\n')
        print(f"Token saved to {file_path} successfully.")
    except Exception as e:
        print(f"Error saving token to file: {e}")

# Example usage
dev_token = create_dev_token()
if dev_token:
    save_token_to_file(dev_token)
    print(f"Generated Dev API Token: {dev_token}")
