#!/usr/bin/python3
'''
module call 5-save_t_json_file
'''
import json


def save_to_json_file(my_obj, filename):
    '''
    save to json file
    args:
        my_obj: object
        filename: name of file
    '''
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
