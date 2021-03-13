from urllib.request import urlopen

html = urlopen("https://ru.wikipedia.org/wiki/Python").read().decode('utf-8')
s = str(html)
ans =[]
state = 0 # 0 означает, что мы находимся вне тега, 1 - что находимся в теге
for c in s:
    if c == '<':
        state = 1  # мы находимся внутри  тега
    elif c == '>':
        state = 0  # мы находимся вне тега
    elif state == 0:
        ans.append(c)
s = ''.join(ans)
print(s.count("C++"))