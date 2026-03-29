import pandas as pd
import pickle
import os
import sys

# Fix path
sys.path.append(os.path.dirname(__file__))

from preprocessing import clean_text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_path = os.path.join(BASE_DIR, "data", "news.csv")
model_path = os.path.join(BASE_DIR, "models", "model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "models", "vectorizer.pkl")

os.makedirs(os.path.join(BASE_DIR, "models"), exist_ok=True)

# Load dataset
df = pd.read_csv(data_path, header=None)
df.columns = ["category", "title", "description"]

# Combine + clean
df["text"] = (df["title"] + " " + df["description"]).apply(clean_text)

X = df["text"]
y = df["category"]

# Vectorize
vectorizer = TfidfVectorizer(max_features=5000)
X_vect = vectorizer.fit_transform(X)

# Train
model = MultinomialNB()
model.fit(X_vect, y)

# Save
with open(model_path, "wb") as f:
    pickle.dump(model, f)

with open(vectorizer_path, "wb") as f:
    pickle.dump(vectorizer, f)

print("Model trained and saved!")