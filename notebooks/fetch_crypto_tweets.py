# fetch_crypto_tweets.py

import tweepy
import pandas as pd
from datetime import datetime


# === 1. AUTHENTICATE ===
# Replace with your Bearer Token
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAO5m2gEAAAAAqZRYlzCH8z1Fs4znpxhbgySKOD4%3Dhoy9aiBRQSzH9MqqgDNkfWZXSOYRTRTJkgdq7S10JvmRu6UWU5"

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
