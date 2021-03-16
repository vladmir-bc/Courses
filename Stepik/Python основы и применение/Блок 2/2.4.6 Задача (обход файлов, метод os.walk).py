import os.path

for currentdir, dirs, files in os.walk(
        'Задание 2.4.6'):  # перебирает текущую директорию, подпапку и файлы
    for element in files:
        if element[-3:] == '.py':
            print(currentdir[14:])
            break
