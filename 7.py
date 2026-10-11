
# Prompt Optimization / Comparison

import requests

URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:1b"


def generate(prompt):
    data = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0,
            "num_predict": 100
        }
    }

    response = requests.post(URL, json=data, timeout=120)
    response.raise_for_status()
    return response.json()["response"].strip()


# Candidate prompts
prompts = {
    "A": (
        "Classify the sentiment of this review:\n"
        "{review}"
    ),
    "B": (
        "Classify this review as Positive, Negative, or Neutral. "
        "Return only one label.\n"
        "Review: {review}"
    ),
    "C": (
        "Classify the review as Positive if it expresses satisfaction, "
        "Negative if it expresses dissatisfaction, or Neutral if it "
        "expresses neither. Return exactly one label.\n"
        "Review: {review}"
    )
}


# Mobile product reviews with expected labels
reviews = [
    {
        "review": "The battery lasts all day and the camera is excellent.",
        "expected": "positive"
    },
    {
        "review": "The phone heats up and the battery drains quickly.",
        "expected": "negative"
    },
    {
        "review": "The phone comes with a 6.5-inch display.",
        "expected": "neutral"
    }
]


# Test each prompt against the same reviews
for ty, template in prompts.items():
    print(f"\nPrompt {ty}")
    print("=" * 60)

    correct = 0

    for item in reviews:
        review = item["review"]
        expected = item["expected"]

        # Replace the placeholder with the actual review
        prompt = template.format(review=review)

        answer = generate(prompt)
        normalized = answer.strip().lower().rstrip(".")

        print(f"\nReview: {review}")
        print(f"Expected: {expected}")
        print(f"Predicted: {answer}")

        # Simple exact-label evaluation
        # print("============>..........." + normalized)
        if normalized == expected:
            correct += 1

    accuracy = correct / len(reviews) * 100
    print(f"\nAccuracy: {correct}/{len(reviews)} = {accuracy:.1f}%")
