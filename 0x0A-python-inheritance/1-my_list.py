#!/usr/bin/python3
"""
class my list that inhirits from list
"""


class MyList(list):
    """
    a class inhirits from the list
    """
    def print_sorted(self):
        """
        prints the list sorted
        """
        print(sorted(self))
