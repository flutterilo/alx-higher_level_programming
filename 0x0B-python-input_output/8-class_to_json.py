#!/usr/bin/python3
'''
module call 8-class_to_json
'''
import json


def class_to_json(obj):
    '''
    returns the dictionary description with simple data structure
    arg:
        obj: object
    '''
    return obj.__dict__
