sum = 0
a = []
f = True
i = 0
while f == True:
    a += [int(i) for i in input().split()]
    sum += a[i]
    i+=1
    if sum == 0:
        break
for i in a:
    sum += i ** 2
print(sum)

# Хорошее решение:
# a = int(input())
# c = a ** 2
# while a != 0:
#     b = int(input())
#     a += b
#     c += b ** 2
# print(c)