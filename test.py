import requests

# Define the URL and the request data
url = "http://localhost:5000/chat"
data = {
    "message": "Tell me about Course 1"
}

# Send the POST request
response = requests.post(url, json=data)

# Print the response
print(response.json())
