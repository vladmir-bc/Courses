with open('D:\\Users\\vladm\\PycharmProjects\\Python\\dataset_3363_3.txt', 'r') as inf:
    elements = inf.read().replace('\n', ' ').lower().split()
    elements.sort()

with open('D:\\Users\\vladm\\PycharmProjects\\Python\\dataset_3363_3.txt', 'w') as ouf:
    word = str
    counter = 0
    for element in elements:
        if elements.count(element) > counter:
            counter = elements.count(element)
            word = element
    ouf.write(word + ' ' + str(counter))