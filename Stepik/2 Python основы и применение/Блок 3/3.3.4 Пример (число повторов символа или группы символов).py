import re

pattern = r'ab*a'  # интересует любое число символа b, включая 0
string = 'aa, aba, abba'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)  # ['aa', 'aba', 'abba']

pattern = r'ab+a'  # интересует положительное число символа b (>0)
string = 'aa, aba, abba'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)  # ['aba', 'abba']

pattern = r'ab?a'  # интересует 0 или 1 вхождение символа b
string = 'aa, aba, abba'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)  # ['aa', 'aba']

pattern = r'ab{3}a'  # интересует 3 вхождения символа b
string = 'aa, aba, abba, abbba, abbbba'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)  # ['abbba']

pattern = r'ab{2,4}a'  # интересует от 2 до 4 вхождений
string = 'aa, aba, abba, abbba, abbbba'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)  # ['abba', 'abbba', 'abbbba']

pattern = r'a[ab]+a'  # положительное число вхождений символов a или b. + действует "жадно", т.к. ищет наибольшее число вхождений
string = 'abaaba'
matches = re.match(pattern, string)
print(matches)  # <re.Match object; span=(0, 6), match='abaaba'>
print(re.findall(pattern, string))  # ['abaaba']

'''Для того, чтобы поиск происходил не жадным способом, можно использовать "?" - т.е. 0 или 1 вхождение'''

pattern = r'a[ab]+?a' # + требует 1 или больше вхождений, ? требует 0 или 1 вхождение. Таким образом, комбинация +? дает требует ровно одно вхождение
string = 'abaaba'
print(re.match(pattern, string))  # <re.Match object; span=(0, 3), match='aba'>
print(re.findall(pattern, string))  # ['aba', 'aba']
