import re

# . ^ $ * + ? { } [ ] \ | ( ) — метасимволы
#
# [ ] — можно указать множество подходящих символов
#
# ^ - карет, обозначает либо начало строки, либо инвертирование группы символов. (например: "^[^0-9]" — не-цифра в начале строки).
#
# \d ~ [0-9] — цифры
#
# \D ~ [^0-9] - что угодно, но не цифры
#
# \s ~ [ \t\n\r\f\v] — пробельные символы (пробел, табуляция, перенос строки, перенос каретки, перенос страницы и вертикальная табуляция
#
# \S ~ [^ \t\n\r\f\v] - не пробельные символы
#
# \w ~ [a-zA-Z0-9_] — буквы + цифры + _
#
# \W ~ [^a-zA-Z0-9_] - не цифры и не буквы
# . - любой символ, кроме переноса строки, будет подходить под точку

pattern = r' english?'
string = 'Do ypu speak english?'
match = re.search(pattern, string)  # не содержит символ ?, т.к. он является метасимволом. Чтобы этого избежать ? надо экранировать
print(match)

pattern = r' english\?'
string = 'Do you speak english?'
match = re.search(pattern, string)  # символ ? был экранирован
print(match)

pattern = r'a[a-zA-Z]c'  # в шаблон входят все буквы алфавита
string = 'acc'
match_object = re.match(pattern, string)
print(match_object)

string = 'abc, acc, aac, adc'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

pattern = r'a[^a-zA-Z]c'  # ^ сигнализирует о том, что перечисленный диапазон символов НЕ подходит
string = 'abc, a.c, a-c, a\\c'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)