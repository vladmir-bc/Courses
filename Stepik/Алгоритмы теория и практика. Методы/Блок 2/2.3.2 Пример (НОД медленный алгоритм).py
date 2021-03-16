def NaiveGCD(a, b):
    gcd = 1
    for d in range(2, max(a, b) + 1):
        if a % d == 0 and b % d == 0:
            gcd = d
    return gcd


print(NaiveGCD(14159572, 63967072))
