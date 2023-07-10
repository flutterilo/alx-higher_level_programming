#!/usr/bin/python3

'''
module call is_kind_of_class
'''


def is_kind_of_class(obj, a_class):
    '''
    check is it is instance of object or class
    args:
        obj: first argument to check
        a_class: second argment
    Return: return true if it same or false not
    '''
    return isinstance(obj, a_class)
