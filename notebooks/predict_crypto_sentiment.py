import pandas as pd
from joblib import load

# Load trained model & vectorizer
model = load('models/sentiment_model.joblib')
vectorizer = load('models/vectorizer.joblib')

# Load new crypto-related tweets
df = pd.read_csv('/Users/mona/sentiment_crypto_project/data/cleaned_tweets.csv')  
# Preprocess text (assuming it's already cleaned for now)
texts = df['cleaned_text']

# Vectorize using the same TF-IDF
X = vectorizer.transform(texts)

# Predict sentiment
predictions = model.predict(X)

# Add predictions to DataFrame
df['predicted_sentiment'] = predictions

# Save output
df.to_csv('output/crypto_sentiment_predictions.csv', index=False)

print("✅ Crypto sentiment predictions saved to 'output/crypto_sentiment_predictions.csv'")
