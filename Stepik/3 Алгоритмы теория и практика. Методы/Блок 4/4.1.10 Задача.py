goods = []
number_of_goods = [int(i) for i in input().split()]
for elem in range(number_of_goods[0]):
    goods.append([int(i) for i in input().split()])


def knapsack(arr, capacity):
    result = int()
    arr = sorted(arr, key=lambda element: element[0] / element[1], reverse=True)
    for el in arr:
        if capacity == 0:
            return '{:.3f}'.format(result)
        elif el[1] <= capacity:
            result += el[0]
            capacity -= el[1]
        else:
            counter = 0
            while counter < capacity:
                counter += 1
            result += el[0] * (counter / el[1])
            capacity -= counter
    return '{:.3f}'.format(result)


print(knapsack(goods, number_of_goods[1]))
