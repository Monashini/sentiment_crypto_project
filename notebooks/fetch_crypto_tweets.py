# fetch_crypto_tweets.py

import tweepy
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv

# === 1. AUTHENTICATE ===
# Replace with your Bearer Token
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAO5m2gEAAAAAhjZrZZGn%2FNlvy%2Fn4%2FxPRyvn5ThQ%3DwV36g91EfWPPhcEBLaryEffg215BXI2RUP2fUoEdMVNQx2v9I0"
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# === 2. SEARCH RECENT TWEETS ===
query = "bitcoin OR ethereum OR crypto OR BTC OR ETH -is:retweet lang:en"

response = client.search_recent_tweets(
    query=query,
    tweet_fields=["created_at", "text"],
    max_results=100
)

# === 3. PARSE RESULTS ===
tweets = []
for tweet in response.data:
    tweets.append({
        "created_at": tweet.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        "text": tweet.text.replace("\n", " ")
    })

# === 4. SAVE TO CSV ===
df = pd.DataFrame(tweets)
df.to_csv("data/crypto_live_tweets.csv", index=False)
print("✅ Fetched and saved 100 crypto tweets to 'data/crypto_live_tweets.csv'")
