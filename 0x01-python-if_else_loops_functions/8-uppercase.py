#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in range(len(str)):
        if str[i] != " ":
            x = ord(str[i])
            if x > 90:
                y = x - 32
                result = result + "{:c}".format(y)
            else:
                result = result + ":c".format(x)
    print(result)

