#!/usr/bin/python3
"""defines a class square and validate it's size"""


class Square:
    """
    this is the class square
    """

    def __init__(self, size=0):
        try:
            assert type(size) == int
        except TypeError:
            print("size must be an integer")

        try:
            if size >= 0:
                self.__size = size
        except ValueError:
            print("size must be >= 0")
