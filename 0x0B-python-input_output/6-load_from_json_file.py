#!/usr/bin/python3

"""6-load_from_json_file.py module"""


import json
"""A module that take Python data hierarchies, and convert
them to string representations"""


def load_from_json_file(filename):
    """a function that create an object from a 'JSON file'

    Args:
        filename: the JSON file

    """
    with open(filename, 'r') as f:
        return json.load(f)
