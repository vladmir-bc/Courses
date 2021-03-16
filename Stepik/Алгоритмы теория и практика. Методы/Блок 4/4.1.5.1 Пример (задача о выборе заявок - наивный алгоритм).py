s = [[0, 15], [0, 4], [0, 4], [3, 5], [2.8, 4.2], [2.5, 8], [4, 8], [7, 9],
     [7, 15], [9, 12], [12, 15], [15, 20]]

result = []
counter = int()

while s:
    min_end = 10000000
    for element in range(len(s)):
        if s[element][1] <= min_end:
            min_end = s[element][1]
            counter = element
    result.append(s[counter])
    i = 0
    while i <= len(s) - 1:
        if s[i][0] < result[-1][-1]:
            s.pop(i)
            continue
        i += 1

print(result)
print(len(result))
