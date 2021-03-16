def find_min_func(a, b):
    if a <= b:
        return a
    else:
        return b


print(find_min_func(find_min_func(1, 5), 20))
