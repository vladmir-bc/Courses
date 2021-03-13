from urllib.request import urlopen
from bs4 import BeautifulSoup

# html = urlopen("https://stepik.org/media/attachments/lesson/209723/5.html").read()
# s = str(html)
# soup = BeautifulSoup(s, "html.parser")
# sum_of_numbers = 0
# for tag in soup.find_all("td"):
#     sum_of_numbers += int(tag.text)
#
# print(sum_of_numbers)

html = urlopen("https://stepik.org/media/attachments/lesson/209723/5.html").read()
s = str(html)
soup = BeautifulSoup(s, "html5lib")
print(soup)
sum_of_numbers = 0
for tag in soup.find_all("td"):
    sum_of_numbers += int(tag.text)

print(sum_of_numbers)