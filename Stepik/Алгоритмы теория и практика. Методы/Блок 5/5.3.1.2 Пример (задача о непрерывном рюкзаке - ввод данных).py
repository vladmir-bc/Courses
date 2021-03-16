import sys


def fractional_knapsack(capacity, values_and_weights):
    return 0


def main():
    reader = (tuple(map(int, line.split())) for line in
              sys.stdin)  # разбивает строку на куски, каждый кусок приводит к целому числу. Функция map - генератор
    n, capacity = next(reader)
    # n, capacity = reader  # в таком случае, ввод будет бесконечен, но возникнет ошибка too many values to unpack (expected 2) на 3 вводе
    for elem in range(n):
        values_and_weights = list(next(reader))
        print(values_and_weights)
    # assert len(values_and_weights) == n
    opt_value = fractional_knapsack(capacity, values_and_weights)
    print('{:.3f}'.format(opt_value))


if __name__ == '__main__':
    main()
