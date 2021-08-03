import json
import requests
import os

new = 'http://127.0.0.1:8000/get_api/'
AUTH_ENDPOINT = "http://127.0.0.1:8000/api/token/"
REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"

# image_path = os.path.join(os.getcwd(), "logo.jpg")

headers = {
    "Content-Type": "application/json",
}

data = {
    'username': 'f18bb107',
    'password': 'Spotify420',
}

r = requests.post(new, data=json.dumps(data), headers=headers)
token = r.json()
print(token)

"""----------------------------------------------------------------------------------------------------"""

# headers2 = {
#     "Content-Type": "application/json",
#     "Authorization": "JWT " + token
# }
#
# data2 = {
#     'title': 'ssfss',
#     'description': 'this new content post'
# }
#
#
# post_data = 'http://127.0.0.1:8000/api/upde/'
#
# json_data = json.dumps(data2)
# posted_response = requests.post(post_data + str(5) + "/", data=data, headers=headers2)
# print(posted_response)



# AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/register/"
# REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"
# ENDPOINT = "http://127.0.0.1:8000/api/status/"
#
# # image_path = os.path.join(os.getcwd(), "logo.jpg")
#
# headers = {
#     "Content-Type": "application/json",
#     "Authorization": "JWT " + token,
# }
#
# r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
# token = r.json()
# print(token)
#
# refresh_data = {
#     'token': token
# }
#
# new_response = requests.post(REFRESH_ENDPOINT, data=json.dumps(refresh_data), headers=headers)
# new_token = new_response.json()
#
# print(new_token)

# headers = {
#     "Content-Type": "application/json",
#     "Authorization": "JWT " + token,
# }

# with open(image_path, 'rb') as image:
#     file_data = {
#         'image': image
#     }

# data = {
#     "content": "Updated description"
# }
# json_data = json.dumps(data)
# posted_response = requests.put(ENDPOINT + str(37) + "/", data=data, headers=headers)
# print(posted_response.text)


# headers = {
#     #"Content-Type": "application/json",
#     "Authorization": "JWT " + token,
# }

# data = {
#     "content": "Updated description"
# }
# json_data = json.dumps(data)
# posted_response = requests.put(ENDPOINT + str(37) + "/", data=data, headers=headers)
# print(posted_response.text)


# get_endpoint =  ENDPOINT + str(12)
# r = requests.get(get_endpoint)
# print(r.text)


# r2 = requests.get(ENDPOINT)
# print(r2.status_code)


# post_headers = {
#     'content-type': 'application/json'
# }

# post_response = requests.post(ENDPOINT, data=post_data, headers=post_headers)
# print(post_response.text)


# def do_img(method='get', data={}, is_json=True, img_path=None):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     if img_path is not None:
#         with open(image_path, 'rb') as image:
#             file_data = {
#                 'image': image
#             }
#             r = requests.request(method, ENDPOINT, data=data, files=file_data, headers=headers)
#     else:
#         r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r


# do_img(
#     method='post',
#     data={'id': 23, 'user': 1, "content": "Some new content"},
#     is_json=True
#     )


# def do(method='get', data={}, is_json=True):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r


# do(data={'id': 500})

# do(method='delete', data={'id': 13})

# do(method='put', data={'id': 13, "content": "some cool new content", 'user': 1})

# do(method='post', data={"content": "some cool new content", 'user': 1})

# create
# retrieve / list
# update
# delete
