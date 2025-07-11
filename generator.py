import requests

url = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = "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"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://your-app.com",  # Optional
    "X-Title": "My Chat App"                # Optional
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
