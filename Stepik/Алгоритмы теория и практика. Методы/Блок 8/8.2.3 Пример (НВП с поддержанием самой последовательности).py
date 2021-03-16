mass = [7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3, 8, 1]


def lis_bottom_up(mas):
    D, prev = [0 for x in range(len(mas))], [0 for x in range(len(mas))]
    for i in range(len(mas)):
        prev[i] = -1
        D[i] = 1
        for j in range(i):
            if mas[j] < mas[i] and D[j] + 1 > D[i]:
                D[i], prev[i] = D[j] + 1, j
    ans = (0, 0)
    for i in range(len(mas)):
        if ans[0] < D[i]:
            ans = (D[i], i)
    L = [int(i) for i in range(ans[0])]
    k = 0
    for i in range(1, len(D)):
        if D[i] > D[k]:
            k = i
    j = ans[0] - 1
    while k >= 0:
        L[j] = k
        j -= 1
        k = prev[k]
    for el in L:
        print(mas[el], end=' ')
    print()
    return ans[0]


print(lis_bottom_up(mass))
