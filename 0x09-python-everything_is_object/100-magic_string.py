#!/usr/bin/python3


x = 0


def magic_string():
    '''
    magic function that return string
    '''
    global x
    x += 1
    str = "BestSchool, " * (x - 1)
    str += "BestSchool"
    return str
