#!/usr/bin/env python3
def no_c(my_string):
    new_string = ""
    for i in my_string:
        if ord(i) != ord("c") and ord(i) != ord("C"):
            new_string += i
    return new_string
