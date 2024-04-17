import requests

response = requests.get('https://indeed.com/')
print(response.text)

