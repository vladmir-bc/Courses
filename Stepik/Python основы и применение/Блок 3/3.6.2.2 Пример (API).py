import requests

api_url = "http://api.openweathermap.org/data/2.5/weather"

city = input('City? ')


params = {
    'q': city,
    'appid': '829c3c9c3e1090563696f0aaf5d257f1',
    'units': 'metric'
}

res = requests.get(api_url, params=params)
data = res.json()
template = 'Current temperature in {} is {} degrees Celsius'
print(template.format(city, data["main"]["temp"]))