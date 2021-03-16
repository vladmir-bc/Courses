class Cat:
    def hello():  # о self будет сказано далее
        print("Hello world from my kitty")


# Воспроизведем ошибку, которую мы получили на прошлом уроке
bob = Cat()


# bob.hello() получим ошибку, что функция принимает 0 аргументов, но 1 был передан

# Метод отличается от функции тем, что метод будет привязан к конкретному объекту,
# т.е. он будет связан с ним, а функция - нет. Функция ни с чем не связана, ее можнов вызывать отдельно
# Мы не можем отдельно вызвать функцию hello(), мы должны ее вызывать через объект
# При вызове метода, тот объект, с которым он связан будет автоматически проставляться в аргумент функции,
# поэтому возникает ошибка

# Опишем метода функции прием аргументов
class Cat:
    def hello(*args):  # принимаем произвольное количество аргументов
        print("Hello world from my kitty", args)


jim = Cat()
jim.hello()  # после строки выводится объект. Мы видим, что объект принадлежит классу Cat
print(jim)  # мы видим, что это один и тот же объект в нашей памяти


# Обратим внимание, что bob и jim - два разных объекта с разными адресами

# Через объект, который попадает первым аргументом внутрь метода мы можем получать
# доступ к атрибутам, например, класса. Продемонстрируем это:
class Cat:
    breed = 'pers'  # создадим породу всех кошек - персидская

    def hello(*args):  # принимаем произвольное количество аргументов
        print("Hello world from my kitty", args)

    def show_breed(instance):
        print(f"my breed is {instance.breed}")


walt = Cat()
walt.show_breed()
walt.breed = 'siam'
walt.show_breed()


# Можем также показать имя
class Cat:
    breed = 'pers'  # создадим породу всех кошек - персидская

    def hello(*args):  # принимаем произвольное количество аргументов
        print("Hello world from my kitty", args)

    def show_breed(instance):
        print(f"my breed is {instance.breed}")

    def show_name(instance):
        print(f"my name is {instance.name}")


mary = Cat()
# mary.show_name() - возникнет ошибка, т.к. атрибут name не был задан
#mary.name = "MARY"
#mary.show_name()  # теперь ошибки не возникнет, т.к. мы сами вручную задали этот атрибут

# Чтобы этот метод работал сам по себе, в экземпляре должен быть атритбут name,
# поэтому исправим метод:
class Cat:
    breed = 'pers'  # создадим породу всех кошек - персидская

    def hello(*args):  # принимаем произвольное количество аргументов
        print("Hello world from my kitty", args)

    def show_breed(instance):
        print(f"my breed is {instance.breed}")

    def show_name(instance):
        if hasattr(instance, 'name'):  # проверяем, есть ли у экземпляра атрибут name
            print(f"my name is {instance.name}")
        else:
            print('nothing')

mary = Cat()
mary.show_name()
mary.name = 'www'
mary.show_name()


# Для того, чтобы воспользоваться атрибутами, их тоже нужно создать. Создадим соотвествующий метод
class Cat:
    breed = 'pers'  # создадим породу всех кошек - персидская

    def hello(*args):  # принимаем произвольное количество аргументов
        print("Hello world from my kitty", args)

    def show_breed(instance):
        print(f"my breed is {instance.breed}")

    def show_name(instance):
        if hasattr(instance, 'name'):  # проверяем, есть ли у экземпляра атрибут name
            print(f"my name is {instance.name}")
        else:
            print('nothing')

    def set_value(koshka, value):  # вне зависимости от имени, сюда придет именно наш объект - экземпляр класса
        koshka.name = value

tom = Cat()
tom.show_name()
tom.set_value("Tom")
print(tom.name)
tom.show_name()

# добавим возраст кошки
class Cat:
    breed = 'pers'  # создадим породу всех кошек - персидская

    def hello(*args):  # принимаем произвольное количество аргументов
        print("Hello world from my kitty", args)

    def show_breed(instance):
        print(f"my breed is {instance.breed}")

    def show_name(instance):
        if hasattr(instance, 'name'):  # проверяем, есть ли у экземпляра атрибут name
            print(f"my name is {instance.name}")
        else:
            print('nothing')

    def set_value(koshka, value, age = 0):  # вне зависимости от имени, сюда придет именно наш объект - экземпляр класса
        koshka.name = value
        koshka.age = age

jerry = Cat()
jerry.set_value("Jerry")
print(jerry.age)

# self - общепринятое название объекта, у которого был вызван метод.
# По идее можно давать любое другое название, но по стандартам нужно задавать self

class Cat:
    breed = 'pers'  # создадим породу всех кошек - персидская

    def hello(*args):  # принимаем произвольное количество аргументов
        print("Hello world from my kitty", args)

    def show_breed(self):
        print(f"my breed is {self.breed}")

    def show_name(self):
        if hasattr(self, 'name'):  # проверяем, есть ли у экземпляра атрибут name
            print(f"my name is {self.name}")
        else:
            print('nothing')

    def set_value(self, value, age = 0):  # вне зависимости от имени, сюда придет именно наш объект - экземпляр класса
        self.name = value
        self.age = age
