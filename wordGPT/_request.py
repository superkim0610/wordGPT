import requests
import env

env.loadEnv()
API_KEY = env.getEnv("API_KEY")

# prompt = "answer syntax(sparator=comma, suffix=;, none space)\neach 3 antonym word of \"orange\""
prompt = "answer syntax : word1,word2;\neach 3 syntonym words of \"orange\""

URL = "https://api.openai.com/v1/completions"
headers = {"Content-type": "application/json", "Authorization": "Bearer "+API_KEY}
data = {
  "model": "text-davinci-003",
  "prompt": prompt,
  "max_tokens": 100,
  "temperature": 0,
  "frequency_penalty":0,
  "presence_penalty":0,
  "top_p": 1,
}

response = requests.post(URL, headers=headers, json=data)
print(response.json()["choices"][0]["text"])