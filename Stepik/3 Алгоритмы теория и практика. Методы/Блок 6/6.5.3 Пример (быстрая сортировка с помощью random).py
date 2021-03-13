import random


def quick_sort(mas, l, r):
    def partition(mas, l, r):
        f = random.randint(l, r - 1)
        mas[f], mas[r - 1] = mas[r - 1], mas[f]
        j = l
        for i in range(l, r - 1):
            if mas[i] < mas[r - 1]:
                mas[i], mas[j] = mas[j], mas[i]
                j += 1
        mas[r - 1], mas[j] = mas[j], mas[r - 1]
        return j

    if l >= r:
        return mas
    m = partition(mas, l, r)
    quick_sort(mas, l, m)
    quick_sort(mas, m + 1, r)
    return mas


mass = [random.randint(-10, 10) for i in range(1000000)]
l = 0
r = len(mass)
print(quick_sort(mass, l, r))
