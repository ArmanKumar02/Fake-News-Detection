# 📰 Fake News Detection System

A Machine Learning-based web application that classifies news articles as **REAL** or **FAKE** using Natural Language Processing (NLP) techniques. The application is built with **Python**, **Flask**, and **Scikit-Learn**, and is deployed online for real-time predictions.

---

## 🚀 Live Demo

🔗 https://fake-news-detection-xq4t.onrender.com

---

## 📌 Project Overview

Fake news has become a major challenge in the digital era. This project uses Machine Learning and NLP techniques to analyze news content and predict whether it is real or fake.

The model is trained on a large dataset containing **44,898 news articles** and achieves **98.64% accuracy** on the test dataset.

---

## ✨ Features

- ✅ Detects whether a news article is REAL or FAKE
- ✅ Displays prediction confidence score
- ✅ User-friendly web interface
- ✅ Machine Learning-based classification
- ✅ TF-IDF text vectorization
- ✅ Logistic Regression classifier
- ✅ Real-time predictions
- ✅ Cloud deployment using Render

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Machine Learning & Data Science
- Scikit-Learn
- Pandas
- NumPy
- Joblib

### Web Development
- Flask
- HTML
- CSS

### Tools & Platforms
- Git
- GitHub
- Render

---

## 🤖 Machine Learning Details

| Feature                  | Value                |
| Dataset Size             | 44,898 News Articles |
| Vectorization Technique  | TF-IDF               |
| Classification Algorithm | Logistic Regression  |
| Accuracy                 | 98.64%               |
| Model Storage            | model.pkl            |
| Vectorizer Storage       | vectorizer.pkl       |

---

## 📂 Project Structure

```text
Fake-News-Detection/
│
├── app.py                 # Flask web application
├── train_model.py         # Model training script
├── predict.py             # Command-line prediction script
├── model.pkl              # Trained ML model
├── vectorizer.pkl         # TF-IDF vectorizer
├── requirements.txt       # Project dependencies
│
├── templates/
│   └── index.html         # Frontend page
│
├── static/
│   └── style.css          # Styling
│
├── screenshots/
│   ├── home_page.png
│   ├── real_prediction.png
│   └── fake_prediction.png
│
└── README.md
```

---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/ArmanKumar02/Fake-News-Detection.git
```

### 2️⃣ Navigate to the Project Directory

```bash
cd Fake-News-Detection
```

### 3️⃣ Create Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate virtual environment:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the Flask server:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 🧠 Model Training

If you want to retrain the model using your dataset:

```bash
python train_model.py
```

This will generate:

```text
model.pkl
vectorizer.pkl
```

---

## 🔮 Future Enhancements

- Deep Learning Models (LSTM, BERT)
- Live News API Integration
- Multi-language News Detection
- News Source Verification
- User Authentication System
- Improved UI/UX Design
- Mobile Responsive Interface

---

## 📈 Learning Outcomes

Through this project, I gained practical experience in:

- Machine Learning
- Natural Language Processing (NLP)
- Data Preprocessing
- Model Evaluation
- Flask Web Development
- Git & GitHub
- Cloud Deployment
- End-to-End ML Project Development

---

## 👨‍💻 Author

### Arman Kumar

- GitHub: https://github.com/ArmanKumar02
- LinkedIn: https://www.linkedin.com/in/arman-kumar-895189326
            
---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

## 📜 License

This project is developed for educational and portfolio purposes.