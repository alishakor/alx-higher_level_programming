#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) >= ord("A") and ord(letter) <= ord("Z"):
            print({}.format((letter), end=""))
        else:
            print({}.format(chr(ord(letter) - 32)), end="")
