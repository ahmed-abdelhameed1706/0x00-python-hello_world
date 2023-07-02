#!/usr/bin/python3

def text_indentation(text):
    """
    a function that prints on certain conditions
    text: text to be printed
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for c in text:
        print(c, end="")
        if c in [".", "?", ":"]:
            print("\n\n", end="")
