# 'yield from' keyword
def number_generator():
    x = [1, 2, 3, 4, 5]
    yield from x


for i in number_generator():
    # print(i)
    pass


# Generator Comprehension
g_comp = (i for i in range(0, 10) if i & 1 == 0)
for i in g_comp:
    print(i, end=" ")

print()

# It is the same expression like this:
for i in range(0, 10):
    if i & 1 == 0:
        print(i, end=" ")
