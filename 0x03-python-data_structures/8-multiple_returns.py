#!/usr/bin/python3
def multiple_returns(sentence):
    length = 0
    first_char = ""
    if len(sentence) == 0:
        length = 0
        first_char = None
    else:
        length = len(sentence)
        first_char = sentence[0]
    return ("Length: {} - First character: {}".format(length, first_char))
