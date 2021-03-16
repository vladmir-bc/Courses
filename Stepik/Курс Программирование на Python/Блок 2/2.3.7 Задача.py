a, b, c, f, l = int(input()), int(input()), 0, 0, 0
for i in range(a, b + 1):
    if i % 3 == 0:
        c += i
        l += 1
f = c / l
print(f)
