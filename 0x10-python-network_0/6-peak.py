#!/usr/bin/python3
"""
function to find the peak in a list of numbers
"""


def find_peak(list_of_integers):
    """finds a peak in a list of numbers"""
    if not list_of_integers:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        return max(list_of_integers)
    mid = int(len(list_of_integers) / 2)
    if list_of_integers[mid] >= list_of_integers[mid - 1] and\
            list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    if list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid + 1:])
