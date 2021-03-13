from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://stepik.org/media/attachments/lesson/209723/4.html").read().decode('utf-8')
s = str(html)
# print(html)
soup = BeautifulSoup(s, "html.parser")
sum_of_numbers = 0
for tag in soup.find_all("td"):
    sum_of_numbers += int(tag.text)

print(sum_of_numbers)