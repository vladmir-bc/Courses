print('abc' in 'abcba')  # True
print('abce' in 'abcba')  # False

print('cabcd'.find('abc'))  # Индекс первого вхождения или -1
# print(str.find.__doc__)  # Описание метода find

print('cabcd'.index('abc'))  # индекс первого вхождения или ValueError

s = 'The man in black fled across the desert, and the gunslinger followed'
print(s.startswith('The man in black'))  # Проверяет, начинается ли строка с заданного аргумента: True
# print(s.startswith.__doc__)  # Описание метода startwith

s = 'image.png'
print(s.endswith('.png'))

s = 'abacaba'
print(s.count('aba'))  # Считает количество непересекающихся вхождений в строку: 2

print(s.find('aba'))  # возвращает индекс вхождения строки слева: 0
print(s.rfind('aba'))  # возвращает индекс вхождения строки справа: 4
