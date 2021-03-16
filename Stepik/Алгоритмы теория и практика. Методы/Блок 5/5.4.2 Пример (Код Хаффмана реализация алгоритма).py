import heapq  # очередь с приоритетами
from collections import \
    Counter, namedtuple  # импортируем для подсчета частот символов. Поддерживает счетчик, сколько раз встретился объект


class Node(namedtuple("Node", ["left", "right"])):  # внутренность дерева: принимает первым аргументом имя класса, а вторым - его атрибуты: левый и правый потомок
    def walk(self, code, acc):  # второй аргумент code - префикс кода, который мы накопили, спускаясь от корня до листа
        self.left.walk(code, acc + "0")  # чтобы обойти внутренний узел, нужно спуститься сначала в левого потомка, добавив к префиксу ноль
        self.right.walk(code, acc + "1")  # затем в правого потомка, добавив к префиксу единицу


class Leaf(namedtuple("Leaf", ["char"])):  # лист: нет потомков, но есть символ, который в этом листе записан
    def walk(self, code, acc):
        code[self.char] = acc or "0"  # потомков у листа нет, поэтому все, что мы можем сделать - записать в словарь code построенный код данного символа


def huffman_encode(s):
    # h = [(freq, Leaf(ch)) for ch, freq in Counter(s).items()]  # Counter(s) считает, сколько раз каждый символ встречается в строке s и возвращает словарь. Плохой способ, вылазит ошибка при строке abracadabra
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))  # теперь для всех элементов в списке второй элемент различен, потому что после каждого шага длина h увеличивается на 1
    heapq.heapify(h)  # создает кучу типа min

    count = len(h)
    while len(h) > 1:  # пока в очереди есть хотя бы 2 элемента, делаем следующее
        freq1, _count1, left = heapq.heappop(h)  # достаем элемент с минимальной частотой
        freq2, _count2, right = heapq.heappop(h)  # достаем следующий элемент с минимальной частотой
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))  # добавляем в очередь новый элемент
        count += 1
    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    return code


def main():
    s = input()  # строка ввода не длинне, чем 10^4, поэтому ввод можно использовать любой
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    print(len(code), len(encoded))  # выводим количество символов строки и длину закодированной строки
    for ch in sorted(code):  # для удобство обходить символы будем в алфавитном порядке
        print("{}: {}".format(ch, code[ch]))
    print(encoded)


if __name__ == "__main__":
    main()
