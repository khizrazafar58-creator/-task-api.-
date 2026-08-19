# Spam Message Classifier (Machine Learning)

A beginner-friendly ML project that classifies text messages as **spam** or **ham** (not spam) using Natural Language Processing (NLP) and a Naive Bayes classifier — built with Python and scikit-learn.

## What it does

Given a text message, the model predicts whether it's spam (unwanted/promotional/scam content) or a genuine message, along with a confidence score.

## How it works

1. **Data loading** — Reads labeled messages from `spam_data.csv`
2. **Text preprocessing** — Lowercases and cleans the text
3. **Feature extraction** — Converts text into numerical features using **TF-IDF** (Term Frequency–Inverse Document Frequency)
4. **Model training** — Trains a **Multinomial Naive Bayes** classifier, a standard algorithm for text classification
5. **Evaluation** — Reports accuracy, precision, recall, and a confusion matrix
6. **Prediction** — Tests the trained model on new, unseen messages

## Tech stack

- Python 3
- pandas — data handling
- scikit-learn — TF-IDF vectorization, Naive Bayes model, evaluation metrics

## How to run

```bash
pip install pandas scikit-learn
python spam_classifier.py
```

## Sample output

```
Model Accuracy: 80.00%

--- Testing on new messages ---
[SPAM] (58.2% confidence) -> Congratulations! Claim your free prize now by clicking this link.
[HAM ] (66.3% confidence) -> Hey, are we still on for coffee tomorrow morning?
```

## Dataset

This repo includes a small 40-message sample dataset (`spam_data.csv`) for demonstration purposes. For a more robust and production-realistic model, this project can be retrained on the public **SMS Spam Collection Dataset** (available on Kaggle and the UCI Machine Learning Repository), which contains 5,000+ labeled real-world messages.

## Possible next steps / improvements

- Train on the full SMS Spam Collection dataset for better accuracy
- Try other models (Logistic Regression, SVM) and compare performance
- Add cross-validation instead of a single train/test split
- Build a simple web interface (Flask/Streamlit) to test messages interactively
- Explore explainability: which words most influence the spam prediction?

## Author

Khizra Zafar — Bachelor's student, University of Engineering and Technology (UET), Lahore
