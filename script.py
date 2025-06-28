import requests

ETHERSCAN_API_KEY = 'AI6WEBHE3VU51P134A4SC4WEUKPDF3DAH1'
WALLET_ADDRESS = '0x64ff401b86781f106e0202517d9590c2347f7d1f'

def get_balance(address):
    url = (
        f"https://api.etherscan.io/api"
        f"?module=account"
        f"&action=balance"
        f"&address={address}"
        f"&tag=latest"
        f"&apikey={ETHERSCAN_API_KEY}"
    )
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        if data['status'] == '1':
            wei = int(data['result'])
            eth = wei / 10**18
            return eth
        else:
            return f"Error from API: {data['message']}"
    except Exception as e:
        return f"Request failed: {e}"

def main():
    print(f"Checking balance for address: {WALLET_ADDRESS}")
    balance = get_balance(WALLET_ADDRESS)
    print(f"Balance: {balance} ETH")

if __name__ == "__main__":
    main()

