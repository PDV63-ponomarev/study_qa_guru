import requests
import json

url = "https://reqres.in/api/users?page=2"

payload = {"name": "morpheus", "job": "leader"}

headers = {
  'Content-Type': 'application/json',
  'x-api-key': 'reqres_291758bfc2fa49ae90f3e31b2d6cd46f'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


