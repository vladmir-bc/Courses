f = input()
import math
if f == 'треугольник':
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    print(math.sqrt(p * (p - a) * (p - b) * (p - c)))
elif f == 'прямоугольник':
    a = float(input())
    b = float(input())
    print(a * b)
elif f == 'круг':
    r = float(input())
    pi = 3.14
    print(pi * r ** 2)
