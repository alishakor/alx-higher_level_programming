#!/usr/bin/python3
for character in range(122, 96, -1):
    if character%2 == 0:
        character = chr(character)
    else:
        character = chr(character - 32)
    print("{}".format(character), end="")
