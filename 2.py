import requests
URL="http://localhost:11434/api/generate"
def generate(prompt):
    data = {
        "model":"llama3.2:1b",
        "prompt":prompt,
        "stream":False,
        "options":{
            "temperature":0.7,
            "num_predict":500
        }
    }
    response = requests.post(URL,json=data)
    response.raise_for_status()
    return response.json()["response"].strip()
answer = generate("is 25 even, say yes or no")
print(answer)