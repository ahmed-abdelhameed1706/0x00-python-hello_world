#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        value = a / b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside Result: {}".format(value))

    return value
