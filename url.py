urls = [
    "https://www.google.com",
    "http://free-money.xyz",
    "https://secure-bank.com",
    "http://login-paypal-alert.com",
    "https://github.com",
    "http://win-prize-now.net",
    "https://amazon.in",
    "http://verify-account-security.com"
]

labels = [0, 1, 0, 1, 0, 1, 0, 1]

def extract_features(url):
    features = {}

    features["https"] = 1 if "https" in url else 0

    features["length"] = len(url)

    suspicious_words = ["login", "verify", "free", "win", "prize", "alert"]
    features["suspicious"] = 0
    for word in suspicious_words:
        if word in url:
            features["suspicious"] = 1

    return features

print("URL Analysis:\n")
for i in range(len(urls)):
    f = extract_features(urls[i])
    print("URL:", urls[i])
    print("Features:", f)
    print("Actual Label:", "Malicious" if labels[i] == 1 else "Safe")
    print("-" * 40)

def predict(url):
    f = extract_features(url)

    if f["https"] == 0 and f["suspicious"] == 1:
        return 1
    elif f["length"] > 25 and f["suspicious"] == 1:
        return 1
    else:
        return 0

print("\nPrediction Results:\n")

correct = 0

for i in range(len(urls)):
    prediction = predict(urls[i])

    print("URL:", urls[i])
    print("Predicted:", "Malicious" if prediction == 1 else "Safe")
    print("Actual   :", "Malicious" if labels[i] == 1 else "Safe")

    if prediction == labels[i]:
        correct += 1

    print("-" * 40)

accuracy = correct / len(urls)
print("Model Accuracy:", accuracy * 100, "%")
