class Buffer:
    """Класс Buffer будет накапливать в себе элементы последовательности
    и выводить сумму пятерок последовательных элементов по мере их накопления"""

    def __init__(self):
        self.lst = list()

    # конструктор без аргументов

    def add(self, *a):
        for element in a:
            self.lst.append(element)
            if len(self.lst) % 5 == 0:  # такая формулировка не имеет смысла. Лучше написать if len(self.lst) == 5:
                print(sum(self.lst[-5:]))  # тогда тут будет print(sum(self.lst))
                del self.lst[-5:]  # а тут: self.lst.clear() - чистим буфер, не храним уже просуммированные и выведенные
                # элементы

    # добавить следующую часть последовательности

    def get_current_part(self):
        return self.lst  # важно чтобы здесь был return, а не print. Иы должны вернуть, а не вывести

    # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
    # добавлены


buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part()
buf.add(4, 5, 6)
buf.get_current_part()
buf.add(7, 8, 9, 10)
buf.get_current_part()
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
buf.get_current_part()

"""Решение преподавателя
Пример правильного решения:

Атрибут self.part -- хранит текущее состояние нашего буфера. 
Внутри метода add после добавления каждого элемента, 
проверяем длину текущего состоянии нашего буфера: если длина стала равно 5 -- выводим на экран сумму элементов в буфере 
и не забываем чистить буфер.

class Buffer:
    def __init__(self):
        self.part = []

    def add(self, *a):
        for i in a:
            self.part.append(i)
            if len(self.part) == 5:
                print(sum(self.part))
                self.part.clear()

    def get_current_part(self):
        return self.part"""
