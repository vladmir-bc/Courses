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


def merge_sort(mas, l, r):
    if len(mas[l:r]) == 1:
        return mas[l:r]
    m = (l + r) // 2
    print(mas[l:r])
    return merge(merge_sort(mas, l, m), merge_sort(mas, m, r))


mass = [4, 56, 18, -100, -1000, 99, -1.58, 65, -99999, 0, 0.5]
left = 0
right = len(mass)
print(merge_sort(mass, left, right))
