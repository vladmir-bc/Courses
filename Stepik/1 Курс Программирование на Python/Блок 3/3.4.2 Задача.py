# with open('D:\\Users\\vladm\\PycharmProjects\\Python\\dataset_3363_2.txt', 'r') as inf:
#     a = inf.readline().strip()
#
# with open('D:\\Users\\vladm\\PycharmProjects\\Python\\dataset_3363_2.txt', 'w') as ouf:
#     i = 0
#     c = 0
#     while i + 1 < len(a):
#         repeats = 1
#         while a[i].isdigit():
#             if a[i].isdigit() and a[i + 1].isalpha():
#                 c = int(''.join(a[i:i + repeats]))
#                 ouf.write(str(a[i - 1] * c))
#                 i += 1
#                 continue
#             while a[i + repeats].isdigit():
#                 repeats += 1
#                 c = int(''.join(a[i:i + repeats]))
#                 if i + repeats == len(a):
#                     ouf.write(str(a[i - 1] * c))
#                     exit()
#                 elif a[i + repeats].isalpha():
#                     ouf.write(str(a[i - 1] * c))
#             i += repeats
#         i += 1




with open('D:\\Users\\vladm\\PycharmProjects\\Python\\dataset_3363_2.txt', 'r') as f:
    s = f.readline().strip()
    print(s)
    i = 0
    while i < len(s):
        j = i + 1
        while j < len(s) and s[j].isdigit():
            j += 1
        print(s[i] * int(s[i+1:j]), end='')
        i = j