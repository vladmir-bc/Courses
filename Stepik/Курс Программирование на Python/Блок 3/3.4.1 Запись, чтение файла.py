# a = open('D:\\Users\\vladm\\PycharmProjects\\Python\\file.txt', 'r')
# s1 = a.readline()
# s2 = a.readline()
# s3 = a.readline()
# s4 = a.readline()
# print(s1)
# print(s2)
# print(s3)
# a.close()




with open('D:\\Users\\vladm\\PycharmProjects\\Python\\file.txt', 'w') as ouf:
    ouf.write('\t Some text\n')
    ouf.write(str(25))

with open('D:\\Users\\vladm\\PycharmProjects\\Python\\file.txt', 'r') as a:
    for line in a:
        line = line.strip()
        print(line)

# 'D:\\Users\\vladm\\PycharmProjects\\Python\\file.txt', 'r'
