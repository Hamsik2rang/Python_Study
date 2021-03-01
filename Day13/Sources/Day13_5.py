# filter, map and  *reduce with lambda

a = [0,1, 2, 3, 4, 5, 6, 7, 8, 9]

odd_numbers = list(filter(lambda x: x & 1, a))
even_numbers = list(filter(lambda x: not x & 1, a))

print(odd_numbers)
print(even_numbers)


b = list(map(lambda x: x ** 2, a))
print(b)

# before use lambda with map, if you can make result with comprehension it's better to use comprehension than map.
b = [i ** 2 for i in a]
print(b)

# Since python 3, reduce has not been in built-in function library.
# so for use it, import functool module.
from functools import reduce

c = reduce(lambda x, y: x + y, a)
print(c)
