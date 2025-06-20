import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from joblib import dump
from imblearn.over_sampling import RandomOverSampler

# 1. Load cleaned dataset
df = pd.read_csv('/Users/mona/Downloads/cleaned_tweets.csv')  
X = df['cleaned_text']
y = df['airline_sentiment']

# 2. Vectorize with bi-grams
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000, ngram_range=(1, 2))
X_vec = vectorizer.fit_transform(X)

# 3. Oversample minority classes
ros = RandomOverSampler(random_state=42)
X_resampled, y_resampled = ros.fit_resample(X_vec, y)

# 4. Train/test split
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

# 5. Train Logistic Regression
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 6. Evaluate performance
y_pred = model.predict(X_test)
print("\n🔍 Sentiment Classification Report:\n")
print(classification_report(y_test, y_pred))

# 7. Save model + vectorizer
dump(model, 'models/sentiment_model.joblib')
dump(vectorizer, 'models/vectorizer.joblib')
print("\n✅ Model and vectorizer saved in 'models/' folder.")
