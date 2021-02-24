# Closure


# Function
def foo():
    word = 'Happy'
    print(word, 'Birthday')

foo()


# Closure
def bar():
    word = 'Happy'
    def closure_bar():
        print(word, 'Birthday')
    return closure_bar

func = bar()
func()

# Closure that count the number of calls.
def counter():
    i = 0
    def count():
        nonlocal i
        i += 1
        return i
    return count

c = counter()
for i in range(10):
    print(c(), end=' ')