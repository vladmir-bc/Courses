s1 = list(input())
s2 = list(input())


def is_equal(l, m):
    if s1[l] == s2[m]:
        return 0
    else:
        return 1


def edit_dist_td(i, j):
    D = [[-99999 for l in range(j + 1)] for m in range(i + 1)]
    if D[i][j] == -99999:
        if i == 0:
            D[i][j] = j
        elif j == 0:
            D[i][j] = i
        else:
            ins = edit_dist_td(i, j - 1) + 1
            delete = edit_dist_td(i - 1, j) + 1
            sub = edit_dist_td(i - 1, j - 1) + is_equal(i - 1, j - 1)
            D[i][j] = min(ins, delete, sub)
    return D[i][j]


i = len(s1)
j = len(s2)
print(edit_dist_td(i, j))
