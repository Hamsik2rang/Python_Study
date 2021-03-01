# Make Exception
# You can make new Exception using Inheritance
from random import randint


class MyException(Exception):
    # Just call super class's constructor with passing error message to parameter.
    # Or cannot define anything and pass the error message when you raise this error class like this:
    # raise MyException("Error Message")
    def __init__(self):
        super().__init__("My Error Message")


def check_whether_it_is_even_number():
    try:
        x = randint(0, 5)
        if x & 1 != 0:
            raise MyException
        print(f"{x} is Even number.")
    except Exception as e:
        print(e, f": {x} is Odd number.")


check_whether_it_is_even_number()