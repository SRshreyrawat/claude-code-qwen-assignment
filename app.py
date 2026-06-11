import requests

url = "http://localhost:11434/api/generate"

prompt = input("Enter your question:\n")

payload = {
    "model": "qwen3:4b",
    "prompt": prompt,
    "stream": False
}

print("Sending request...")

response = requests.post(
    url,
    json=payload,
    timeout=300
)

print("Status Code:", response.status_code)

result = response.json()

print("\nModel Response:\n")
print(result["response"])