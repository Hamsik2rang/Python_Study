#list
a = [1,2,3,4]
print(a)

# indexing
a = [1,2,3,4]

print(f"\n0th element in a is {a[0]}")

# slicing
a = [1,2,3,4]

print(f"\n0th~2nd elements in a is {a[0:3]}")

# n-dimentional list
a = [1,2,3,[4,5,6]]

print(f"\nIf a is {a}, a[3][1] is {a[3][1]}")

# add list
a = [1,2,3,4]
b = [5,6,7]

print(f"\n{a} + {b} is {a+b}")

# repeat list
a = [1,2,3,4]
print(f"\n{a} * 2 is {a*2}")

# modifying an element
a = [1,2,3,4]
print(f"\nIf a is {a},")
a[-1] = 5
print(f"after modify a[-1] to 5 is {a}")

# modifying elements
a = [1,2,3,4]
print(f"\nIf a is {a},")
a[:2] = [5,6]
print(f"\nafter modify is {a}")

# append = 원소 하나 추가
a = [1,2,3,4]
print(f"\na is {a}")

a.append(5)
print(f"append 5 in a is {a}")

# extend = 원소 여러개 추가
a = [1,2,3,4]
print(f"\na is {a}")

a.extend([5,6,7])
print(f"extend [5,6,7] in a is {a}")

# pop
a = [1,2,3,4]
print(f"\npop element of -1th index is {a.pop(-1)}")
print(f"after pop is{a}")

# remove (remove for value)
a = [1,2,3,4]

print(f"\na is {a},")
a.remove(4)
print(f"after remove 4 in a is {a}")

# del (remove for index)
a = [1,2,3,4]

print(f"\na is {a},")
del a[3]
print(f"after del a[3] is {a}")

# reverse
a = [1,2,3,4]
print(f"\na is {a},")
a.reverse
print(f"after reverse is {a}")

# Get index
a = [1,2,3,4]
print(f"\na is {a}, index of 4 is {a.index(4)}")

# sorted
a = [1,2,4,3]
print(f"\na is {a},")
a.sort()
print(f"after sort of a is {a}\n")
a.sort(reverse = True)
print(f"if you give True to 'reverse' parameter,\nafter sort of a is {a}")

# insert
a = [1,2,3,5]

print(f"\na is {a},")
a.insert(3, 5)
print(f"after insert 5 at index 3, a is {a}")

# count
a = [1,2,3,2,4,1,2]
print(f"\na is {a}, count of 2 in a is {a.count(2)}")

# range to list
a = list(range(1,11))
print(f"\n{a}")

a = [*range(5)]
print(f"or {a}")

a = [i for i in range(16)]
print(f"or {a}")
