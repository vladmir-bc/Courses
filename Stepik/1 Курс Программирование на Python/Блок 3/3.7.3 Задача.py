number_of_addes = int(input())
dictionary = set()

for element in range(number_of_addes):
    dictionary.add(input().lower())
check = int(input())
check_dict = []
for element2 in range(check):
    check_dict += [input().split()]

check_d = set()
for element in check_dict:
    for elem2 in element:
        if elem2.lower() not in dictionary and elem2 not in check_d:
            check_d.add(elem2)
            print(elem2)