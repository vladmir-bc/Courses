class Alpha:
    def hi(self):
        print('Class Alpha')


class Bravo:
    def hi(self):
        print('Class Bravo')


class Charlie:
    def hi(self):
        print('Class Charlie')


class Delta(Alpha):
    pass


class Echo(Delta):
    pass


class Foxtrot(Bravo, Alpha):
    pass


class Golf(Foxtrot):
    pass


class Hotel(Echo, Charlie, Golf):
    pass


print(Hotel.mro())
Hotel.hi(0)
