#!/usr/bin/python3

"""2-append_write.py module"""


def append_write(filename="", text=""):
    """a function that appends a string at the end of a
    text file (UTF8) and returns the number of characters added

    Args:
        filename: The text file
        text: contents to append

    """

    with open(filename, 'a+', encoding="utf-8") as f:
        appended_content = f.write(text)
        return appended_content
