from bs4 import BeautifulSoup
from urllib.request import urlopen


html = urlopen("https://ru.wikipedia.org/wiki/Python").read().decode('utf-8')
s = str(html)
soup = BeautifulSoup(s, "html.parser")
print(soup.find_all('a', href=True))
print(len(soup.find_all('a', href=True)))

for a in soup.find_all('a', href=True):
    print(a["href"])