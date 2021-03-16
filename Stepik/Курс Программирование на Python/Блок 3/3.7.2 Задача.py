for_crypt, key, encode, encrypted = list(input()), list(input()), list(input()), list(input())
dictionary = dict()
for element in range(len(for_crypt)):
    dictionary[for_crypt[element]] = key[element]
for element in encode:
    print(dictionary[element], end='')
print()
for element in encrypted:
    for key, value in dictionary.items():
        if value == element:
            print(key, end='')