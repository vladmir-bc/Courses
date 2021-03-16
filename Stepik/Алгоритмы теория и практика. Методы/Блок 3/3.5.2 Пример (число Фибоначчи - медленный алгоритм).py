from rcviz import CallGraph, viz
from PIL import Image


cg = CallGraph(filename="fib1.png")

@viz(cg)
def fib1(n):
    assert n >= 0
    return n if n <= 1 else fib1(n - 1) + fib1(n - 2)

print(fib1(5))
cg.render()
Image.open('./fib1.png').show()

