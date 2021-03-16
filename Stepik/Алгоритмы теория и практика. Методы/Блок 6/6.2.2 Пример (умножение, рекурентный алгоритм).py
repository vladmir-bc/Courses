x, y = int(input()), int(input())
x = bin(x)
y = bin(y)


def multiply(x, y):
    if y[-1] == '0':
        return 0
    z = multiply(x, y[:-1])
    if y[-1] == 0:
        return bin(2 * z)
    else:
        return bin(x + 2 * z)


print(multiply(x, y))