A = map(int, input().split())
A = list(A)
A.sort()
n = len(A) - 1


def binary_search(mas, i):
    l = 0
    r = len(mas) - 1
    while l <= r:
        m = (l + r) // 2
        if mas[m] == i and m == i:
            return print(m, end=' ')
        elif mas[m] > i:
            r = m - 1
        else:
            l = m + 1

for i in range(len(A)):
    binary_search(A, i)