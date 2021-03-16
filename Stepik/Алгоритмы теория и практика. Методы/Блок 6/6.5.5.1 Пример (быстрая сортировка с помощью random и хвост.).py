import random


def quick_sort(mas, l, r):
    def partition(mas, l, r):
        f = random.randint(l, r - 1)
        print(f)
        mas[f], mas[r - 1] = mas[r - 1], mas[f]
        j = l
        for i in range(l, r - 1):
            if mas[i] < mas[r - 1]:
                mas[i], mas[j] = mas[j], mas[i]
                j += 1
        mas[r - 1], mas[j] = mas[j], mas[r - 1]
        return j
    while l < r:
        m = partition(mas, l, r)
        quick_sort(mas, l, m)
        l = m + 1
    return mas


mass = [random.randint(-1, 1) for i in range(100000)]
l = 0
r = len(mass)
print(quick_sort(mass, l, r))

# for el in range(len(mass)):
#     try:
#         assert mass[el] <= mass[el + 1]
#     except:
#         print(el)