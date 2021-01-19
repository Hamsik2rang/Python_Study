# tuple
# tuple is immutable object. so when you create tuple once, you can't change or delete element(s) in it.

t = (1,)
print(t)

print("  remark: you can't create tuple that have an element without using comma(,). because it is confused with parenthesis operation.\n")

t = (1,2,3)
print(t)
t = 1,2,3
print(t)

# indexing
t = 1,2,3,4
print(f"t is {t}, and t[2] is {t[2]}\n")

# slicing
t = 1,2,3,4
print(f"t is{t}, and t[1:3] is {t[1:3]}\n")

# add tuple
t1 = 1,2
t2 = 3,4
print(f"t1 is {t1}, t2 is {t2}, then t1 + t2 is {t1+t2}\n")

# repeat tuple
t = 1,2
print(f"t is {t}, t * 3 is {t*3}\n")

# count
t = 1,2,1,1,4,2
print(f"t is {t}, and count of 1 in t is {t.count(1)}\n")

# get Index
t = 1,2,3,4
print(f"t is {t}, and index of 4 in t is {t.index(4)}\n")
