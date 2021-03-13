class MyList(list):
    def even_lenght(self):  # Метод проверяет, является ли лист четной длины
        return len(self) % 2 == 0


x = MyList()  # 
print(x)  # []
"""Когда интерпретатор не находит имя внутри namespace экземпляра и не находит
имя внутри namespace класса, то он смотрит и проверяет namespace классов, 
от которых происходило наследование класса"""

x.extend([1, 2, 3, 4, 5])
'''Не найдя имя в namespace x, и не найдя имя в namespace MyList,
интерпретатор находит имя extend в namespace list.
И запускается метод extend для list'''

print(x)  # [1, 2, 3, 4, 5]
print(x.even_lenght())  # False
x.append(6)
print(x.even_lenght())  # True
