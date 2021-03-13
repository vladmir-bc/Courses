number_of_steps = int(input())
value_each_step = [int(value) for value in input().split()]


def stairs(mas):
    d = [0 for elem in range(len(mas) + 1)]
    for i in range(1, len(d)):
        if i < 2:
            d[i] = mas[i - 1]
        else:
            d[i] = max(d[i - 2] + mas[i - 1], d[i - 1] + mas[i - 1])
    return d[-1]


print(stairs(value_each_step))