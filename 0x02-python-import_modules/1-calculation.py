#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5

    return ("{} + {} = {}".format(a, b, add(a,b)))
    return ("{} - {} = {}".format(a, b, sub(a,b)))
    return ("{} * {} = {}".format(a, b, mul(a,b)))
    return ("{} / {} = {}".format(a, b, div(a,b)))
