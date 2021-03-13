number_of_requests = int(input())
requests = list()
dict_of_requests = dict()
for request in range(number_of_requests):
    requests.append(input().split())
for element in requests:
    if ':' in element:
        element.remove(':')
for element in requests:
    if len(element) == 1:
        dict_of_requests[element[0]] = ['object']
    else:
        dict_of_requests[element[0]] = element[1:]
Mydict = dict_of_requests.copy()
for value in Mydict.values():
    if len(value) == 1:
        if value[0] not in dict_of_requests and value[0] != 'object':
            # for el in list(value):
            dict_of_requests[value[0]] = 'object'
    else:
        for element in value:
            if element not in dict_of_requests:
                dict_of_requests[element] = 'object'
req = set()
for element in requests:
    for el in element:
        req.add(el)
counter = 0
def DFS(graph, parent, child):
    global counter
    if parent == child:
        counter += 1
        return
    elif child not in req:
        return
    if parent not in graph and child not in graph or graph[child] == 'object':
        return
    for parents in graph[child]:
        if parents == parent:
            counter += 1
        if parents in graph:
            DFS(graph, parent, parents)
number_of_outs = int(input())
outs = []
new_out = dict()
new_out2 = []
for out in range(number_of_outs):
    outs += [input()]
for elem in range(len(outs)):
    for out in range(len(outs)):
        DFS(dict_of_requests, outs[elem], outs[out])
        if counter > 0:
            if outs[out] not in new_out:
                new_out[outs[out]] = [outs[elem]]
            elif outs[out] in new_out and outs[elem] not in new_out[outs[out]]:
                new_out[outs[out]].append(outs[elem])
        counter = 0
for i in outs:
    for j in outs:
        if outs.index(i) > outs.index(j) and j in new_out[i]:
            if i not in new_out2:
                new_out2.append(i)
                print(i)