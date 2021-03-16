from math import log


def RecTimeKey(x):
    a, b, d = x[0], x[1], x[2]
    if d > log(a, b):
        return d, 1
    elif d == log(a, b):
        return d, 2
    else:
        return log(a, b), 1


A = []
print('Write "a b d", there T(n) = aT(n/b) + O(n^d)')
for _ in range(9):
    A.append(tuple(map(int, input().split())))
    assert len(A[-1]) == 3

for x in sorted(A, key=RecTimeKey):
    a, b, d = x[0], x[1], x[2]
    print('{}T(n/{}) + O(n^{})'.format(a, b, d))
