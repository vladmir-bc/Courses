a, b, c, d = int(input()), int(input()), int(input()), int(input())
print(end='\t')
for f in range(c, d + 1):
    print(f, end='\t')
print()
for i in range(a, b + 1):
    print(i, end='\t')
    for j in range(c, d + 1):
        print(i * j, end='\t')
    print()