#!/usr/bin/python3
"""defines a class square and validate it's size"""


class Square:
    """
    this is the class square
    """

    def __init__(self, size=0):
        """size is an integer"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
