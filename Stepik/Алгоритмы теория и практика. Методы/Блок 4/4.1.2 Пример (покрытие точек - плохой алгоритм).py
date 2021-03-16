s = [1.1, 1.2, 1.3, 1.4]
s.sort()
answer = []
while s:
    x_m = s[0]
    answer.append([x_m, x_m + 1])
    counter = 0
    # for element in s:
    #     if element > answer[-1][-1]:
    #         break
    #     s.pop(0)
    try:
        while s[counter] <= answer[-1][-1]:
            s.pop(counter)
    except:
        break
print(s)
print(answer)
