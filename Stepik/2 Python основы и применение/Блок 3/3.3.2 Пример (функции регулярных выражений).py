import re

# print(re.match)  # функция match проверяет, подходит ли данная строка под данный шаблон
# print(re.search)  #  функция search находит первое вхождение шаблона в строку
# print(re.findall)  # находит все подстроки строки, которые подходят под данный шаблон
# print(re.sub)  # заменяет все вхождения подстрок, которые подходят под шаблон чем-нибудь другим

# [] -- можно указать множество подходящих символов

pattern = r'abc'  # шаблон
string = 'babc'
match_object = re.match(pattern, string)  # проверяет, подходит ли данная строка под данный шаблон
print(match_object)  # None

match_object = re.search(pattern, string) # берет строку и находит ПЕРВУЮ подстроку, которая подходит под наш шаблон. Строка не обязательно должна начинаться также, как и шаблон, но шаблон должен присутствовать в строке
print(match_object)  # <re.Match object; span=(1, 4), match='abc'>

pattern = r'a[abc]c'  # вторым символом строки может являться как символ a, как символ b, так и символ c
string = 'aac'
match_object = re.match(pattern, string)  # проверяет, подходит ли данная строка под данный шаблон
print(match_object)  # <re.Match object; span=(0, 3), match='aac'>

string = 'abc, acc, aac'
all_inclusions = re.findall(pattern, string)  # позволяет найти все вхождения шаблона внутри текста
print(all_inclusions)  # ['abc', 'acc', 'aac']

fixed_typos = re.sub(pattern, 'abc',
                     string)  # позволяет найти и заменить все вхождения шаблона внутри текста на строку 'abc'
print(fixed_typos)  # abc, abc, abc
