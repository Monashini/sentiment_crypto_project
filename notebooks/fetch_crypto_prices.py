import requests
import pandas as pd
from datetime import datetime
import os

# === 1. Set your API and coin details ===
COINS = ['bitcoin', 'ethereum']
CURRENCY = 'usd'

# === 2. Fetch prices from CoinGecko ===
data = []
for coin in COINS:
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies={CURRENCY}"
    response = requests.get(url)
    result = response.json()
    price = result[coin][CURRENCY]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data.append({"coin": coin, "price": price, "timestamp": timestamp})

# === 3. Save to CSV ===
df = pd.DataFrame(data)
os.makedirs("data", exist_ok=True)
df.to_csv("data/crypto_prices.csv", index=False)
print("✅ Crypto prices saved to 'data/crypto_prices.csv'")
