mass = [7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3, 8, 1]

def lis_bottom_up(mas):
    D = [0 for x in range(len(mas))]
    for i in range(len(mas)):
        D[i] = 1
        for j in range(i):
            if mas[j] < mas[i] and D[j] + 1 > D[i]:
                D[i] = D[j] + 1
    ans = max(D)
    return ans

print(lis_bottom_up(mass))