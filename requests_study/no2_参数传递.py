import requests

url = "http://httpbin.org"

param_data = {
    'key1': 123
}
r_get = requests.get(url + '/get', params=param_data)
r_post = requests.post(url + '/post', data=param_data)
print(r_get.url)
# http://httpbin.org/get?key1=123

print(r_post.url)
# http://httpbin.org/post
