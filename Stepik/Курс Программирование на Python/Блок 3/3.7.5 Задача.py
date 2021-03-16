with open('D:\\Users\\vladm\\PycharmProjects\\Python\\dataset_3380_5.txt', 'r') as s:
    student_lst = list()
    for line in s:
        line = line.strip()
        student_lst.append(line.split())
student_dict = dict()
for element in student_lst:
    element[0], element[2] = int(element[0]), int(element[2])
    if element[0] not in student_dict:
        student_dict[element[0]] = [element[2]]
    else:
        student_dict[element[0]].append(element[2])

for element in range(1, 12):
    if element in student_dict:
        print(element, (sum(student_dict[element]) / len(student_dict[element])))
    else:
        print(element, '-')
