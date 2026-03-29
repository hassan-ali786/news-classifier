import os
import pickle
import sys

# Fix path
sys.path.append(os.path.dirname(__file__))

from preprocessing import clean_text

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "models", "model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "models", "vectorizer.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(vectorizer_path, "rb") as f:
    vectorizer = pickle.load(f)

def predict_category(text):
    text = clean_text(text)
    X = vectorizer.transform([text])
    pred = model.predict(X)[0]
    conf = max(model.predict_proba(X)[0])
    return pred, conf