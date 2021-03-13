dictionary = {}
b = input().split()
i = 0
for element in b:
    b[i] = element.lower()
    i += 1
for element in b:
    counter = b.count(element)
    dictionary[element] = counter
    i += 1
for key, value in dictionary.items():
    print(key, value)
