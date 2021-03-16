# a = int #мой вариант
# b = 0
# while b >= 0:
#     a = int(input())
#     if a > 100:
#         break
#     elif a < 10:
#         continue
#     print(a)
#     b += 1

# while True: #альтернативный вариант, не мой
#     i = int(input())
#     if i >100:
#         break
#     if i <10:
#         continue
#     print(i)

a = 0
while a <= 100:
    a = int(input())
    if a <= 100 and a >=10:
        print(a)

