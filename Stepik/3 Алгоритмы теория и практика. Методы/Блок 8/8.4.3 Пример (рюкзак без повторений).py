import sys

# capacity, *weights = (int(i) for i in next(sys.stdin).split())
# coasts = [int(i) for i in next(sys.stdin).split()]

# capacity, weights = 10, [6, 3, 4, 2]
# coasts = [30, 14, 16, 9]


# capacity, weights = 7, [1, 3, 4, 5]
# coasts = [1, 4, 5, 7]

capacity, weights = 10, [1, 4, 8]
coasts = [1, 4, 8]


def knapsack_without_reps_bu(cap, wghts, csts):
    d = [[0 for el in range(cap + 1)] for elem in range(len(csts))]
    for i in (range(len(csts))):
        d[i][0] = 0
    for w in range(cap + 1):
        d[0][w] = 0
    for i in range(len(csts)):
        for w in range(cap + 1):
            d[i][w] = d[i - 1][w]
            if wghts[i] <= w:
                d[i][w] = max(d[i][w], d[i - 1][w - wghts[i]] + csts[i])
    return d


print(knapsack_without_reps_bu(capacity, weights, weights))
