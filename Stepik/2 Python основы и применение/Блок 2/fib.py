def fib(x):
    if x == 1 or x == 0:
        return 1
    return fib(x - 1) + fib(x - 2)

if __name__ == '__main__':
    print(__name__)
    print(fib(31))
