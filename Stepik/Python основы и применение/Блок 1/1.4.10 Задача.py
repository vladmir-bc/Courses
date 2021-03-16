number_of_requests = int(input())
requests = []
for req in range(number_of_requests):
    requests.append(input().split())

namespace_parent = {'global': None}
variables = {'global': set()}


def find_namespace(nmspc, var):
    if nmspc == 'global' and var not in variables[nmspc]:
        return None
    if nmspc in namespace_parent and var in variables[nmspc]:
        return nmspc
    return find_namespace(namespace_parent[nmspc], var)


for request in requests:
    if request[0] == 'add':
        variables[request[1]].add(request[2])

    if request[0] == 'create':
        namespace_parent[request[1]] = request[2]
        variables[request[2]].add(request[1])
        variables[request[1]] = set()
    if request[0] == 'get':
        print(find_namespace(request[1], request[2]))