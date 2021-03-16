goods = [[20, 4], [18, 3], [14, 2], [1, 1]]


def knapsack(arr, capacity):
    result = []
    arr = sorted(arr, key=lambda element: element[0] / element[1], reverse=True)
    for el in arr:
        if capacity == 0:
            return result
        elif el[1] <= capacity:
            result.append(el)
            capacity -= el[1]
        else:
            counter = 0
            while counter < capacity:
                counter += 1
            result.append([el[0] * (counter / el[1]), counter / el[1]])
            capacity -= counter
    return result


print(knapsack(goods, 8))
