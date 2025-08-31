# kaspa_price.py

import requests
import csv
from datetime import datetime
import os
print("Saving CSV in:", os.getcwd())

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
def save_price_to_csv(price,filename="kaspa_price.csv"):
    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists=os.path.isfile(filename)

    with open(filename, mode="a",newline="") as file:
        writer =csv.writer(file)
        if not file_exists:
            writer.writerow(["timestamp","price_usd"])
        writer.writerow([timestamp,price])


if __name__ == "__main__":
    price = get_kaspa_price()
    if price is not None:
        print(f"Current Kaspa price: ${price}")
        save_price_to_csv(price)
        print("Price saved to CSV.")
    else:
        print("Could not fetch Kaspa price.")
