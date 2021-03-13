import heapq


# Первый метод
# def heap_sort(mas):
#     heapq.heapify(mas)
#     while mas:
#         print(heapq.heappop(mas), end=' ')


# Второй метод
def heap_sort(mas):
    heapq.heapify(mas)
    h = []
    while mas:
        h.append(heapq.heappop(mas))
    for i in h:
        print(i, end=' ')


mass = [2, 1, 0, 5, 4, 9, 9, 9, 0, -500, 1000000, 1.01]
heap_sort(mass)
