import sys

number_of_inputs = int(next(sys.stdin))
mass = [int(i) for i in next(sys.stdin).split()]
assert len(mass) == number_of_inputs


def count_sort(mas):
    minimum = min(mas)
    maximum = max(mas)
    b = [0 for elem in range(minimum, maximum + 1)]
    d = [0 for el in range(len(mas))]
    for el in mas:
        b[el - minimum] += 1
    for i in range(1, len(b)):
        b[i] += b[i - 1]
    for j in range(len(mas) - 1, 0 - 1, -1):
        d[b[mas[j] - minimum] - 1] = mas[j]
        b[mas[j] - minimum] -= 1
    for element in d:
        print(element, end=' ')


count_sort(mass)

# Проверка
# for el in range(len(mass)):
#     if el < len(mass) - 1:
#         try:
#             assert mass[el] <= mass[el + 1]
#         except:
#             print(el)
