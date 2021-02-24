# Abstract Class
# For use Abstract class, have to import 'abc' module

from abc import *

# For define Abstract class, pass ABCMeta to metaclass keyward argument.


class MyAbClass(metaclass=ABCMeta):
    # For define Abstract method, use decorator '@abstractmethod' avobe the definition of function.
    @abstractmethod
    def print_name(self):
        pass

    @abstractclassmethod
    def print_object_count(cls):
        pass

# If you not define abstract method, TypeError will raised.


class MyClass(MyAbClass):
    object_count = 0

    def __init__(self, name):
        self.name = name
        MyClass.object_count += 1

    def print_name(self):
        print(self.name)

    @classmethod
    def print_object_count(cls):
        print(cls.object_count)


mc = MyClass("Hamsik2rang")

mc.print_name()
MyClass.print_object_count()


dic = {'apple': '맛있다',
       'banana': '길다',             'carrot': '두껍다'}
