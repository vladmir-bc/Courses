class A:
    def __init__(self, val=0):
        self.val = val

    def add(self, x):
        self.val += x

    def print_val(self):
        print(self.val)


a = A()  # 0
b = A(2)  # 2
c = A(4)  # 4
a.add(2)  # 2
b.add(2)  # 4

a.print_val()
b.print_val()
c.print_val()
