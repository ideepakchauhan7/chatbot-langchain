import requests
import json

url = "http://localhost:5000/chat"
payload = {
    "query": "What courses are available?",
    "chat_history": []
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, data=json.dumps(payload), headers=headers)
print(response.json())