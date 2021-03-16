class BadName(Exception):
    pass

def greet(name):
    '''Функция, которая приветствует человека по имени'''
    if name[0].isupper():  # метод строки isupper проверяет, является ли первая буква заглавной
        return 'Hello, ' + name
    else:
        raise BadName(name + ' is inappropriate name')

print('Import is execution')