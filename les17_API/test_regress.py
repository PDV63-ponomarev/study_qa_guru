import requests
import json
from jsonschema import validate
from les17_API.shemas import post_users

url = "https://reqres.in/api/users"
payload = json.dumps({
  "name": "morpheus",
  "job": "leader"
})
headers = {
  'Content-Type': 'application/json',
  'x-api-key': 'reqres_291758bfc2fa49ae90f3e31b2d6cd46f'
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)



def test():
  response = requests.post(url, data=payload, headers=headers)
  body = response.json()
  assert response.status_code == 201
  with open('les17_API/post_users.json') as file:
    validate(body, schema=json.loads(file.read()))


def test_with_shemas():
  response = requests.post(url, data=payload, headers=headers)
  body = response.json()
  assert response.status_code == 201
  validate(body, schema=post_users)



def test_job_name_from_request_return_in_response():
  job = 'master'
  name = 'Bob'

  response = requests.post(url, data=json.dumps({
    "name": name,
    "job": job}),
    headers=headers
    )
  body = response.json()

  assert body['name'] == name
  assert body['job'] == job


def test_get_id():
  response = requests.get('https://reqres.in/api/users',
                          params={'page':2, 'per_page':4},
                          headers=headers,
                          verify=False)
  idx = [element['id'] for element in response.json()["data"]]
  set_idx = set(idx[1:])

  assert len(idx) > len(set_idx)
  assert len(idx) == len(set(idx))