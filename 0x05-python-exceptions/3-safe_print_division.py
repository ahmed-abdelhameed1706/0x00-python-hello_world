#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        value = a / b
    except ZeroDivisionError:
        value = "None"
        return value
    finally:
        print("Inside Result: {}".format(value))

    return value
