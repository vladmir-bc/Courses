d = {}


def update_dictionary(d, key, value):
    if key not in d:
        if key * 2 not in d:
            d[key * 2] = [value]
        else:
            d[key * 2] += [value]
    else:
        d[key] += [value]





print(update_dictionary(d, 1, -1))
print(d)
print(update_dictionary(d, 2, -2))
print(d)
print(update_dictionary(d, 1, -3))
print(d)
print(update_dictionary(d, 10, 8))
print(d)