import pandas as pd

df = pd.read_csv("crypto_prices.csv")

summary = {
    "total_tokens": len(df),
    "average_price": df["current_price"].mean(),
    "highest_price_token": df.loc[df["current_price"].idxmax(), "name"],
    "lowest_price_token": df.loc[df["current_price"].idxmin(), "name"]
}

print("=== Crypto Market Summary ===")
for k, v in summary.items():
    print(f"{k}: {v}")
