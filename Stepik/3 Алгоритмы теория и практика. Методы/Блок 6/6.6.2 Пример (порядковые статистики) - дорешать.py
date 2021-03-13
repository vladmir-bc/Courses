import random


def random_select(mas, l, r, k):
    if l >= r:
        return mas[l]
    f = random.randint(l, r - 1)
    # print(f)
    # f = int(input())
    x = mas[f]
    head = [element for element in mas if element < x]
    # head.sort()
    equal = [element for element in mas if element == x]
    # equal.sort()
    tail = [element for element in mas if element > x]
    # tail.sort()
    if l <= k <= len(head) - 1:
        return random_select(mas, l, len(head) - 1, k)
    elif len(head) <= k <= len(head) + len(equal):
        return x
    else:
        return random_select(mas, len(head) + len(equal), r, k)


mass = [8, 9, 9, 1, 7, 5, 5]
l = 0
r = len(mass)
k = 5
print(random_select(mass, l, r, k))

# import random
# 
# 
# def quick_sort(mas, l, r):
#     def partition(mas, l, r):
#         f = random.randint(l, r - 1)
#         mas[f], mas[r - 1] = mas[r - 1], mas[f]
#         j = l
#         counter = 0
#         for i in range(l, r - 1):
#             if i + counter >= r - 1:
#                 break
#             if mas[i] == mas[r - 1]:
#                 while mas[i] == mas[r - 1 - counter] and (r - 1 - counter) != i:
#                     counter += 1
#                 mas[i], mas[r - 1 - counter] = mas[r - 1 - counter], mas[i]
#                 if (mas[i] < mas[r - 1]) and ((r - 1 - counter) != i):
#                     mas[i], mas[j] = mas[j], mas[i]
#                     j += 1
#             elif mas[i] < mas[r - 1]:
#                 mas[i], mas[j] = mas[j], mas[i]
#                 j += 1
#         mas[j:j + counter + 1], mas[r - 1 - counter:r] = mas[r - 1 - counter:r], reversed(mas[j:j + counter + 1])
#         return j, j + counter
# 
#     while l < r:
#         m = partition(mas, l, r)
#         quick_sort(mas, l, m[0])
#         l = m[1] + 1
#     return mas
# 
# 
# mas = [random.randint(-100000000, 100000000) for i in range(5000000)]
# k = 3
# l = 0
# r = len(mas)
# print(quick_sort(mas, l, r))

# Проверка:
# for el in range(len(mas)):
#     if el < len(mas) - 1:
#         try:
#             assert mas[el] <= mas[el + 1]
#         except:
#             print(el)
