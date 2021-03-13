s = 'The man in black fled across the desert, and the gunslinger followed'
print(s.lower())  # преобразует каждый символ строки в нижний регистр
print(s.upper())  # преобразует каждый символ строки в верхний регистр
print(s.count('the'))  # считает количество вхождений в строку указанного фрагмента
print(s.lower().count('the'))  # перед подсчетом преобразует символы строки в нижний регистр

s = '1,2,3,4'
print(s)
print(s.replace(',', ', ', 2))  # 2 раза заменяет ',' на ', '

s = '1 2 3 4'
print(s.split(' '))  # разделяет строку по пробелу
# print(s.split.__doc__)


s = '_*__1, 2, 3, 4__*_'
print(repr(s.rstrip('*_')))
print(repr(s.lstrip('*_')))
print(repr(s.strip('*_')))

numbers = map(str, [1, 2, 3, 4, 5])
print(repr(' '.join(numbers)))
