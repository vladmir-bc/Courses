import os
import os.path
import shutil

shutil.copy('main.py', 'test 1//test 1.1//Новая папка 1')  # копирует файл main.py из текущего каталога в новую папку

shutil.copytree('test4', 'test 1//test 1.1//Новая папка 1//test4')

for currentdir, dirs, files in os.walk('.'):  # перебирает текущую директорию, подпапку и файлы. '.' - означает. что нужно начать с текущей директории
    print(currentdir, dirs, files)


