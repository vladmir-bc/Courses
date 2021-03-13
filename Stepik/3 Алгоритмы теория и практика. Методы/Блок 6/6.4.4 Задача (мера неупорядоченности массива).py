import sys

counter = 0
n = int(input())
reader = ((map(int, line.split())) for line in sys.stdin)
mass = list(next(reader))


def merge(mas1, mas2):
    global counter
    ms = []
    while mas1 and mas2:
        if mas1[0] <= mas2[0]:
            ms.append(mas1.pop(0))
        else:
            counter += len(mas1)
            ms.append(mas2.pop(0))
    ms.extend(mas1 or mas2)
    return ms


def merge_sort(mas, l, r):
    if r - l == 1:
        return mas[l:r]
    m = (l + r) // 2
    return merge(merge_sort(mas, l, m), merge_sort(mas, m, r))


left, right = 0, len(mass)
merge_sort(mass, left, right)
print(counter)