number_of_segments = int(input())
segments = []
result = []
for segment in range(number_of_segments):
    segments.append([int(i) for i in input().split()])
segments = sorted(segments, key=lambda element: element[1])
for element in segments:
    if len(result) == 0:
        result.append(element[1])
    if element[0] > result[-1]:
        result.append(element[1])

print(len(result))
for el in result:
    print(el, end=' ')