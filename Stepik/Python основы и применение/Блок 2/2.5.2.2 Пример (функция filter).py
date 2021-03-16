x = input().split()
xs = (int(i) for i in x)


def even(x):
    '''Проверяет, является ли число четным'''
    return x % 2 == 0


# evens = filter(even,
#                xs)  # конструктор класса filter возвращает filter-object.
# # filter-object является итератором, и внутри него реальзован метод next
# for i in evens:
#     print(i)

# or

evens = list(filter(even, xs))
print(evens)
