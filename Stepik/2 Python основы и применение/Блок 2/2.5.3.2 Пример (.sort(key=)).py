# x = input().split()
# xs = (int(i) for i in x)
#
#
# def even(x):
#     '''Проверяет, является ли число четным'''
#     return x % 2 == 0


# evens = filter(even,
#                xs)  # конструктор класса filter возвращает filter-object.
# # filter-object является итератором, и внутри него реальзован метод next
# for i in evens:
#     print(i)

# or
x = [
    ('Guiod', 'van', 'Rossum'),
    ('Haskell', 'Curry'),
    ('John', 'Backus')
]  # список имен, где каждое имя описывается кортежем, который состоит из составляющих каждого имени


def length(name):
    '''Функция возвращает длину имени'''
    return len(' '.join(name))


name_lengths = [length(name) for name in x]
print(name_lengths)

x.sort(key=length)
print(x)