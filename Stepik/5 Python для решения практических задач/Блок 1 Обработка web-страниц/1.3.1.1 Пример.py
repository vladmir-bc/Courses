from urllib.request import urlopen


html = urlopen("https://ru.wikipedia.org/wiki/Python").read().decode('utf-8')
s = str(html)
pos = s.find("<a href=")
counter = 0
# while pos != -1:  # будем искать все вхождения
#     posquote = s.find('"', pos + 9)
#     href = s[pos + 9:posquote]  # строка начинается от первых " и заканчивается закрывающими "
#     counter += 1
#     print(counter, href)
#     s = s[posquote + 1:]
#     pos = s.find("<a href=")


while pos != -1:  # будем искать все вхождения
    posquote = s.find('"', pos + 9)
    href = s[pos + 9:posquote]  # строка начинается от первых " и заканчивается закрывающими "
    counter += 1
    print(counter, href)
    pos = s.find("<a href=", pos + 1)