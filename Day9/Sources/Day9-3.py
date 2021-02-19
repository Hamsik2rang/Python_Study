# use of map in iterable objects

a = [10, 20, 30, 40, 50]

a = list(map(str, a))
print(a)

b = tuple(map(str, a))
print(b)

i = input("Type 2 or more Integer data: ")
c = i.split()
print(c)

c = map(int, c)
print(c)
