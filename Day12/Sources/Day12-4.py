from math import log

MILLI_SEC = 10 ** (-3)


n = 10 ** 3
a = log(log(2 * n, 2), 2) / log(log(n, 2), 2)
print(a)
b = log(2 * n, 2) / log(n, 2)
print(b)
c = 2 * n / n
print(c)
d = 2 * n * log(2 * n, 2) / n * log(n, 2)
print(d)

e = ((2 * n) ** 2) / n ** 2
print(e)

f = ((2 * n) ** 3) / n ** 3
print(f)

g = (2 ** (2 * n)) / 2 ** n
print(g)