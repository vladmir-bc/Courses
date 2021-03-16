import requests
import sys

res = requests.get('https://docs.python.org/3/')
print(res.status_code)
print(res.headers['Content-Type'])

print(res.content)
print(res.text)