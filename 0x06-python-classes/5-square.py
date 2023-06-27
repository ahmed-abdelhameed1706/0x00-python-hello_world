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

    @property
    def size(self):
        """gets the value of size"""
        return self.__size

    @size.setter
    """sets the value of size"""
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """this prints the square using #"""
        if self.__size == 0:
            print()
        elif:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
