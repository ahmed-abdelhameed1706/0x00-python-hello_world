#!/usr/bin/python3
"""
function inhirits from int and reverts operators
"""


class MyInt(int):
    """
    a class to invert eq with ne
    """
    def __eq__(self, other):
        """
        an equal function to invert
        """
        if int(self) == int(other):
            return False
        else:
            return True

    def __ne__(self, other):
        """
        a not equal function to invert with eq
        """
        if int(self) != int(other):
            return False
        else:
            return True
