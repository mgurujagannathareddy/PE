import requests
from sklearn.metrics import accuracy_score

URL = "http://localhost:11434/api/generate"

prompts = {
    "A": "Classify this review:\n{review}",
    "B": "Classify as Positive, Negative, or Neutral. Return only one label:\n{review}",
    "C": (
        "Positive means satisfaction, Negative means dissatisfaction, "
        "Neutral means neither. Return only one label:\n{review}"
    )
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


results = {}

for name, template in prompts.items():
    y_true = []
    y_pred = []

    for review, expected in reviews:
        answer = generate(template.format(review=review))

        prediction = next(
            (label for label in ["positive", "negative", "neutral"]
             if label in answer.split()),
            "invalid"
        )

        print(expected)
        print("="*200)
        print(prediction)

        y_true.append(expected)
        y_pred.append(prediction)

    accuracy = accuracy_score(y_true, y_pred)
    results[name] = accuracy
    print(name, "Accuracy:", round(accuracy, 3))


best = max(results, key=results.get)

print("\nBest prompt:", best)
print("Best accuracy:", round(results[best], 3))
print(prompts[best])
