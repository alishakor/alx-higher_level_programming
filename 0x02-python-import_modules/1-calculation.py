#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    return ("{} + {} = {}".format(a, b, add(a,b)), end=" ")
    return ("{} - {} = {}".format(a, b, sub(a,b)), end=" ")
    return ("{} * {} = {}".format(a, b, mul(a,b)), end=" ")
    return ("{} / {} = {}".format(a, b, div(a,b)), end=" ")
