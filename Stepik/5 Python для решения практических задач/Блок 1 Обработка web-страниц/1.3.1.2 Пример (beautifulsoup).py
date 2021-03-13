from bs4 import BeautifulSoup
from urllib.request import urlopen


html = urlopen("https://ru.wikipedia.org/wiki/Python").read().decode('utf-8')
s = str(html)
pos = s.find("<a href=")
counter = 0

soup = BeautifulSoup(html, "html.parser")
# print(soup.find_all("a"))
# print(len(soup.find_all("a")))
# print(soup.select('a[href^=""]'))
# print(len(soup.select('a[href^=""]')))

for link in soup.find_all("a"):
    if link.has_attr('href'):
        print(link['href'])
        counter += 1
        print(counter, link['href'])