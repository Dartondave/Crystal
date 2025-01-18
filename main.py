import requests
import time

# Function to read tokens from datas.txt
def read_tokens(file_path):
    try:
        with open(file_path, 'r') as file:
            tokens = [line.strip() for line in file.readlines()]
        return tokens
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []

# Define request functions
def send_request(url, headers, data=None):
    try:
        response = requests.post(url, headers=headers, json=data)
        print(f"Response: {response.status_code} - {response.text}")
        return response
    except Exception as e:
        print(f"Request error: {e}")
        return None

def send_clicks(auth_token):
    url = 'https://crystalton.ru/api/clicks'
    headers = {
        'Authorization': f'Bearer {auth_token}',
        'Content-Type': 'application/json;charset=utf-8',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1'
    }
    data = {"clicks": 500}
    print("Sending clicks...")
    send_request(url, headers, data)

def send_ad(auth_token):
    url = 'https://crystalton.ru/api/ads'
    headers = {
        'Authorization': f'Bearer {auth_token}',
        'Content-Type': 'application/json;charset=utf-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }
    data = {"ads_id": 6, "source": 3, "ads_partner": 1}
    print("Sending ad...")
    send_request(url, headers, data)

def send_spin(auth_token):
    url = 'https://crystalton.ru/api/fortune_wheel/spin'
    headers = {
        'Authorization': f'Bearer {auth_token}',
        'Content-Type': 'application/json;charset=utf-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }
    print("Sending spin...")
    send_request(url, headers)

# Main execution loop
def main():
    tokens = read_tokens("datas.txt")
    if not tokens:
        print("No valid tokens found. Exiting...")
        return

    while True:
        for token in tokens:
            print(f"Processing token: {token[:5]}...")  # Show partial token for logging
            send_clicks(token)

            # Loop to perform ad and spin actions for a fixed number of iterations
            for _ in range(5):  # Adjust the range to control repetitions
                send_ad(token)
                send_spin(token)
                time.sleep(0.00000000002)  # Prevent spamming the server

if __name__ == "__main__":
    while True:
        try:
            main()
        except Exception as e:
            print(f"An error occurred: {e}. Restarting in 1 second...")
            time.sleep(1)