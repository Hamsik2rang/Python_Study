# where are we? we can't go anymore.
a = set("acd")
print(a)
b = {"a", "b", "c"}
print(b)

c = a & b
print(c)
c = set.intersection(a, b)
print(c)

d = a | b
print(d)
d = set.union(a, b)
print(d)


e = a - b
print(e)
e = set.difference(a, b)
print(e)


print(e <= a)


if a.isdisjoint(set("egk")):
    print("서로소")
