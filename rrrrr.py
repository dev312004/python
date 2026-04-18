# Step 1: Import required libraries
import pandas as pd
import numpy as np
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Step 2: Acquiring the URL data
# Replace 'urls.csv' with your dataset file
# Dataset format example: url,label (label: 0=benign, 1=malicious)

data = pd.read_csv('urls.csv')

print("Dataset Sample:")
print(data.head())

# Step 3: Data Preprocessing

# Function to clean URLs
def clean_url(url):
    url = str(url)
    url = url.lower()
    url = re.sub(r'http[s]?://', '', url)
    url = re.sub(r'www\.', '', url)
    return url

data['clean_url'] = data['url'].apply(clean_url)

# Step 4: Data Exploration
print("\nDataset Info:")
print(data.info())

print("\nClass Distribution:")
print(data['label'].value_counts())

# Step 5: Feature Extraction (Convert text to numerical features)
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['clean_url'])
y = data['label']

# Step 6: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 7: Model Building
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Step 8: Prediction
y_pred = model.predict(X_test)

# Step 9: Evaluation
print("\nModel Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Step 10: Test with custom URL
def predict_url(url):
    url = clean_url(url)
    url_vec = vectorizer.transform([url])
    prediction = model.predict(url_vec)[0]
    
    if prediction == 1:
        print("⚠️ Malicious URL")
    else:
        print("✅ Safe URL")

# Example test
predict_url("http://example-login-secure.com")