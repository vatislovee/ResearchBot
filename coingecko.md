# CoinGecko API

**Purpose:** Fetches real-time cryptocurrency prices, market cap, and trading volume.

## API Endpoint
- `https://api.coingecko.com/api/v3/coins/markets`
- Parameters:
  - `vs_currency`: fiat currency (e.g., USD)
  - `ids`: comma-separated list of token IDs
  - `order`: market cap, volume, etc.
  - `per_page`: number of results per page

## Usage Example (Python)
```python
import requests

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {"vs_currency": "usd", "ids": "bitcoin,ethereum"}
response = requests.get(url, params=params)
data = response.json()
print(data)
