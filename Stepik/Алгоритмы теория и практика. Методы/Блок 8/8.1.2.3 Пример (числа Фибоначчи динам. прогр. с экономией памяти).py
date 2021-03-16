number = int(input())


def fib_BU_improved(n):
    if n <= 1:
        return n
    prev = 0
    curr = 1
    for i in range(n - 1):
        nxt = prev + curr
        prev = curr
        curr = nxt
    return curr


print(fib_BU_improved(number))
