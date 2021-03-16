import os

import os.path

print(os.getcwd())  # выводит текущую директорию  D:\Users\vladm\PycharmProjects\Python\Программирование на Python\Stepik\2 Python основы и применение\Блок 2
print(os.listdir('test 1'))  # перечисляет файлы внутри указанной директории  ['test 1.1', 'test 1.2', 'test 1.3', 'test 1.4', 'test 1.5', 'test 1.6', 'test 1.7']

print(os.path.exists('fib.py'))  # проверяет, существует ли файл или папка в директории  True
print(os.path.exists('random.py'))  # проверяет, существует ли файл или папка в директории  False

print(os.path.isfile('exceptions.py'))  # проверяет, файл ли это  True
print(os.path.isdir('test4'))  # проверяет, папка ли это  True
print(os.path.isdir('test 1//test 1.1'))  # True

print(os.path.abspath('fib.py'))  # выводит абсолютный путь к файлу (включая сам файл) D:\Users\vladm\PycharmProjects\Python\Программирование на Python\Stepik\2 Python основы и применение\Блок 2\fib.py

os.chdir('test 1')  # меняет директорию, переходит в указанную папку
print(os.getcwd())  # выводит текущую директорию D:\Users\vladm\PycharmProjects\Python\Программирование на Python\Stepik\2 Python основы и применение\Блок 2\test 1
