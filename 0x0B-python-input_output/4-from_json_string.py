#!/usr/bin/python3
'''
module call 4-from_json_string
'''
import json


def from_json_string(my_str):
    '''
    return object represenation of json string
    args:
        my_str: string
    '''
    return json.loads(my_str)
