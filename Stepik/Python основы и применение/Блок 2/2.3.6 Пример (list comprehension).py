x = [-2, -1, 0, 1, 2]
y = [i * i for i in x]
print(y)  # [4, 1, 0, 1, 4]

z = [(x, y) for x in range(3) for y in range(3) if y >= x]
print(z)  # [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]

z = ((x, y) for x in range(3) for y in range(3) if y >= x)
print(type(z))  # <class 'generator'>
print(next(z))  # (0, 0)
print(next(z))  # (0, 1)