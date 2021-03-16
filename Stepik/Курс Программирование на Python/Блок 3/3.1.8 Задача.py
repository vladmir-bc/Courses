def foo(x):
    if x <= -2:
        f_x = 1 - (x + 2) ** 2
    elif -2 < x <= 2:
        f_x = -x / 2
    else:
        f_x = (x - 2)**2 + 1
    return f_x

print(foo(4.5))
