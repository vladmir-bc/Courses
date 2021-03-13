# s, a, b = input(), input(), input()
# number_of_operations, counter = 0, 0
# if a in s:
#     while a in s:
#         counter = s.count(a)
#         s = s.replace(a, b)
#         if s.count(a) >= counter:
#             print('Impossible')
#             break
#         number_of_operations += 1
#     else:
#         print(number_of_operations)
# else:
#     print(number_of_operations)

# Если так сделать, то не засычитывает

s, a, b = input(), input(), input()
number_of_operations = 0
if a in s:
    while a in s:
        if a in b and a != b:
            print('Impossible')
            break
        s = s.replace(a, b)
        number_of_operations += 1
        if number_of_operations > 1000:
            print('Impossible')
            break
    else:
        print(number_of_operations)
else:
    print(number_of_operations)