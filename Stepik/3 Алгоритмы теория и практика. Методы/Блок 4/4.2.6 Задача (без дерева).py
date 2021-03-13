requests = [int(i) for i in input().split()]
code = {}
for request in range(requests[0]):
    req = input().split(': ')
    code[req[1]] = req[0]
string = input()
assert requests[1] == len(string)

counter = 0
while string:
    for el in code:
        if el == string[counter:counter + len(el)]:
            print(code[el], end='')
            counter += len(el)
            break
    if len(string) == counter:
        string = False