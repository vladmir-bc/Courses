numb = int(input())


def result(number):
    res = []
    counter = 1
    while number != 0:
        if number - counter == 0:
            res.append(counter)
            number -= counter
            continue
        if counter + counter + 1 > number:
            counter += 1
            continue
        res.append(counter)
        number -= counter
        counter += 1
    print(len(res))
    for elem in res:
        print(elem, end=' ')


result(numb)
