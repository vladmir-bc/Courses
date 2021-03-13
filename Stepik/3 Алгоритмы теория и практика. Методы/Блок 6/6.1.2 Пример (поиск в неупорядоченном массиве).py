import random


def LinearSearch(mas, k):
    print(mas)
    for i in range(len(mas)):
        if mas[i] == k:
            return i
    return -1


mas = [random.randint(0, 5) for i in range(5)]
print(LinearSearch(mas, k=5))
