mass = [7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3, 8, 1]
# mass = [10000,1,2,3,4,5,6,7,8,9,10,-999]

def lis_bottom_up(mas):
    D = [0 for x in range(len(mas))]
    for i in range(len(mas)):
        D[i] = 1
        for j in range(i):
            if mas[j] < mas[i] and D[j] + 1 > D[i]:
                D[i] = D[j] + 1
    ans = (0, 0)
    for i in range(len(mas)):
        if ans[0] < D[i]:
            ans = (D[i], i)
    L = [mas[ans[1]]]
    k = 0
    for i in range(1, len(D)):
        if D[i] > D[k]:
            k = i
    pos = ans[1]
    print(ans)
    for elem in reversed(range(pos)):
        if D[elem] == D[pos] - 1 and mas[elem] < mas[pos]:
            L.append(mas[elem])
            pos = elem
    L.reverse()

    return L


print(lis_bottom_up(mass))
