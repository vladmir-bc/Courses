def f(x, y):
    try:
        return x / y
    except (TypeError, ZeroDivisionError) as e:
        print('Error')
        print(type(e))
        print(e)
        print(e.args)


f(5, 0)
print('_____________________________________________________________________________')
f(5, [])
