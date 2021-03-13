a = [int(i) for i in input().split()]
a.sort()
if len(a) == 0:
    exit(0)
m = 0
while m + 1 < len(a):
    if a[m] == a[m + 1] and a[m] != a[m - 1]:
        print(a[m], end=' ')
        m += 1
    elif min(a) == max(a):
        print(a[m], end=' ')
        exit(0)
    else:
        m += 1