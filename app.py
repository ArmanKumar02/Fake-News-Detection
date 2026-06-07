from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    confidence = None

    if request.method == "POST":
        news = request.form["news"]

        news_vector = vectorizer.transform([news])

        prediction = model.predict(news_vector)[0]

        confidence = max(model.predict_proba(news_vector)[0]) * 100

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence
    )

if __name__ == "__main__":
    app.run(debug=True)