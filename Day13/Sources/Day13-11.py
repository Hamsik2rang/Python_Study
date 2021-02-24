# Multiple Inheritance
# Python support Multiple Inheritance.
class Dragon:
    def breath(self):
        print("브레스!!!! 피해욧!!!!!")

class Elf:
    def heal(self):
        print("치유 마법")

class Player(Dragon, Elf):
    def attack(self):
        print("얍!")


me = Player()

me.breath()
me.heal()
me.attack()

# Diamond Inheritance
class A:
    def foo(self):
        print("A")

class B(A):
    def foo(self):
        print("B")

class C(A):
    def foo(self):
        print("C")

class D(B, C):
    pass

d = D()
# Generally, Programmer(User) don't know what letter will be printed
d.foo()

# In python, it follow Method Resolution Order, MRO.
# when you want to check this order, use mro() function like this:
D.mro()
# MRO is same with Inheritance argument order. 
# when class D was defined, Inheritance argument order is B->C. (class D(B, C): ...)

# +a. All Python objects inherit 'Object' class. like this:
print(int.mro())
