# Discrete Mathmatics - Bit Arithmetic calculate algorithm
from functools import reduce


def add_to_string(bit1, bit2):
    carry = 0
    bit_string = ""

    while bit1 > 0 or bit2 > 0:
        a = bit1 & 1
        b = bit2 & 1
        res = (a + b + carry) // 2
        bit = a + b + carry - 2 * res
        bit_string = str(bit) + bit_string
        carry = res
        bit1 //= 2
        bit2 //= 2
    bit_string = str(carry) + bit_string
    return bit_string


def add_to_string_use_bitwise(bit1, bit2):
    carry = 0
    bit_string = ""

    while bit1 > 0 or bit2 > 0:
        a = bit1 & 1
        b = bit2 & 1
        bit = (a ^ b) ^ carry
        bit_string = str(bit) + bit_string
        # It's fairly complexity.
        carry = ((a ^ b) & carry) or ((a ^ carry) & b) or ((b ^ carry) & a)
        # Or you can code like this:
        # carry = (!a & b & carry) or (a & !b & carry) or (a & b & !carry)
        bit1 //= 2
        bit2 //= 2
    bit_string = str(carry) + bit_string
    return bit_string


def add_to_int(bit1, bit2):
    carry = 0
    bit_int = 0
    digit = 1
    while bit1 > 0 and bit2 > 0:
        a = bit1 & 1
        b = bit2 & 1
        res = (a + b + carry) // 2
        bit = a + b + carry - 2 * res
        bit_int = (bit * digit) + bit_int
        digit *= 10
        carry = res
        bit1 //= 2
        bit2 //= 2
    bit_int = (carry * digit) + bit_int
    return bit_int


def mul(bit1, bit2):
    add_list = []
    pow = 1
    while pow <= bit2:
        if bit2 & pow != 0:
            add_list.append(bit1)
        bit1 <<= 1
        pow *= 2

    result = reduce(add_to_int, add_list)
    return result


def div_and_mod(dividend, divisor):
    """dividend and divisor is Decimal integers
    Time Complexity is O(qlogn)"""
    q = 0
    r = abs(dividend)
    while r >= divisor:
        r = r - divisor
        q += 1
    if dividend < 0 and r > 0:
        r = divisor - r
        q = -(q + 1)
    return (q, r)


def mod_exp(under, index, m):
    x = 1
    pow = under % m
    a = index
    while a > 0:
        if a & 1 == 1:
            x = (x * pow) % m
        pow = (pow * pow) % m
        a //= 2
    return x


a = 0b1011
b = 0b0110
print(a)
print(b)
print(mul(a, b))
print(add_to_string(a, b))
print(add_to_string_use_bitwise(a, b))
div, mul = div_and_mod(34, 3)
print(mod_exp(3, 644, 645))

print(471 * 111 % 645)
