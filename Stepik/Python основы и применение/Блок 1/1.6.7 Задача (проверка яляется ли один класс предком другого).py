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
req = set()
for element in requests:
    for el in element:
        req.add(el)
counter = 0




def DFS(graph, parent, child):
    global counter
    if parent not in graph and child not in graph:
        return
    if parent == child:
        counter += 1
        return
    elif child not in req:
        return
    for parents in graph[child]:
        if parents == parent:
            counter += 1
        if parents in graph:
            DFS(graph, parent, parents)


number_of_outs = int(input())
outs = []
for out in range(number_of_outs):
    outs += [input().split()]
for out in outs:
    if len(out) == 1:
        print('Yes')
        continue
    DFS(dict_of_requests, out[0], out[1])
    if counter > 0:
        print('Yes')
    else:
        print('No')
    counter = 0
