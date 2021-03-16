import heapq
import sys


def fractional_knapsack(capacity, values_and_weights):
    order = [(-v / w, w) for v, w in values_and_weights]  # удельная ценность - v, количество предмета в наличии - w
    heapq.heapify(order)  # создаем кучу типа min
    acc = 0  # аккумулятор - стоимость рюкзака на данный момент
    while order and capacity:  # пока куча не пуста
        v_per_w, w = heapq.heappop(order)  # извлекаем из кучи нулевой элемент
        can_take = min(w, capacity)  # переменная берет либо целиком, либо величину оставшейся вместимости
        acc += -v_per_w * can_take
        capacity -= can_take
    return acc


def main():
    reader = (tuple(map(int, line.split())) for line in
              sys.stdin)  # разбивает строку на куски, каждый кусок приводит к целому числу. Функция map - генератор
    n, capacity = next(reader)
    values_and_weights = []
    for elem in range(n):
        values_and_weights.append(list(next(reader)))

    opt_value = fractional_knapsack(capacity, values_and_weights)
    print('{:.3f}'.format(opt_value))


def test():
    assert fractional_knapsack(0, [(60, 20)]) == 0.0  # если вместимость рюкзака = 0
    assert fractional_knapsack(25, [(60, 20)]) == 60.0  # если вместимость больше, чем вес предмета
    assert fractional_knapsack(25, [(60, 20), [0, 100]]) == 60.0  # если есть предмет с нулевой стоимостью, то он не повлияет на результат
    assert fractional_knapsack(25, [(60, 20), (50, 50)]) == 65.0  # если вместимость меньше, чем вес всех предметов в магазине
    assert fractional_knapsack(50, [(60, 20), (100, 50), (120, 30)]) == 180.0  # тестовый пример
    from random import randint
    from timing import timed

if __name__ == '__main__':
    test()


# Ввод:
# 3 50
# 60 20
# 100 50
# 120 30

# Вывод:
# 180.000