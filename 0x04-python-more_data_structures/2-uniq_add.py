#!/usr/bin/python3

def uniq_add(my_list=[]):

    uniq_list = set()

    for i in my_list:
        uniq_list.add(i)

    return sum(uniq_list)
