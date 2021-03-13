class Counter:  # Создается объект класса без атрибутов (пустой), который передается
    # в функцию init в качестве self
    def __init__(self):  # Принимает в качестве аргумента пустой экзмепляр класса.
        # Функция устанавливает атрибуты для объекта self
        self.count = 0

Counter  # class object
x = Counter()
print(x.count)  # 0
x.count += 1
print(x.count)  # 1
y = Counter()
print(y.count)
print('_____________________________________________________________________________')

class Counter2:
    def __init__(self, start=0):
        self.count = start

Counter2
x1 = Counter2(10)
z = Counter2()
print(x1.count)
print(z.count)
x1.count += 1
print(x1.count)