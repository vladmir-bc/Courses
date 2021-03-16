# Атрибуты экземпляра класса

class Car:
    model = "BMW"
    engine = 1.6

print(Car)

# Результат вызова класса - экземпляр класса. Создадим 2 экземпляра класса

a1 = Car()
a2 = Car()

print(Car.__dict__)