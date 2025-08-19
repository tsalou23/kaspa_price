import requests

url = "https://api.example.com/kaspa-price"
response = requests.get(url)
data = response.json()

print("Kaspa Price:", data["price"])