import random


def binary_search(mas, k):
    mas.sort()
    print(mas)
    l = 0
    r = len(mas) - 1
    while l <= r:
        m = (l + r) // 2
        if mas[m] == k:
            try:
                if mas[m + 1] == k:
                    l = m + 1
                else:
                    return m
            except:
                return m
        elif mas[m] > k:
            r = m - 1
        else:
            l = m + 1
    return -1


# mas = [random.randint(0, 5) for i in range(5)]
mas = [random.randint(-2, 2) for i in range(50)]
k = 0
print(binary_search(mas, k))
