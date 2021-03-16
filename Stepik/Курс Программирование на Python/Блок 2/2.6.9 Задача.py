a, b, c, j = [int(i) for i in input().split()], int(input()), [], 0
for i in a:
    if i == b:
        c += [j]
    j += 1
if len(c) == 0:
    print('Отсутствует')
else:
    for i in c:
        print(i, end=' ')

#После моего усовершенствования:
# a, b = [int(i) for i in input().split()], int(input())
# for i in range(len(a)):
#     if a[i] == b:
#         print(i, end = ' ')
# if b not in a:
#     print('Отсутствует')

#Чужое решение:
# l = [int(i) for i in input().split()]
# x = int(input())
# if x not in l: print('Отсутствует')
# else:
#     for i in range(len(l)):  # здесь лучше задать else, чтобы программа не прогоняла по списку, если "Отсутствует"
#         if l[i] == x: print(i, end=' ')
