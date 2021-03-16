import random


def partion(mas, l, r):
    x = mas[l]
    j = l
    for i in range(l + 1, r):
        if mas[i] <= x:
            j = j + 1
            mas[j], mas[i] = mas[i], mas[j]
    mas[l], mas[j] = mas[j], mas[l]
    return j


def quick_sort(mas, l, r):
    if l >= r:
        return mas
    m = partion(mas, l, r)
    quick_sort(mas, l, m)
    quick_sort(mas, m + 1, r)
    return mas


mass = [random.randint(0, 100) for i in range(10)]
print(quick_sort(mass, 0, len(mass)))
