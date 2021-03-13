# Передача функции неопределенного количества аргументов (неименованные аргументы)
def printab(a, b, *args):
    print('positional argument a ', a)
    print('positional argument b ', b)
    print('additional arguments:')
    for arg in args:
        print(arg)


printab(10, 20, 30, 40, 50)