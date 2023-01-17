#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary or len(a_dictionary) == 0:
        return None
    max_key = 0
    for key in a_dictionary.keys():
        if a_dictionary[key] > max_key:
            max_key = a_dictionary[key]
    return max_key
