import pandas as pd
import numpy as np
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
data = pd.read_csv("urls.csv")
print("Dataset Sample:")
print(data.head())
def clean_url(url):
    url = str(url)
    url = url.lower()
    url = re.sub(r'http[s]?://', '', url)
    url = re.sub(r'www\.', '', url)
    return url
data['clean_url'] = data['url'].apply(clean_url)
print("\nDataset Info:")
print(data.info())
print("\nClass Distribution:")
print(data['label'].value_counts())
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['clean_url'])
y = data['label']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("\nModel Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
def predict_url(url):
    url = clean_url(url)
    url_vec = vectorizer.transform([url])
    prediction = model.predict(url_vec)[0]
    if prediction == 1:
        print("Malicious URL")
    else:
        print("Safe URL")
predict_url("http://example-login-secure.com")