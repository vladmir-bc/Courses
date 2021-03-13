import sys

# capacity, *weights = (int(i) for i in next(sys.stdin).split())
# coasts = [int(i) for i in next(sys.stdin).split()]

capacity, weights = 10, [6, 3, 4, 2]
coasts = [30, 14, 16, 9]


def knapsack_with_reps_bu(cap, wghts, csts):
    d = [0 for el in range(cap + 1)]
    for w in range(cap + 1):
        for i in (range(len(csts))):
            if wghts[i] <= w:
                d[w] = max(d[w], d[w - wghts[i]] + csts[i])
    return d


print(knapsack_with_reps_bu(capacity, weights, coasts))
