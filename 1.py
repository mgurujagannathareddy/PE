import ollama
client = ollama.Client(host="http://localhost:11434")

response = client.chat(
    model="llama3.2:1b",
    messages=[
        {
            "role": "user",
            "content": "Explain Ai"
        }
    ]
)

print(response.message.content)