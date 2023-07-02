#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """
    a function that prints my name
    first_name: the first name
    last_name: the last name
    prints the full name
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    if len(first_name) == 0 and len(last_name) == 0:
        raise ValueError("You have to enter atleast one name")

    if len(first_name) == 0:
        print(f"My name is {last_name}")
    elif len(last_name) == 0:
        print(f"My name is {first_name}")
    else:
        print(f"My name is {first_name} {last_name}")


