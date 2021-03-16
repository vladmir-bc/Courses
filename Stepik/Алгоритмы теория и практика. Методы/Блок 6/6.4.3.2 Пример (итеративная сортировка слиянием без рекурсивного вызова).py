def merge(mas1, mas2):
    ms = []
    while mas1 and mas2:
        if mas1[0] <= mas2[0]:
            ms.append(mas1.pop(0))
        else:
            ms.append(mas2.pop(0))
    if mas1:
        ms.extend(mas1)
    else:
        ms.extend(mas2)
    return ms


def iterative_merge_sort(mas):
    q = []
    for i in range(len(mas)):
        q.append([mas[i]])
    while len(q) > 1:
        q.append(merge(q.pop(0), q.pop(0)))
    return q[0]


mass = [4, 56, 18, -100, -1000, 99, -1.58, 65, -99999, 0, 0.5]
print(iterative_merge_sort(mass))
