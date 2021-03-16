number = int(input())


def fib_BU(n):
    mas_fib = [int(i) for i in range(number + 1)]
    if n == 0:
        return mas_fib[n]
    mas_fib[0], mas_fib[1] = 0, 1
    for j in range(2, n + 1):
        mas_fib[j] = mas_fib[j - 1] + mas_fib[j - 2]
    return mas_fib[n]


print(fib_BU(number))
