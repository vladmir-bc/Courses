# Вывести сумму нечетных чисел от a до b (включая обе границы)
a, b = int(input()), int(input())
c = 0
for i in range(a, b + 1):
    if i % 2 != 0:
        c += i
print(c)

# if a % 2 != 0:
#     for i in range(a, b + 1, 2):
#         c += i
#     print(c)
# else:
#     for i in range(a, b + 1):
#         if i % 2 != 0:
#             c += i
#     print(c)

