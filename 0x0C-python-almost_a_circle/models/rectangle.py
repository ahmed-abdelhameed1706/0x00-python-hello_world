#!/usr/bin/python3
"""
a rectangle model
"""

from models.base import Base


class Rectangle(Base):
    """
    class Rectangle that inhirits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initizalize method
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)
    
    @property
    def width(self):
        """
        getter for width
        """
        return self.__width

    @property
    def height(self):
        """
        getter for height
        """
        return self.__height

    @property
    def x(self):
        """
        getter for x
        """
        return self.__x

    @property
    def y(self):
        """
        getter for y
        """
        return self.__y

    @width.setter
    def width(self, value):
        """
        setter for width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        setter for height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """
        setter for x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """
        setter for y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        function to return the area of the rectangle
        """
        return self.__height * self.__width

    def display(self):
        """
        function to print the rectangle to stdout with char #
        """
        rect = (self.__y * "\n")
        for i in range(self.__height):
            rect += (" " * self.__x)
            rect += (("#" * self.__width) + "\n")
        print(rect, end="")

    def __str__(self):
        """
        returns a string that presents the rectangle
        """
        return
        (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """
        updates the rectangle with new values
        """
        if args is not None and len(args) != 0:
            arguments = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, arguments[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        a method to make a dictionary
        """
        self_dict = {"id": self.id, "width": self.__width,
                    "height": self.__height, "x": self.__x, "y": self.__y}
        return self_dict
