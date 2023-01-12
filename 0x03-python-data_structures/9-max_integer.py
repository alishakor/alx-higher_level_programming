#!/usr/bin/python3
def max_integer(my_list=[]):
    if isinstance(my_list, list):
        if my_list == []:
            return None
        elif my_list != []:
            max_value = 0
            for value in my_list:
                if value > max_value:
                    max_value = value
            return max_value
