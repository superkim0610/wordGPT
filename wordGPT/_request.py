import requests
import env

env.loadEnv()
API_KEY = env.getEnv("API_KEY")

URL = "https://api.openai.com/v1/completions"
headers = {'Content-type': 'application/json', "Authorization": "Bearer "+API_KEY}
data = {
  "model": "text-davinci-003",
  "prompt": "Say this is a test",
  "max_tokens": 7,
  "temperature": 0,
  "top_p": 1,
}

response = requests.post(URL, headers=headers, json=data)
print(response.json()["choices"][0]["text"])