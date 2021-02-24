n = 1
CONSTANT = 2 ** (10 ** 9)
while n ** n < CONSTANT:
    print(n)
    n *= 10

print("fin exponent operation")

origin = n
for i in range(2, 10):
    if n ** n < CONSTANT:
        print(n)
        n = origin * i

print(n)