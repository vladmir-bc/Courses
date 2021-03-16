class PositiveList(list):
    def append(self, p_object):
        if p_object > 0:
            super(PositiveList, self).append(p_object)
        else:
            raise NonPositiveError

class NonPositiveError(Exception):
    pass

y = PositiveList([1, 2, 3, 4])
y.append(10)
print(y)
y.append(-10)
print(y)