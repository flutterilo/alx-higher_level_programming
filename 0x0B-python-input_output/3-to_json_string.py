#!/usr/bin/python3

'''
module call 3-to_json_string
'''


import json
def to_json_string(my_obj):
    '''
    json represenation of of object
    args:
        my_obj: object to be converted
    '''
    return json.dumps(my_obj)
