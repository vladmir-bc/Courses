s = [[7, 15], [15, 20], [0, 15], [0, 4], [0, 4], [3, 5], [2.8, 4.2], [2.5, 8], [4, 8], [7, 9], [9, 12], [12, 15]]
s = sorted(s, key=lambda element: element[1])
print(s)
result = []

for element in s:
    if len(result) == 0:
        result.append(element)
    if result[-1][-1] <= element[0]:
        result.append(element)

print(result)
print(len(result))