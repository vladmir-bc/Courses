with open('D:\\Users\\vladm\\PycharmProjects\\Python\\dataset_3363_4.txt', 'r', encoding='utf-8') as inf:
    elements = []
    for lines in inf:
        elements += [lines.strip().split(';')]

with open('D:\\Users\\vladm\\PycharmProjects\\Python\\dataset_3363_4.txt', 'w') as ouf:
    for element in elements:
        for di in range(1, 4):
            element[di] = int(element[di])
    print(elements)
    print(len(elements))

    for unit in elements:
        a = 0
        for di in range(1, 4):
            a += unit[di]
            if di == 3:
                ouf.write('%.9f' % (a / 3) + '\n')  # ouf.write + '\n'
                print('%.9f' % (a / 3))
    b = 0
    c = 0
    d = 0
    for unit in elements:
        b += unit[1]
        c += unit[2]
        d += unit[3]
    ouf.write('%.9f %.9f %.9f' % (b / len(elements), c / len(elements), d / len(elements)))
    ouf.write('\n')