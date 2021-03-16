def foo(a, b):
    try:
        a / b
        assert 1 == 2
    except ZeroDivisionError:
        print('ZeroDivisionError')
    except ArithmeticError:
        print('ArithmeticError')
    except AssertionError:
        print('AssertionError')


try:
    foo(10**1000000, 1)
except ZeroDivisionError:
    print('ZeroDivisionError')
except ArithmeticError:
    print("ArithmeticError")
except AssertionError:
    print('AssertionError')
