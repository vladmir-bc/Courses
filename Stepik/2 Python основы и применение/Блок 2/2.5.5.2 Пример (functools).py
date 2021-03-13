x = [
    ('Guiod', 'van', 'Rossum'),
    ('Haskell', 'Curry'),
    ('John', 'Backus')
]  # список имен, где каждое имя описывается кортежем, который состоит из составляющих каждого имени

import operator as op
from functools import partial

sort_by_last = partial(list.sort, key=op.itemgetter(-1))
print(x)
sort_by_last(x)
print(x)

y = ['abc', 'cba', 'abb']
sort_by_last(y)
print(y)