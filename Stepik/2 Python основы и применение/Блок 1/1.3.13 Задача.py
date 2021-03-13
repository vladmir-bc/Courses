def s(a, *vs, b=10):
    res = a + b
    for v in vs:
        res += v
    return res


print(s(b=31))
