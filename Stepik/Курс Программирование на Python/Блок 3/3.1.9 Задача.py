lst = [2, 4, 6, 8, 9, 10]


def modify_list(l):
    a = len(l)
    for i in range(a):
        if l[i] % 2 == 0:
            l.append(int(l[i] / 2))
    del l[:a]


print(modify_list(lst))
print(lst)
print(modify_list(lst))
print(lst)
print(modify_list(lst))
print(lst)
