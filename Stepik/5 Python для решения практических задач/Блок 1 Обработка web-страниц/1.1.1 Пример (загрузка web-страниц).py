from urllib.request import urlopen

html = urlopen("https://ru.wikipedia.org/wiki/Python").read().decode('utf-8')
print(html.count("C++"))