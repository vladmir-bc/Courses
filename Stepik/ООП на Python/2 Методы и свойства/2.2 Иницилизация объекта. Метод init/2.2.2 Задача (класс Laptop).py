''' Создайте класс Laptop, у которого есть:

конструктор __init__, принимающий 3 аргумента: brand, model, price . Также во время инициализации необходимо создать атрибут laptop_name - строковое значение, вида "<brand> <model>"
hp = Laptop('hp', '15-bw0xx', 57000)
print(hp.laptop_name) # выводит "hp 15-bw0xx"
И затем создайте 2 экземпляра класса Laptop и сохраните их в переменные laptop1 и laptop2.'''

class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f"{self.brand} {self.model}"

# hp = Laptop('hp', '15-bw0xx', 57000)
# print(hp.laptop_name) # выводит "hp 15-bw0xx"

laptop1 = Laptop('hp', '15-bw0xx', 57000)
laptop2 = Laptop('hp', '15-bw0xx', 57000)