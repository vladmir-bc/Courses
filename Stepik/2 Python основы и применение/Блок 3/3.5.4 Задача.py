import json

classes = json.loads(input())
path = set()
number = 1
parent = []
data_dict = {}


def rec(parent, graph):
    global number
    global path
    for el in graph:
        if len(el['parents']) > 0:
            if parent in el['parents'] and el['name'] not in path:
                path.add(el['name'])
                number += 1
                rec(el['name'], graph)


for element in classes:
    rec(element['name'], classes)
    data_dict[element['name']] = number
    number = 1
    path.clear()

data_list = [data_dict]
data_json = json.dumps(data_list, indent=4, sort_keys=True)
data_again = json.loads(data_json)
for key, value in data_again[0].items():
    print(str(key) + ' : ' + str(value))
