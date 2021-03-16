a, c = int(input()), 1
b = []
for i in range(a):
    b += [c]*(i+1)
    c += 1
for j in range(a):
    d = b[j]
    print(d, end=' ')