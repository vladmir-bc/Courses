class multifilter:
    def judge_half(self, pos, neg):
        return pos >= neg
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)

    def judge_any(self, pos, neg):
        return pos >= 1
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)

    def judge_all(self, pos, neg):
        return neg == 0
        # допускает элемент, если его допускают все функции (neg == 0)

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.func = funcs
        self.judge = judge
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция

    def __iter__(self):
        for element in self.iterable:
            pos, neg = 0, 0
            for el in self.func:
                if el(element):
                    pos += 1
                else:
                    neg += 1
            if self.judge(self, pos, neg):
                yield element
        # возвращает итератор по результирующей последовательности


def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)]
print(a)
print(list(multifilter(a, mul2, mul3, mul5)))
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))