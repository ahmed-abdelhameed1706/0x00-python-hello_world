#!/usr/bin/python3
"""
class my list that inhirits from list
"""


class MyList(list):
    """
    a class inhirits from the list
    """
    def __init__(self):
        super().__init__(self)

    def print_sorted(self):
        """
        prints the list sorted

        """
        print(sorted(self))
