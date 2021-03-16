a, b, c, d = int(input()), 'программист', 'а', 'ов'
if (a == 0) or (a % 100 == 0) or (a % 100 == 11) or (5 <= a % 100 <= 19 or 5 <= a % 10 <= 9 or (a % 10 == 0 and a != 0)):
    print(a, b + d)
elif a % 10 == 1:
    print(a, b)
else:
    print(a, b + c)
