import sys
number_of_operations = int(sys.stdin.readline())
heap = []
requests = []
for request in range(number_of_operations):
    requests.append(sys.stdin.readline().split())
for request in range(len(requests)):
    if 'Insert' in requests[request][0]:
        heap.append(int(requests[request][1]))
    else:
        if request > 0 and requests[request-1][0] == 'Insert':
            heap.sort()
        print(heap.pop(), end=', ')