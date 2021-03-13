from urllib.request import urlopen
import requests

# 1 вариант решения
html = urlopen("https://stepik.org/media/attachments/lesson/209717/1.html").read().decode('utf-8')
print(max(html.count("C++"), html.count("Python")))

# 2 вариант решения
html2 = requests.get("https://stepik.org/media/attachments/lesson/209717/1.html").text
print(max(html2.count("C++"), html2.count("Python")))

# 3 вариант решения
html3 = requests.get("https://stepik.org/media/attachments/lesson/209717/1.html").content.decode('utf-8')
print(max(html3.count("C++"), html3.count("Python")))
