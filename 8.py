import requests
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

URL = "http://localhost:11434/api/generate"

def generate(prompt):
    r = requests.post(URL, json={
        "model": "llama3.2:1b",
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0}
    }, timeout=300)

    r.raise_for_status()
    return r.json()["response"].strip().lower()


try:
    n = int(input("Number of prompts: "))
    prompts = [input(f"Prompt {i+1}: ") for i in range(n)]

    m = int(input("\nNumber of test inputs: "))
    data = []

    for i in range(m):
        text = input("Enter text: ")
        actual = input("Enter correct category: ").lower()
        data.append((text, actual))

    scores = []

    for i, prompt in enumerate(prompts):
        actual, predicted = [], []

        for text, label in data:
            answer = generate(prompt + "\n" + text)

            prediction = next(
                (x for x in ["positive", "negative", "neutral"]
                 if x in answer.split()), "invalid"
            )

            actual.append(label)
            predicted.append(prediction)

        a = accuracy_score(actual, predicted)
        p = precision_score(actual, predicted, average="macro", zero_division=0)
        r = recall_score(actual, predicted, average="macro", zero_division=0)
        f = f1_score(actual, predicted, average="macro", zero_division=0)

        scores.append(f)

        print(f"\nPrompt {i+1}")
        print("=" * 40)
        print("Accuracy:", round(a, 2))
        print("Precision:", round(p, 2))
        print("Recall:", round(r, 2))
        print("F1-score:", round(f, 2))

    best = scores.index(max(scores))

    print("\nBEST PROMPT")
    print("=" * 40)
    print(prompts[best])
    print("Best F1-score:", round(scores[best], 2))

except requests.exceptions.ConnectionError:
    print("Error: Could not connect to Ollama. Make sure Ollama is running.")

except requests.exceptions.Timeout:
    print("Error: Model took too long to respond.")

except Exception as error:
    print("Error:", error)
