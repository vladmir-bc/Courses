print('This Line is executed')


class EvenLengthMixin:
    def even_length(self):
        return len(self) % 2 == 0


class MyList(list, EvenLengthMixin):
    pass


ml = MyList([1, 12, 4, 17, 3, 'abc'])
ml.sort()
print(ml)
