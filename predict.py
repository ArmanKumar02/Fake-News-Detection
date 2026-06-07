import joblib

# Load saved model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

while True:
    news = input("\nEnter News (or type 'exit'): ")

    if news.lower() == "exit":
        print("Exiting...")
        break

    # Convert text into numerical form
    news_vector = vectorizer.transform([news])

    # Predict
    prediction = model.predict(news_vector)[0]

    # Get confidence
    confidence = max(model.predict_proba(news_vector)[0]) * 100

    print("\n======================")
    print("Prediction :", prediction)
    print(f"Confidence : {confidence:.2f}%")
    print("======================")