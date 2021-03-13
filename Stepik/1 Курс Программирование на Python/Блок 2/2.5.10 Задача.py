a = [int(i) for i in input().split()]
if len(a) == 1:
    print(a[0])
    exit(0)
m = 0
f = 0
for k in a:
    if m + 1 == len(a):
        print(a[m - 1] + a[0], end='')
        exit(0)
    else:
        f = a[m - 1] + a[m + 1]
        print(f, end=' ')
    m += 1

