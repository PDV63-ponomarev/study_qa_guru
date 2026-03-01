import requests
import json
from jsonschema import validate
from les17_API.HW.shemas_hw import get_user, post_user, put_users, new_shemas


url = 'https://reqres.in/api/users'
headers = {
  'Content-Type': 'application/json',
  'x-api-key': 'reqres_291758bfc2fa49ae90f3e31b2d6cd46f'
}

def test_get_user_with_id_10():
    response = requests.get(url,
                          params={'id':10},
                          headers=headers,
                          )
    id_user = response.json()['data']['id']
    assert id_user == 10
    return response

def test_post_new_user():
    response = requests.post(url, data=json.dumps({
        "name": 'Dima',
        "job": 'QA-Auto'}),
         headers=headers
         )



def test_put_page_with_new_data():
    url = "https://reqres.in/api/users/2"
    headers = {
        'x-api-key': 'reqres_291758bfc2fa49ae90f3e31b2d6cd46f'
    }

    response = requests.put(url, headers=headers)
    id_user_old = response.json()['updatedAt']
    response = requests.put(url, headers=headers)
    id_user_new = response.json()['updatedAt']

    assert not id_user_old == id_user_new

def test_delete_user_get_code():
    url = "https://reqres.in/api/users/2"
    headers = {
        'x-api-key': 'reqres_291758bfc2fa49ae90f3e31b2d6cd46f'
    }
    response = requests.delete(url, headers=headers)

    assert response.status_code == 204


def test_positive_get_user_for_id():
    response = requests.get(url,
                            params={'id': 10},
                            headers=headers,
                            )
    assert response.status_code == 200

def test_negative_get_user_for_id():
    response = requests.get(url,
                            params={'id': 13},
                            headers=headers,
                            )
    assert response.status_code == 404


def test_with_code_200():
    response = requests.get(url, headers=headers)
    assert response.status_code == 200

def test_with_code_201():
    response = requests.post(url, data=json.dumps({
        "name": 'Dima',
        "job": 'QA-Auto'}),
                             headers=headers
                             )
    assert response.status_code == 201

def test_with_code_204():
    url = "https://reqres.in/api/users/2"
    headers = {
        'x-api-key': 'reqres_291758bfc2fa49ae90f3e31b2d6cd46f'
    }
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204


def test_with_code_404():
    headers = {
        'x-api-key': 'reqres_291758bfc2fa49ae90f3e31b2d6cd46f'
    }
    response = requests.post('https://reqres.in',data=None, headers=headers)
    assert response.status_code == 404


def test_with_code_400():
    response = requests.post('https://reqres.in', headers=headers)
    assert response.status_code == 400


def test_get_with_shemas():
    response = requests.get(url,
                            params={'id': 10},
                            headers=headers,
                            )
    body = response.json()
    validate(body, schema=get_user)

def test_post_with_shemas():
    response = requests.post(url, data=json.dumps({
        "name": 'Dima',
        "job": 'QA-Auto'}),
                             headers=headers)
    body = response.json()
    validate(body, schema=post_user)

def test_put_with_shemas():
    url = "https://reqres.in/api/users/2"
    headers = {
        'x-api-key': 'reqres_291758bfc2fa49ae90f3e31b2d6cd46f'
    }
    body = requests.put(url, headers=headers).json()
    validate(body, schema=put_users)


def test_post_with_new_shemas():
    payload = json.dumps({
        "name": "Dima",
        "job": "QU-Auto2"
    })
    headers = {
        'x-api-key': 'reqres_291758bfc2fa49ae90f3e31b2d6cd46f'
    }
    response = requests.post(url,
                            params=payload,
                            headers=headers,
                            )
    assert response.status_code == 201
    body = response.json()
    validate(body, schema=new_shemas)


def test_get_user_with_body():
    response = requests.get(url, headers=headers)
    assert not response.text == None


def test_delete_user_with_no_body():
    url = "https://reqres.in/api/users/2"
    headers = {
        'x-api-key': 'reqres_291758bfc2fa49ae90f3e31b2d6cd46f'
    }
    response = requests.delete(url, headers=headers)
    assert response.text == ''


def test_get_users_always_6():
    response = requests.get(url, headers=headers)
    lens = 0
    for element in response.json()["data"]:
        if element['id']:
            lens += 1
    assert lens == 6