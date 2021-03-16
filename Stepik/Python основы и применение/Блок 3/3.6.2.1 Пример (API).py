import requests

api_url = "http://api.openweathermap.org/data/2.5/weather"


params = {
    'q': 'Saint Petersburg',
    'appid': '829c3c9c3e1090563696f0aaf5d257f1'
}

res = requests.get(api_url, params=params)
print(res.status_code)
print(res.headers["Content-Type"])
print(res.json())  # returns json.loads(res.text)
data = res.json()
print(data["main"]["temp"])