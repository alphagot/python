# import functools
# a = functools.reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
from functools import reduce

a = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])

print(a)
