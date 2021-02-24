# iterator guide
a, b, c, d, e = range(0, 5)
print(f"{a},{b},{c},{d},{e}")

print(dir(range(0, 5)))

iter_r = range(0, 5).__iter__()
print(iter_r.__next__())
print(iter_r.__next__())
print(iter_r.__next__())
print(iter_r.__next__())
print(iter_r.__next__())


d = {"a": [1, 2], "b": "e"}
print(dir(d))

iter_d = d.__iter__()
print(iter_d.__next__())
print(iter_d.__next__())

