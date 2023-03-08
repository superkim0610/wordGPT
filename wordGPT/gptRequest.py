import requests
import env

def getRequest(prompt):
  API_KEY = env.getEnv("API_KEY")
  URL = "https://api.openai.com/v1/completions"
  headers = {"Content-type": "application/json", "Authorization": "Bearer " + API_KEY}
  data = {
    "model": "text-davinci-003",
    "prompt": prompt,
    "max_tokens": 100,
    "temperature": 0.7,
    "frequency_penalty": 0,
    "presence_penalty": 0,
    "top_p": 1,
  }

  response = requests.post(URL, headers=headers, json=data)
  return response.json()["choices"][0]["text"]

def getWords(word, number):
  prompt = f"syntonym words of \"{word}\"(separate by comma, {number} words)"
  syntonyms = getRequest(prompt).split(',')

  prompt = f"antonym words of \"{word}\"(separate by comma, {number} words)"
  antonyms = getRequest(prompt).split(',')

  prompt = f"recommended words that will help memorize related with \"{word}\"(separate by comma, {number} words)"
  recommendations = getRequest(prompt).split(',')

  return {
    "syntonyms": syntonyms,
    "antonyms": antonyms,
    "recommendations": recommendations
  }

def getSentences(word, number):
  prompt = f"recommended words that will help memorize related with \"{word}\"(separate by comma, {answer_number} words\nsupply, furnish, render\nreccomendation reason)"
  sentences = getSentences(prompt).split(',')

  return sentences





