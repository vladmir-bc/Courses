number = int(input())
mas_fib = [-1 for i in range(number + 1)]


def fib_TD(n):
    global mas_fib
    if mas_fib[n] == -1:
        if n <= 1:
            mas_fib[n] = n
        else:
            mas_fib[n] = fib_TD(n - 1) + fib_TD(n - 2)
    return mas_fib[n]


print(fib_TD(number))
