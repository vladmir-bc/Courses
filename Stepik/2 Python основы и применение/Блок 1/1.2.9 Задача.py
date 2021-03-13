# ans = 0
# objects = [1, 1, 1, 2, 2, 3, 4]
# objects2 = set
#
# for obj in objects:  # доступная переменная objects
#     objects2 = set(objects)
#
#
#
# print(len(objects2))

# objects = [1, 1, 1, 2, 3]
# objects2 = set
# ans = 0
# for obj in objects:  # доступная переменная objects
#     ans += 1
#     objects2.add(id(obj))
# print(ans)
# print(objects2)

ans = 0
objects = [1, 1, 1, 2, 3]
objects2 = []
for obj in objects: # доступная переменная objects
    if obj not in objects2:
        objects2.append(obj)


print(len(objects2))