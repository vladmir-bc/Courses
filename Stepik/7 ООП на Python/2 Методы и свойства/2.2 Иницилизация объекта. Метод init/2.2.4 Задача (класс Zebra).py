''' Создайте класс Zebra, внутри которого есть метод which_stripe , который поочередно печатает фразы "Полоска белая", "Полоска черная", начиная именно с фразы "Полоска белая"'''


class Zebra:
    def __init__(self, color="белая"):
        self.color = color

    def which_stripe(self):
        print(f"Полоска {self.color}")
        if self.color == "белая":
            self.color = "черная"
        else:
            self.color = "белая"


# z1 = Zebra()
# z1.which_stripe()  # печатает "Полоска белая"
# z1.which_stripe()  # печатает "Полоска черная"
# z1.which_stripe()  # печатает "Полоска белая"
#
# z2 = Zebra()
# z2.which_stripe()  # печатает "Полоска белая"
