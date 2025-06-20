# predict_live_crypto_sentiment.py

import pandas as pd
from joblib import load

# Load model and vectorizer
model = load("models/sentiment_model.joblib")
vectorizer = load("models/vectorizer.joblib")

# Load fetched live tweets
df = pd.read_csv("data/crypto_live_tweets.csv")

# Preprocess (optional: basic lowercasing and stripping)
df['cleaned_text'] = df['text'].astype(str).str.lower().str.strip()

# Vectorize
X = vectorizer.transform(df['cleaned_text'])

# Predict
df['predicted_sentiment'] = model.predict(X)

# Save results
df.to_csv("output/live_crypto_sentiment.csv", index=False)

print("✅ Live tweet sentiments saved to 'output/live_crypto_sentiment.csv'")
