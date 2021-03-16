def h():
    print("- H")
    print("- 12")
    print("H - end")

def f():
    print("- F")
    g(h)
    print("F - end")

def g(a):
    print("- G - ",a)
    a()
    print("G - end")

print("\nMODULE")
g(f)

x = print(4)
print(x is None)