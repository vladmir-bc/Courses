def fib_mod(n, m):
    fibbb = [0, 1]
    for i in range(2, n + 1):
        fibbb.append(fibbb[0] + fibbb[1])
        fibbb.pop(-3)
    return fibbb[-1] % m


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
