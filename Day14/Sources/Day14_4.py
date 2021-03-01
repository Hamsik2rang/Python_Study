# iter(), next()
import random

it = iter(lambda: random.randint(1, 10), 3)
print(next(it))

for i in iter(lambda: random.randint(1, 100), 51):
    print(i, end=" ")
