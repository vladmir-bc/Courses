"""Какие последовательности могут являться корректным порядком разрешения методов для класса E?"""


class A:
    pass


class B(A):
    pass


class C:
    pass


class D(C):
    pass


class E(B, C, D):
    pass


print(E.mro())
