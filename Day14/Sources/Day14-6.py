# Generator
# Generator is a function contain 'yield' keyword.
# Generator works like iterator object.
def my_generator():
    # When Interpreter(Compiler) meet 'yield' keyword, Literally yield program flow(resources) to main routine.
    # It means return value there is next 'yield' keyword, and stop routine until next call.
    yield 0
    yield 1
    yield 2


def not_generator():
    return 10


ptr = my_generator()
print(next(ptr))
print(next(ptr))
print(next(ptr))

for i in not_generator():
    print(i)