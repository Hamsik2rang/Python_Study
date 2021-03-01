# list comprehension

a = [i for i in range(10)]

print(a)

b = list(i for i in range(5))
print(b)

c = [round(i * 3.3, 2) for i in range(5)]
print(c)

d = [i for i in range(0, 10) if i & 1]
print(d)

e = [i * j for i in range(2, 10) for j in range(1, 10)]
print(e)
