import requests

URL = "http://localhost:11434/api/generate"

def generate(prompt):
    response = requests.post(URL, json={
        "model": "llama3.2:1b",
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0}
    })
    response.raise_for_status()
    return response.json()["response"].strip()


prompt = """
Explain why people from different backgrounds can be equally capable
of becoming successful scientists. Avoid stereotypes and base your
explanation on individual skills, opportunities, and effort.
"""
try:
    print(generate(prompt))

except requests.exceptions.ConnectionError:
    print("\nError: Could not connect to ollama.")
    print("Make sure ollama is running.")

except requests.exceptions.Timeout:
    print("\nError: Model took too laong to respond.")

except requests.exceptions.HTTPError as error:
    print("\nError: Ollama returned an HTTP error.")
    print(error)

except Exception as error:
    print(error)


    