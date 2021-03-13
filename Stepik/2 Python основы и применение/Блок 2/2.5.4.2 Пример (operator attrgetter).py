x = [
    ('Guiod', 'van', 'Rossum'),
    ('Haskell', 'Curry'),
    ('John', 'Backus')
]  # список имен, где каждое имя описывается кортежем, который состоит из составляющих каждого имени

import operator as op
x.sort(key=op.itemgetter(-1))  # сортировка по последнему слову кортежа - фамилии
print(x)