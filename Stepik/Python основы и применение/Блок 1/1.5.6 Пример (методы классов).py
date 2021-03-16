class Counter:
    def __init__(self):
        self.count = 0

    def inc(self):
        self.count += 1

    def reset(self):
        self.count = 0


Counter  # class object
x = Counter()
x.inc()  # Вызов метода inc. Когда мы вызываем метод, мы подставляем себя (x) в кач-ве
# первого аргумента функции. Т.е. мы вызываем функцию Counter.inc и подставляем x в кач-ве
# аргумента self
print(x.count)  # 1
Counter.inc(x)  # Вызов функции Counter.inc и передача x в кач-ве аргумента self
print(x.count)  # 2
x.inc()
print(x.count)  # 3
x.reset()
print(x.count)  # 0
