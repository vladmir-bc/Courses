s = [1.1, 1.2, 1.3, 1.4, 3, 3.5, 4, 8, 10]
s.sort()
answer = []
i = 0
while i <= len(s) - 1:
    x_m = s[i]
    answer.append([x_m, x_m + 1])
    i += 1
    while i <= len(s) - 1 and s[i] <= answer[-1][-1]:
        i += 1
print(s)
print(answer)
