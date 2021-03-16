number = int(input())


def number_of_operations(number):
    d = [0 for i in range(number)]
    a = []
    for elem in range(len(d)):
        if elem == 0:
            a.append(1)
            try:
                d[elem + 1] += 1
                d[elem + 2] += 1
            except:
                continue
        else:
            try:
                if d[elem + 1] == 0:
                    d[elem + 1] += d[elem] + 1
                else:
                    d[elem + 1] = min(d[elem] + 1, d[elem + 1])
                if d[(elem + 1) * 2 - 1] == 0:
                    d[(elem + 1) * 2 - 1] += d[elem] + 1
                else:
                    d[(elem + 1) * 2 - 1] = min(d[elem] + 1, d[(elem + 1) * 2 - 1])
                if d[(elem + 1) * 3 - 1] == 0:
                    d[(elem + 1) * 3 - 1] += d[elem] + 1
                else:
                    d[(elem + 1) * 3 - 1] = min(d[elem] + 1, d[(elem + 1) * 3 - 1])
            except:
                continue
    a = [len(d)] #10, 9
    counter = len(d) - 1 #9, 8,5
    while counter > 0:
        if (counter + 1) % 2 == 0 and (counter + 1) % 3 == 0:
            if d[counter - 1] < min(d[int((counter + 1) / 2) - 1], d[int((counter + 1) / 3) - 1]):
                a.append(counter)
                counter -= 1
            elif d[int((counter + 1) / 3) - 1] <= d[int((counter + 1) / 2) - 1]:
                a.append(int((counter + 1) / 3))
                counter = int((counter + 1) / 3 - 1)
            else:
                a.append(int((counter + 1) / 2))
                counter = int((counter + 1) / 2 - 1)
        elif (counter + 1) % 2 == 0:
            if d[counter - 1] < d[int((counter + 1) / 2 - 1)]:
                a.append(counter)
                counter -= 1
            else:
                a.append(int((counter + 1) / 2))
                counter = int((counter + 1) / 2 - 1)
        elif (counter + 1) % 3 == 0:
            if d[counter - 1] < d[int((counter + 1) / 3) - 1]:
                a.append(counter)
                counter -= 1
            else:
                a.append(int((counter + 1) / 3))
                counter = int((counter + 1) / 3 - 1)
        else:
            a.append(counter)
            counter -= 1
    a.reverse()
    print(d[-1])
    for el in a:
        print(el, end=' ')
    return


number_of_operations(number)