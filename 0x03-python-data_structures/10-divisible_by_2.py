#!/usr/bin/python
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    for num in range(len(my_list)):
        if new_list[num] % 2 == 0:
            new_list[num] = True
        else:
            new_list[num] = False
    return new_list
