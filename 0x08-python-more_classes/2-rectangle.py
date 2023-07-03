#!/usr/bin/python3
"""
a module that defines a Rectangle
"""


class Rectangle:
    """
    a class that represenets a rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        returns the width
        """
        return self.__width

    @property
    def height(self):
        """
        returns the height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        sets the width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """
        sets the height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        returns the rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width * 2) + (self.__height *2)
