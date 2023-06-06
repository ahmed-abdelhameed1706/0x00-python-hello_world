#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in range(len(str)):
        x = ord(str[i])
        if x in range(97, 123):
            y = x - 32
            result = result + "{:c}".format(y)
        else:
            result = result + "{:c}".format(x)
    print(result)

