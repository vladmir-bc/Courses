from random import random


class RandomIterator:
    def __iter__(self):  # метод нужен, чтобы использовать экземпляр класса в цикле for, пока этот метод не создан
        # объект экземпляра класса не итерируемый. Функция iter должна возвращать экземпляр итератора
        return self

    def __init__(self, k):  # конструктор класса, инициализирует экземпляр класса
        self.k = k
        self.i = 0

    def __next__(self):  # экземпляр класса и объект класса являются итератором тогда,
        # когда у них есть данный метод next
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration


# x = RandomIterator(3)
# print(next(x))  # next(x) - вызвать метод x.__next__() от самого объекта x.
# т.е. мы считаем, что x является итератором тогда, когда у него есть метод
# next__()
# print(next(x))
# print(next(x))
# print(next(x))

# iter(x)
x = RandomIterator(10)
for x in RandomIterator(10):
    print(x)
