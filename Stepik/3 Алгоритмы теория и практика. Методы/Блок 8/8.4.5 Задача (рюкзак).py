import sys

capacity, number_of_gold = (int(i) for i in next(sys.stdin).split())
weights = [int(i) for i in next(sys.stdin).split()]


def knapsack_without_reps_bu(cap, wghts):
    d = [[0 for el in range(cap + 1)] for elem in range(len(wghts))]
    for i in range(len(wghts)):
        for w in range(cap + 1):
            d[i][w] = d[i - 1][w]
            if wghts[i] <= w:
                d[i][w] = max(d[i][w], d[i - 1][w - wghts[i]] + wghts[i])
    return d[-1][-1]


print(knapsack_without_reps_bu(capacity, weights))