#!/usr/bin/python3

"""5-save_to_json_file.py module"""


import json
"""A module that take Python data hierarchies, and convert
them to string representations"""


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file,
    using a JSON representation

    Args:
        my_obj: object to be written
        filename: text file to be written to

    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
