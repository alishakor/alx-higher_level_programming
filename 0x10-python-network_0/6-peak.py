#!/usr/bin/python3
"""A function that finds a peak element in an unsorted list of integers"""


def find_peak(list_of_integers):
    """Find a peak element in a list of unsorted integers"""

    left_int = 0
    right_int = len(list_of_integers) - 1

    while left_int < right_int:
        mid = (left_int + right_int) // 2
        if list_of_integers[mid] < list_of_integers[mid+1]:
            left_int = mid + 1
        else:
            right_int = mid

    return list_of_integers[left_int]
