#!/usr/bin/python3

"""4-from_json_string.py module"""


import json
"""A module that take Python data hierarchies, and convert
them to string representations"""


def from_json_string(my_str):
    """a function that returns an object (Python data structure)
    represented by a JSON string

    Args:
        my_str: paramater to return to its python format

    Return:
        python data structure representation

    """

    return json.loads(my_str)
