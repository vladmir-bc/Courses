import os
import os.path

catalogues = []


def rec(name, path, level=1):
    new_path = path + '\\' + name
    for element in os.listdir(new_path):
        if os.path.isdir(new_path + '\\' + element):
            rec(element, new_path, level=level + 1)
        else:
            if element[-3:] == '.py':
                if new_path[122:] not in catalogues:
                    catalogues.append(new_path[122:])
    return


rec('Задание 2.4.6',
    'D:\\Users\\vladm\\PycharmProjects\\Python\\Программирование на Python\\Stepik\\2 Python основы и применение\\Блок 2')
catalogues.sort()
for i in catalogues:
    print(i)
