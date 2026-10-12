
import requests
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

URL = "http://localhost:11434/api/generate"

prompts = {
    "A": "Classify this review:\n{review}",
    "B": "Classify as Positive, Negative, or Neutral. Return only one label:\n{review}",
    "C": "Positive means satisfaction, Negative means dissatisfaction, Neutral means neither. Return only one label:\n{review}"
}

reviews = [
    ("Amazing phone and excellent camera", "positive"),
    ("Terrible battery life", "negative"),
    ("The phone has 128 GB storage", "neutral"),
    ("I love this phone", "positive"),
    ("Very poor quality", "negative"),
    ("The phone comes in black", "neutral")
]


def generate(prompt):
    response = requests.post(URL, json={
        "model": "llama3.2:1b",
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0}
    })
    response.raise_for_status()
    return response.json()["response"].strip().lower()


for name, template in prompts.items():
    y_true = []
    y_pred = []

    for review, expected in reviews:
        answer = generate(template.format(review=review))

        # Extract the first valid sentiment label
        prediction = next(
            (label for label in ["positive", "negative", "neutral"]
             if label in answer.split()),
            "invalid"
        )

        y_true.append(expected)
        y_pred.append(prediction.lower())

    print(f"\nPrompt {name}")
    print("=" * 35)
    print("Accuracy :", round(accuracy_score(y_true, y_pred), 3))
    print("Precision:", round(precision_score(
        y_true, y_pred, labels=["positive", "negative", "neutral"],
        average="macro", zero_division=0
    ), 3))
    print("Recall   :", round(recall_score(
        y_true, y_pred, labels=["positive", "negative", "neutral"],
        average="macro", zero_division=0
    ), 3))
    print("F1 Score :", round(f1_score(
        y_true, y_pred, labels=["positive", "negative", "neutral"],
        average="macro", zero_division=0
    ), 3))
