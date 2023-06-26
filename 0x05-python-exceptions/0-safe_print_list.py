#!/bin/usr/python3

def safe_print_list(my_list=[], x=0):
    total_len = 0
    for i in range(x):
        try:
            print (my_list[i], end="")
        except IndexError:
            print("\n")
            return total_len
        else:
            total_len += 1

    return total_len
