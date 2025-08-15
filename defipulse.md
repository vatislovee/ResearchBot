# DeFi Pulse API

**Purpose:** Fetches analytics and rankings for DeFi projects.

## API Endpoint
- `https://data.defipulse.com/api/v1/defipulse/api/GetProjects`
- Parameters:
  - `api-key`: your personal API key (register on DeFi Pulse)


import requests

url = "https://data.defipulse.com/api/v1/defipulse/api/GetProjects"
params = {"api-key": "YOUR_API_KEY"}
response = requests.get(url, params=params)
data = response.json()
print(data)
