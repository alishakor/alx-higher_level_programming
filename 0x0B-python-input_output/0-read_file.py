#!/usr/bin/python3

"""0-read_file.py module"""


def read_file(filename=""):
    """a function that reads a text file (UTF8) and prints it to stdout

    Args:
        filename: The file to be read

    """

    with open(filename, encoding="utf-8") as f:
        read_content = f.read()
        print(read_content, end="")
