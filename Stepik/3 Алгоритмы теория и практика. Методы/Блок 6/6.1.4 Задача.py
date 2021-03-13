n, *A = map(int, input().split())
k, *numb_k = map(int, input().split())


def binary_search(mas, k):
    l = 0
    r = len(mas) - 1
    while l <= r:
        m = (l + r) // 2
        if mas[m] == k:
            return m + 1
        elif mas[m] > k:
            r = m - 1
        else:
            l = m + 1
    return -1


for i in numb_k:
    print(binary_search(A, i), end=' ')
