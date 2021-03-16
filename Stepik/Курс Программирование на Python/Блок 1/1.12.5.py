a = int(input())
b = int(input())
c = int(input())
d = max(a, b, c)
e = min(a, b, c)
print(d)
print(e)
if a == b:
    print(b)
elif a == c:
    print(c)
elif b == c:
    print(c)
elif a > b and a < c or a < b and a > c:
    print(a)
elif b > a and b < c or b < a and b > c:
    print(b)
elif c > a and c < b or c < a and c > b:
    print(c)
