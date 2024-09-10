import requests

data = {"text": "Bonjour le monde"}
response = requests.post('http://localhost:5000/detect-and-translate', json=data)
print(response.json())