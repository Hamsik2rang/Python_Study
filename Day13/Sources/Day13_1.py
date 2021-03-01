# In Python, Maximum recursion depth is set about 1000 times.
# So when recursive function call about 1000 times, it occurs RecursionError.

def recursive_hello(i):
    print(f"{i} : hello")
    recursive_hello(i+1)

recursive_hello(1)

# So recursive function must use with things what it takes to exit recursive call.

def recursive_hello_escapable(i):
    print(f"{i} : hello")
    if i<500:
        recursive_hello_escapable(i+1)
    else:
        return

recursive_hello_escapable(1)