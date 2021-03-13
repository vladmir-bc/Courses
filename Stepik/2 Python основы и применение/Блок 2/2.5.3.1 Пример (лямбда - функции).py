x = input().split()
xs = (int(i) for i in x)

# def even(x):
#     '''Проверяет, является ли число четным'''
#     return x % 2 == 0

evens = list(filter(lambda x: x % 2 == 0, xs))
print(evens)
