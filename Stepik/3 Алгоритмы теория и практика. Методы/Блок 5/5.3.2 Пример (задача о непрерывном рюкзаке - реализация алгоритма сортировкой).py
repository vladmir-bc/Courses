import sys


def fractional_knapsack(capacity, values_and_weights):
    order = [(v / w, w) for v, w in values_and_weights]  # удельная ценность - v, количество предмета в наличии - w
    order.sort(reverse=True)
    acc = 0  # аккумулятор - стоимость рюкзака на данный момент
    for v_per_w, w in order:
        if w < capacity:  # если все помещается
            acc += v_per_w * w  # берем полностью
            capacity -= w  # уменьшаем вместимость на величину положенной вещи
        else:
            acc += v_per_w * capacity  # если не помещается, кладём сколько сможем
            break
    return acc


def main():
    reader = (tuple(map(int, line.split())) for line in
              sys.stdin)  # разбивает строку на куски, каждый кусок приводит к целому числу. Функция map - генератор
    n, capacity = next(reader)
    # n, capacity = reader  # в таком случае, ввод будет бесконечен, но возникнет ошибка too many values to unpack (expected 2) на 3 вводе
    values_and_weights = []
    for elem in range(n):
        values_and_weights.append(list(next(reader)))
        # print(values_and_weights)
    # assert len(values_and_weights) == n
    opt_value = fractional_knapsack(capacity, values_and_weights)
    print('{:.3f}'.format(opt_value))


if __name__ == '__main__':
    main()
