from rcviz import CallGraph, viz
from PIL import Image


cg = CallGraph(filename="fib2.png")
cache = {}

@viz(cg)
def fib2(n):
    assert n >= 0
    if n not in cache:
        cache[n] = n if n <= 1 else fib2(n - 1) + fib2(n - 2)
    return cache[n]

print(fib2(5))
cg.render()
Image.open('./fib2.png').show()

