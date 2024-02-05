import requests
import json

params = {
    "city": "北京",
    "key": "xnkd73pN8HHa61J7IWoKLlR0Yk"
}
url = "https://qqlykm.cn/api/weather/get"
WeatherAPIKey = requests.get(url, params=params)
# WeatherData = json.loads(WeatherAPIKey.text)
print(repr(WeatherAPIKey))
