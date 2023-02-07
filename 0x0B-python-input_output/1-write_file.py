#!/usr/bin/python3

"""1-write_file.py module"""


def write_file(filename="", text=""):
    """a function that writes a string to a text file (UTF8)
    and prints it to stdout

    Args:
        filename: The file to be read
        text: contents to write

    """

    with open(filename, 'w', encoding="utf-8") as f:
        write_content = f.write(text)
        return write_content
