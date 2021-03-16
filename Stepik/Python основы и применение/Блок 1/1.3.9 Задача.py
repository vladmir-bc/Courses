def closest_mod_5(condition):
    while condition % 5 != 0:
        condition += 1
    return condition


print(closest_mod_5(7))