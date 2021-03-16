def simple_gen():
    print('Checkpoint 1')
    yield 1
    print('Checkpoint 2')
    return 22
    yield 2
    print('Checkpoint 3')


gen = simple_gen()
x = next(gen)  # Checkpoint 1
print(x)  # 1
y = next(gen)  # Checkpoint 2
print(y)  # 2
z = next(gen)  # Checkpoint 3
#  StopIteration