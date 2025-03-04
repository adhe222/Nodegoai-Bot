import requests
import time
import random
from colorama import init, Fore, Style

init(autoreset=True)

def load_proxies(file_path):
    try:
        with open(file_path, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"{Fore.RED}{Style.BRIGHT}[-] Proxy file not found: {file_path}")
        return []

def load_token(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f"{Fore.RED}{Style.BRIGHT}[-] Token file not found: {file_path}")
        return None

def send_get_request(url, headers, proxy=None):
    try:
        response = requests.get(url, headers=headers, proxies={'http': proxy, 'https': proxy}, timeout=10) if proxy else requests.get(url, headers=headers, timeout=10)
        status = f"via {proxy}" if proxy else ""
        print(f"{Fore.GREEN}{Style.BRIGHT}[+] GET request to {url} {status} - Status Code: {response.status_code}")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}{Style.BRIGHT}[-] Error sending GET request to {url}: {e}")

def send_post_request(url, headers, data, proxy=None):
    try:
        response = requests.post(url, headers=headers, json=data, proxies={'http': proxy, 'https': proxy}, timeout=10) if proxy else requests.post(url, headers=headers, json=data, timeout=10)
        status = f"via {proxy}" if proxy else ""
        print(f"{Fore.GREEN}{Style.BRIGHT}[+] POST request to {url} {status} - Status Code: {response.status_code}")
        data = response.json()
        print(f"{Fore.CYAN}{Style.BRIGHT}Response: {data}")
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}{Style.BRIGHT}[-] Error sending POST request to {url}: {e}")

url1 = "https://nodego.ai/api/user/me"
url2 = "https://api.bigdatacloud.net/data/client-ip"
url3 = "https://nodego.ai/api/user/nodes/ping"

headers1 = {
    'Accept': 'application/json, text/plain, */*',
    'Authorization': '',
    'If-None-Match': 'W/"20c5e-p11ymIrz3M94nwpGIZkYg9Hy8Ac"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'none',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}

headers2 = {
    'Accept': 'application/json, text/plain, */*',
    'Origin': 'chrome-extension://jbmdcnidiaknboflpljihfnbonjgegah',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}

headers3 = {
    'Accept': 'application/json, text/plain, */*',
    'Authorization': '',
    'Content-Type': 'application/json',
    'Origin': 'chrome-extension://jbmdcnidiaknboflpljihfnbonjgegah',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'none',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
}

data3 = {"key": "value"}

proxies = load_proxies('proxies.txt')
auth_token = load_token('token.txt')

if auth_token:
    headers1['Authorization'] = f'Bearer {auth_token}'
    headers3['Authorization'] = f'Bearer {auth_token}'

interval = 360

while True:
    selected_proxy = random.choice(proxies) if proxies else None

    send_get_request(url1, headers1, proxy=selected_proxy)
    send_get_request(url2, headers2, proxy=selected_proxy)
    send_post_request(url3, headers3, data3, proxy=selected_proxy)

    print(f"{Fore.YELLOW}{Style.BRIGHT}[~] Waiting {interval} seconds before the next request...")
    time.sleep(interval)
