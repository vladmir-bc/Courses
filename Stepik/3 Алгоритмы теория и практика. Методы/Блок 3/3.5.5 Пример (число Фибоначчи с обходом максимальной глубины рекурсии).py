# from rcviz import CallGraph, viz
# from PIL import Image
#
# cg = CallGraph(filename="fib3.png")
#
#
# @viz(cg)
def fib3(n):
    assert n >= 0
    f0, f1 = 0, 1
    for i in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1


print(fib3(100000))
print(len(str(fib3(100000))))
# cg.render()
# Image.open('./fib3.png').show()
