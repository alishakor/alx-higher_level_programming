#!/usr/bin/python3

"""3-to_json_string.py module"""


import json
"""A module that take Python data hierarchies, and convert
them to string representations"""


def to_json_string(my_obj):
    """a function that returns the JSON representation
    of an object (string)

    Args:
        my_obj: paramater to convert to string format

    Return:
        json string representation

    """

    return json.dumps(my_obj)
