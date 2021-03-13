# s = input()
# t = input()
# # print(s.count(t))
# counter = 0
# for number in range(len(s)):
#     while number <= len(s) - len(t):
#         # print(s[number:number + len(t)])
#         if s[number:number + len(t)] == t:
#             counter += 1
#             break
#         else:
#             break
# print(counter)

s, t = input(), input()
counter = 0
for number in range(len(s)):
    if number <= len(s) - len(t) and s.count(t, number, number + len(t)):
        counter += 1
print(counter)
