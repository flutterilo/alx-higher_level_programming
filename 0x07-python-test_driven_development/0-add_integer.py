#!/usr/bin/python3
# 0-add_integer.py
'''Define one function add_integer'''


def add_integer(a, b=98):
    '''Definition of add_integer function

    args: integers or floats
    Return: an integer that represent the addition of a and b
    '''
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
