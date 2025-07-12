import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = os.getenv("OPENROUTER_API_KEY")

print("Loaded API key:", API_KEY)

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://your-app.com",  
    "X-Title": "My Chat App"                
}

def query(prompt):
    payload = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        print("RAW RESPONSE:", response.text)
        response.raise_for_status()

        try:
            data = response.json()
            return data["choices"][0]["message"]["content"]
        except ValueError:
            return f"⚠️ Got unexpected response: {response.text}"

    except Exception as e:
        return f"❌ Request failed: {e}"

# Test it
if __name__ == "__main__":
    print("Response:", query("What is the capital of France?"))
