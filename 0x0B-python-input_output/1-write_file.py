#!/usr/bin/python3

"""1-write_file.py module"""


def write_file(filename="", text=""):
    """a function that writes a string to a text file (UTF8)
    and returns the number of characters written

    Args:
        filename: The textfile to be written to
        text: contents to write

    """

    with open(filename, 'w', encoding="utf-8") as f:
        write_content = f.write(text)
        return write_content
