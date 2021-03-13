from urllib.request import urlopen
import re

html = str(urlopen("https://stepik.org/media/attachments/lesson/209719/2.html").read().decode('utf-8'))

pattern = r"<code>(.+?)</code>"
strings = re.findall(pattern, html)
dictionary = {}
max_repeats = [0, 0, 0]
repeats = [0, 0, 0]

for element in strings:
    if strings.count(element) >= max_repeats[-1]:
        max_repeats[0], max_repeats[1], max_repeats[2] = max_repeats[1], max_repeats[2], strings.count(element)
        repeats[0], repeats[1], repeats[2] = repeats[1], repeats[2], element
print(' '.join(sorted(repeats)))