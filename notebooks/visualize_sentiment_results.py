# visualize_sentiment_results.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the predicted results
df = pd.read_csv('output/live_crypto_sentiment.csv')

# 2. Count sentiment categories
sentiment_counts = df['predicted_sentiment'].value_counts()

# 3. Plot the sentiment distribution
plt.figure(figsize=(6, 4))
sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette='Set2')
plt.title("Live Crypto Tweet Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Tweets")
plt.tight_layout()

# 4. Save the figure
plt.savefig("output/sentiment_distribution.png")
plt.show()
