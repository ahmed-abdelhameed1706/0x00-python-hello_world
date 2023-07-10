#!/usr/bin/python3
"""
function inhirits from int and reverts operators
"""


class MyInt(int):
    def __eq__(self, other):
        if int(self) == int(other):
            return False
        else:
            return True

    def __ne__(self, other):
        if int(self) != int(other):
            return False
        else:
            return True
