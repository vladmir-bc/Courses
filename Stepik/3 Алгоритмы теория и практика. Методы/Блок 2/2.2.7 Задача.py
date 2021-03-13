def fib(n):
    fibbb = [0, 1]
    for i in range(2, n + 1):
        fibbb.append(fibbb[0] % 10 + fibbb[1] % 10)
        fibbb.pop(-3)
    return fibbb[-1] % 10


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
