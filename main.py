import requests
import json

AUTH_END_POINT = 'http://127.0.0.1:8000/api-token-auth/'
ENDPOINT = 'http://127.0.0.1:8000/'
data = {
    'username': 'f18bb107',
    'password': 'Spotify420'
}
headers = {
    'Content-Type': 'application/json'
}

response = requests.post(AUTH_END_POINT, data=json.dumps(data), headers=headers)
token = response.json()['token']

print(token)

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'JWT ' + token,
}

data = {
    'title': 'random3',
    'description': 'Some new random content',
}
post_data = json.dumps(data)

re_response = requests.post(url=ENDPOINT, data=post_data, headers=headers)
print(re_response.text)