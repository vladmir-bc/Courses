class D:    pass


class E:    pass


class B(D, E):  pass


class C:    pass


class A(B, C):  pass


"""функция issubclass показывает, является ли первый аргумент наследником 
второго аргумента"""
print(issubclass(A, A))  # True - любой класс является наследником самого себя
print(issubclass(C, D))  # False. C не является наследником класса D
print(issubclass(A, D))  # True. A является наследником класса D. D - предок
# класса А
print(issubclass(C, object))  # True. C является наследником класса object
print(issubclass(object, C))  # False. object не является наследником класса C
print('_____________________________________________________________________________')

"""Чаще всего необходимо знать, ведёт ли себя объект как экземпляр класса. 
Функция isinstance отвечает на вопрос, является ли тип первого аргумента
наследником второго аргумента"""
x = A()
print(isinstance(x, A))  # True
print(isinstance(x, B))  # True
print(isinstance(x, object))  # True
print(isinstance(x, str))  # False
