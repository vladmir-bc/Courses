try:
    15 / 0
    # e
except ArithmeticError:  # isinstance (e, ArithmeticError) == True
    print('ArithmeticError')
# except ZeroDivisionError: - не имеет смысла, т.к. ZeroDivisionError поймали ислючением выше  (# isinstance (e, ZeroDivisionError) == True)
    # print('Division by zero')

print(ArithmeticError.mro())
print(ZeroDivisionError.mro())
