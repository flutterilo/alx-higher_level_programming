#!/usr/bin/python3

'''
module call is_same_class
'''


def is_same_class(obj, a_class):
    '''
    check is it is same class
    args:
        obj: first argument to check
        a_class: second argment
    Return: return true if it same or false not
    '''
    return type(obj) is a_class
