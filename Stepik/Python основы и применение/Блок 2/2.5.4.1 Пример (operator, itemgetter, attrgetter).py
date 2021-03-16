import operator as op

print(op.add(4, 5))  # сложение = 9
print(op.mul(4, 5))  # произведение = 20
print(op.contains([1, 2, 3], 4))  # проверяет, входит ли число 4 в список: False

x = [1, 2, 3]
f = op.itemgetter(1) # f(x) == x[1]: 2
print(f(x))

f = op.attrgetter('sort')  # f(x) == x.sort
print(f([]))