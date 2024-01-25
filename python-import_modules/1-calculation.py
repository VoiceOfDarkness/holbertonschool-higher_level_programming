#!/usr/bin/python3
from calculator_1 import add, div, mul, sub

if __name__ == "__main__":
    a = 10
    b = 5
    funcs = {"+": add(a, b), "/": div(a, b), "*": mul(a, b), "-": sub(a, b)}
    for operator, result in funcs.items():
        print("{} {} {} = {}".format(a, operator , b, result))
