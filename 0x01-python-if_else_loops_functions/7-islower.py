#!/usr/bin/python3
def islower(c):
    x = ord(c)
    for i in range(97, 123):
        if i == x:
            return True
        else:
            return False
