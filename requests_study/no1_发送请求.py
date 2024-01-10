import requests

baidu_page = requests.get('https://www.baidu.com')
print(dir(baidu_page))
print(baidu_page.request)
print(baidu_page.text)
test_page = requests.get('https://httpbin.org/#/Response_formats/get_json')
# print(test_page.json())
print(test_page.text)
print(test_page.status_code)




base_url = "http://httpbin.org"

# 发送get请求
r = requests.get(base_url + "/get")
print(r.status_code)

# 发送post请求
r = requests.post(base_url + '/post')
print(r.status_code)

# 发送put请求
r = requests.put(base_url + "/put")
print(r.status_code)

# 发送delete请求
r = requests.delete(base_url + "/delete")
print(r.status_code)
