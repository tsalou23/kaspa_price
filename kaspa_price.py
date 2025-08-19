# kaspa_price.py

import requests

def get_kaspa_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "kaspa",
        "vs_currencies": "usd"
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise error if request failed
        data = response.json()
        price = data["kaspa"]["usd"]
        return price
    except requests.exceptions.RequestException as e:
        print("Error fetching price:", e)
        return None

if __name__ == "__main__":
    price = get_kaspa_price()
    if price is not None:
        print(f"Current Kaspa price: ${price}")
    else:
        print("Could not fetch Kaspa price.")
