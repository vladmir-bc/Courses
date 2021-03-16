def my_range(start, stop, step=1):
    array = []
    if step > 0:
        x = start
        while x < stop:
            array += [x]
            x += step
    if step < 0:
        x = start
        while x > stop:
            array += [x]
            x += step
    return array


print(my_range(15, 2, -3))
