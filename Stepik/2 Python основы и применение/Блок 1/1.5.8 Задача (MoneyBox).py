class MoneyBox:
    """Создание копилки"""

    def __init__(self, capacity):
        """Создание копилки заданной вместимости"""
        self.capacity = capacity  # вместимость копилки
        self.amount = 0  # общее количество монет в копилке
        print('Создана MoneyBox вместимостью ' + str(self.capacity))
        # конструктор с аргументом – вместимость копилки

    def can_add(self, v):
        """Проверка возможности добавить монеты в копилку"""
        self.value = v  # количество монет, которые хотим добавиь в копилку
        if self.capacity - self.value >= 0:  # если вместимость копилки не превышает количество добавляемых монет
            print('Монеты могут быть добавлены в количестве ' + str(self.value))
            return True
        print("""Число монет превышает максимальную вместимость, монеты не могут добавлены""")
        return False
        # True, если можно добавить v монет, False иначе

    def add(self, v):
        """Добавляем монеты в копилку"""
        self.value = v  # количество добавляемых монет
        if MoneyBox.can_add(self, v):
            self.amount += self.value
            self.capacity -= self.value
            return print('Монеты были добавлены моенты в количестве ' + str(self.value))
        return print("""Число монет превышает максимальную вместимость, монеты не добавлены""")
        # положить v монет в копилку


MoneyBox1 = MoneyBox(10)
MoneyBox1.add(5)
MoneyBox1.add(5)
MoneyBox1.add(0)
