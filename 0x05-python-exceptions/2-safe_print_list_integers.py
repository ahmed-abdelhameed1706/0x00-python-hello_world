#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    total_len = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except IndexError:
            return print("List Index is bigger than list len")
        except (ValueError, TypeError):
            continue
        else:
            total_len += 1
    print()
    return total_len
