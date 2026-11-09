import requests

URL = "http://localhost:11434/api/generate"

def generate(prompt):
    r = requests.post(URL, json={
        "model": "llama3.2:1b",
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0}
    }, timeout=300)

    r.raise_for_status()
    return r.json()["response"].strip()


try:
    n = int(input("Enter number of prompts: "))
    results = {}

    for i in range(n):
        prompt = input(f"\nEnter Prompt {i+1}: ")
        answer = generate(prompt)

        print("\nRESPONSE:")
        print(answer)

        print("\nRESPONSE EVALUATION")
        print("=" * 65)
        print("Give a score from 1 to 5 for each criterion.")

        relevance = int(input("Relevance (1-5): "))
        accuracy = int(input("Accuracy (1-5): "))
        clarity = int(input("Clarity (1-5): "))
        instruction = int(input("Instruction Following (1-5): "))

        total = relevance + accuracy + clarity + instruction

        print("\nTotal Score:", total, "/ 20")
        results[prompt] = total

    best = max(results, key=results.get)

    print("\nOPTIMAL PROMPT")
    print("=" * 65)
    print("Best Prompt:", best)
    print("Best Score:", results[best], "/ 20")

except requests.exceptions.ConnectionError:
    print("Error: Could not connect to Ollama. Make sure Ollama is running.")

except requests.exceptions.Timeout:
    print("Error: Model took too long to respond.")

except Exception as error:
    print("Error:", error)
