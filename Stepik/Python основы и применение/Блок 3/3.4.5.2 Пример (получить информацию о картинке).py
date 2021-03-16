import requests
import sys

res = requests.get('https://docs.python.org/3/_static/py.png')
print(res.status_code)
print(res.headers['Content-Type'])

print(res.content)
# print(res.text)

with open('python.png', 'wb') as f:
    f.write(res.content)