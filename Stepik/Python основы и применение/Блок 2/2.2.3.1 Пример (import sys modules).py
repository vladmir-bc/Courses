import sys
import check  # check

print(type(sys.modules))  # <class 'dict'>
print(sys.modules)  # словарь, где ключами являются названия модулей, а значениями - module object
print(type(check))  # <class 'module'>
print(id(check))
import check  # повторно не исполняется. Любой модуль будет использован единожды
print(id(check))