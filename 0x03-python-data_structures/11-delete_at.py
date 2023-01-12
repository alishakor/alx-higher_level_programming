#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    for i in my_list:
        if idx < 0 or idx > len(my_list) - 1:
            return my_list
        else:
            del my_list[idx]
            new_list = my_list
            print(new_list)
        return new_list
