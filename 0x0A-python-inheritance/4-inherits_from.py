#!/usr/bin/python3

'''
module call inherts_from
'''


def inherits_from(obj, a_class):
    '''
    check is it is instance of object or class
    args:
        obj: first argument to check
        a_class: second argment
    Return: return true if it in sub class or false not
    '''
    return issubclass(type(obj), a_class) if type(obj) != a_class else False
