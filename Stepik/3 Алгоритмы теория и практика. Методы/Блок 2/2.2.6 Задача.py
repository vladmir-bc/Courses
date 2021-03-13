def fib(n):
    fibbb = [0, 1]
    for i in range(2, n + 1):
        fibbb.append(fibbb[i - 1] + fibbb[i - 2])
    return fibbb[-1]


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()