# Передача функции неопределенного количества аргументов (именованные аргументы)
def printab(a, b, **kwargs): # Учесть, что в словаре нет порядка
    print('positional argument a ', a)
    print('positional argument b ', b)
    print('additional arguments:')
    for key in kwargs:
        print(key, kwargs[key])


printab(10, c=30, d=40, jimmi=50, b=20)