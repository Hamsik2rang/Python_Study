from art import logo_calc
from os import system


def plus(left, right):
    return float(left) + float(right)


def subtract(left, right):
    return float(left) - float(right)


def multiply(left, right):
    return float(left) * float(right)


def divide(left, right):
    return float(left) / float(right)


def calc():
    system("cls")
    print(logo_calc)

    operator = ["+", "-", "*", "/"]

    should_end = False
    while not should_end:
        left = input("What's the first number?: ")
        for op in operator:
            print(op)
        op = input("Pick an operation: ")
        right = input("What's the next number?: ")

        if op == "+":
            result = plus(left, right)
            print(f"{left} {operator[0]} {right} = {result}")
        elif op == "-":
            result = subtract(left, right)
            print(f"{left} {operator[1]} {right} = {result}")
        elif op == "*":
            result = multiply(left, right)
            print(f"{left} {operator[2]} {right} = {result}")
        elif op == "/":
            result = divide(left, right)
            print(f"{left} {operator[3]} {right} = {result}")
        else:
            print("Invalid operator.")
        new_start = input(
            f"Type 'y' to start a new calculation, or type 'n' to finish: "
        )

        if new_start == "y":
            pass
        else:
            should_end = True


calc()