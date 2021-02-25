# MultipleIterator(in Day14-5) using generator and closure
def multiple_iterator(stop, multiple):
    current = 0

    def iterator():
        nonlocal current

        while (current + 1) * multiple <= stop:
            current += 1
            yield current * multiple

    return iterator()


generator_multiple_three = multiple_iterator(20, 3)

for i in generator_multiple_three:
    print(i, end=" ")
print()
generator_multiple_five = multiple_iterator(23, 5)

for i in generator_multiple_five:
    print(i, end=" ")