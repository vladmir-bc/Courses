l, m = map(int, input().split())


def combination(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return combination(n - 1, k) + combination(n - 1, k - 1)


print(combination(l, m))
