# Global keyword and Nonlocale keyword

x = 13


# In foo(), x is not same with x in global script.
def foo():
    x = 20
    print(x)

foo()
print(x)


# So if you want to change value in local namespace, you have to use 'global' keyword.
def bar():
    global x
    x = 20
    print(x)

bar()
print(x)


# Also in nested-function, For the same reason, you have to use 'nonlocal' keyword.
def foooo():
    y = 15
    print(y)
    def barrr():
        nonlocal y
        y = 20
        print(y)
    barrr()

foooo()

# When you use local objects have same name, 'nonlocal' Keyword is applied variable in nearer namespace
def A():
    x = 100
    def B():
        x = 10
        def C():
            nonlocal x
            x += 50
            print(x)
        C()
    B()

# It print 60(10+50) as a result.
A()