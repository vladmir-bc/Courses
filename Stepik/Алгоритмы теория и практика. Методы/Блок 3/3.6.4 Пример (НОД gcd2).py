import random


def test(gcd, n_iter=100):
    for i in range(n_iter):
        c = random.randint(0, 1024)
        a = c * random.randint(0, 128)
        b = c * random.randint(0, 128)
        assert gcd(a, a) == gcd(a, 0) == a
        assert gcd(b, b) == gcd(b, 0) == b
        assert gcd(a, 1) == gcd(b, 1) == 1
        d = gcd(a, b)
        assert a % d == b % d == 0

def gcd2(a, b):
    assert a >= 0 and b >= 0
    while a and b:
        if a >= b:
            a %= b  # a заменяем на остаток от деления на b
        else:
            b %= a  # иначе заменим b на остаток от деления на a
    return max(a, b)

test(gcd2)
print(gcd2(1000000000000000000000000000000000000000, 100000000000000000000000000000000000))