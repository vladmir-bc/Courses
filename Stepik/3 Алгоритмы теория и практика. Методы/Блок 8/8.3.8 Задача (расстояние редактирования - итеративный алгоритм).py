s1 = list(input())
s2 = list(input())


def is_equal(l, m):
    if s1[l] == s2[m]:
        return 0
    else:
        return 1


def edit_dist_td(n, m):
    D = [[-9999 for k in range(m + 1)] for l in range(n + 1)]
    for i in range(n + 1):
        D[i][0] = i
    for j in range(m + 1):
        D[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            c = is_equal(i - 1, j - 1)
            D[i][j] = min(D[i - 1][j] + 1, D[i][j - 1] + 1, D[i - 1][j - 1] + c)
    return D[n][m]


i = len(s1)
j = len(s2)
print(edit_dist_td(i, j))
