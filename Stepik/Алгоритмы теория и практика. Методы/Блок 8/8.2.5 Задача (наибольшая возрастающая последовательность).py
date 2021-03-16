import sys

number_of_inputs = next(sys.stdin)
mass = [int(i) for i in next(sys.stdin).split()]


def lis_bottom_up(mas):
    D = [0 for x in range(len(mas))]
    for i in range(len(mas)):
        D[i] = 1
        for j in range(i):
            if mas[i] % mas[j] == 0 and D[j] + 1 > D[i]:
                D[i] = D[j] + 1
    ans = (0, 0)
    for i in range(len(mas)):
        if ans[0] < D[i]:
            ans = (D[i], i)
    return ans[0]


print(lis_bottom_up(mass))
