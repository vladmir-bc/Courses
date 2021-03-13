class MyClass:  # Определяем класс MyClass. Тело классов исполняется в момент определения самого класса
    a = 10  # MyClass.a. a - атрибут класса MyClass

    def func(self):  # MyClass.func. func - атрибут класса MyClass
        print('Hello')


x = MyClass()
print(MyClass.a)
MyClass.func(1)
print(type(x))
print((type(MyClass)))
