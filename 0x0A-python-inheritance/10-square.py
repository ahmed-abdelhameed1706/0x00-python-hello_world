#!/usr/bin/python3
"""
a square that inhirits from rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        self.__size = size
        super().integer_validator("size", self.__size)
        super().__init__(self.__size, self.__size)

    def area(self):
        return self.__size * self.__size
