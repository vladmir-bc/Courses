import requests

r = requests.get('https://example.com')  # простой GET запрос
print(r.text)  # вывод ответа от сервера

url = 'https://example.com'
par = {'key1': 'value1', 'key2': 'value2'}
r = requests.get(url, params=par)  # Передача параметров в запрос
print(r.url)  # Сформированный url-адрес с учетом параметров GET запроса

url = 'http://httpbin.org/cookies'
cookies = {'cookies_are': 'working'}
r = requests.get(url, cookies=cookies)  # отправка сформированных cookies на сервер
print(r.text)

print(r.cookies['example_cookie_name'])  # использование cokies, полученных от сервера
