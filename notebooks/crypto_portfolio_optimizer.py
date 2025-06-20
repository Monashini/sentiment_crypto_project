import pandas as pd

# === STEP 1: Load Data ===
sentiment_data = pd.read_csv("output/live_crypto_sentiment.csv")
price_data = pd.read_csv("data/crypto_prices.csv")

# === STEP 2: Identify Coin from Text ===
sentiment_data["coin"] = sentiment_data["cleaned_text"].apply(
    lambda x: "bitcoin" if "bitcoin" in x.lower() or "btc" in x.lower()
    else ("ethereum" if "ethereum" in x.lower() or "eth" in x.lower() else "other")
)
sentiment_data = sentiment_data[sentiment_data["coin"] != "other"]

# === STEP 3: Map Sentiment Labels to Scores ===
sentiment_map = {"positive": 1.0, "neutral": 0.5, "negative": 0.0}
sentiment_data["sentiment_score"] = sentiment_data["predicted_sentiment"].map(sentiment_map)

# === STEP 4: Aggregate Sentiment Scores per Coin ===
avg_sentiment = sentiment_data.groupby("coin")["sentiment_score"].mean().to_dict()

# === STEP 5: Load Prices ===
price_data.set_index("coin", inplace=True)
prices = price_data["price"].to_dict()

# === STEP 6: Normalize Sentiment Scores to Weights ===
total_score = sum(avg_sentiment.values())
weights = {coin: score / total_score for coin, score in avg_sentiment.items()}

# === STEP 7: Portfolio Allocation Based on Weights and Prices ===
portfolio_value = 10000  # say you want to invest $10,000

allocation = {}
for coin, weight in weights.items():
    usd_amount = portfolio_value * weight
    coin_price = prices.get(coin, 1)  # avoid division by zero
    units = usd_amount / coin_price
    allocation[coin] = {
        "sentiment_weight": round(weight, 4),
        "usd_allocated": round(usd_amount, 2),
        "coin_price": round(coin_price, 2),
        "units_to_buy": round(units, 6)
    }

# === STEP 8: Save Allocation to CSV ===
alloc_df = pd.DataFrame.from_dict(allocation, orient="index")
alloc_df.index.name = "coin"
alloc_df.reset_index(inplace=True)
alloc_df.to_csv("output/portfolio_allocation.csv", index=False)

# === STEP 9: Show Summary ===
print("\n✅ Optimal Portfolio Allocation (based on sentiment):\n")
print(alloc_df)
