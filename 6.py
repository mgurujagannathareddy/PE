#Fine tuning

import requests
URL="http://localhost:11434/api/generate"
def generate(prompt):
    data = {
        "model":"llama3.2:1b",
        "prompt":prompt,
        "stream":False,
        "options":{
            "temperature": 0.7,
            "num_predict": 500
        }
    }
    response = requests.post(URL, json=data)
    response.raise_for_status()
    return response.json()["response"].strip()


prompts = {"prompt": "You are a sentimental classification model. Classify the follownig reviews into exactly one category. Positive, Negative, or Neutral. Return only the category. Reviews: 1. 'This product is amazing.', Consider some example reviews yourself and categorise them. Just for educational purpose"}
for ty, prompt in prompts.items():
    print(ty)
    print("=" * 60)
    print(generate(prompt))