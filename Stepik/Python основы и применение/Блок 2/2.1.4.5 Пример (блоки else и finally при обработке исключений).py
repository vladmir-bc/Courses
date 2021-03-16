def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('division by zero')
    else:
        print('result is ', result)
    finally:
        print('finally')

divide(2, 1)
print('_____________________________________________________________________________')
divide(2, 0)
print('_____________________________________________________________________________')
divide(2, [])