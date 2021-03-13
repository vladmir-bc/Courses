def FibRecursive(n):  # алгоритм очень медленный
    if n <= 1:
        return n
    return FibRecursive(n - 1) + FibRecursive(n - 2)


print(FibRecursive(100000))
