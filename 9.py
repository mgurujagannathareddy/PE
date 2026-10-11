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

print(generate(prompt))