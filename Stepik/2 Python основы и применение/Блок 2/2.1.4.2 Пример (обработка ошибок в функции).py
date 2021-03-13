def f(x, y):
    try:
        return x / y
    except TypeError:
        print('Type error')


f(5, [])
try:
    print(f(5, 0))
except ZeroDivisionError:
    print('Division by zero')