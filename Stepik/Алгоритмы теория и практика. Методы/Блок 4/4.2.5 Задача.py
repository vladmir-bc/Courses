string = list(input())


def encrypt(gr, parent, lst, level=1, path=[], crypto=dict()):
    for key in gr[parent]:
        if key in lst:
            if gr[parent].index(key) == 0:
                path.append(0)
            else:
                path.append(1)
            crypto[key] = ''.join(map(str, path[:]))
            path.pop()
        else:
            if gr[parent].index(key) == 0:
                path.append(0)
            else:
                path.append(1)
            encrypt(gr, key, lst, level=level + 1)
            path.pop()
    if len(crypto) == len(lst) and level == 1:
        return crypto


def Huffman(strng):
    h = []
    letters = set(strng)
    for element in letters:
        h.append([element, strng.count(element)])
    h = sorted(h, key=lambda el: el[1])
    counter = 0
    iterations = len(h) - 1
    graph = dict()
    crpt = str()
    if len(h) == 1:
        graph[h[0][0]] = h[0][1]
        print(len(graph), graph[h[0][0]])
        for ky, val in graph.items():
            print(ky + ':', '0')
            print('0' * val)
            return
    while counter < iterations:
        i, j = h[0], h[1]
        F = [counter + 1, i[1] + j[1]]
        graph[F[0]] = [i[0], j[0]]
        for el in range(len(h)):
            if h[el][1] >= F[1]:
                h.insert(el, F)
                counter += 1
                break
            if el == len(h) - 1:
                h.insert(el + 1, F)
                counter += 1
                break
        h.pop(0)
        h.pop(0)
    result = encrypt(graph, len(letters) - 1, letters)
    for elem in string:
        crpt += result[elem]
    print(len(letters), len(crpt))
    for key, value in result.items():
        print(key + ':', value)
    print(crpt)


Huffman(string)
