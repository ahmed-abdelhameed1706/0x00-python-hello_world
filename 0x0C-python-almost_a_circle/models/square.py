#!/usr/bin/python3
"""
a square class than inhirts from rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    a square class that inhirits rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        init for square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        overloading str
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        size getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        size setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        updates the square with new values
        """
        if args is not None and len(args) != 0:
            arguments = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, arguments[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        overloading to_dictionary
        """
        self_dict = {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y}
        return self_dict
