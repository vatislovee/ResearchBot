import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "ids": "bitcoin,ethereum,cardano",
    "order": "market_cap_desc",
    "per_page": 100,
    "page": 1,
    "sparkline": False
}

response = requests.get(url, params=params)
data = response.json()


df = pd.DataFrame(data)
df.to_csv("crypto_prices.csv", index=False)
print("Saved latest crypto prices to crypto_prices.csv")
