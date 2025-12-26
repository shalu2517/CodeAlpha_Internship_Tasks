# SENTIMENT ANALYSIS

import pandas as pd
import nltk
import re
from nltk.corpus import stopwords
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

# one-time download (internet needed only once)
nltk.download('stopwords')

# load dataset
df = pd.read_csv("amazon_reviews.csv")

# check data
print(df.info())
print(df.isnull().sum())

# stopwords
stop_words = set(stopwords.words('english'))

# text cleaning function
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

df['clean_review'] = df['reviewText'].apply(clean_text)

# sentiment function
def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

df['sentiment'] = df['clean_review'].apply(get_sentiment)

# emotion function
def get_emotion(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.5:
        return "Joy"
    elif polarity < -0.5:
        return "Anger"
    else:
        return "Neutral"

df['emotion'] = df['clean_review'].apply(get_emotion)

# counts
print(df['sentiment'].value_counts())
print(df['emotion'].value_counts())

# sentiment plot
sns.countplot(x='sentiment', data=df)
plt.title("Sentiment Distribution")
plt.show()

# emotion plot
sns.countplot(x='emotion', data=df)
plt.title("Emotion Distribution")
plt.show()
