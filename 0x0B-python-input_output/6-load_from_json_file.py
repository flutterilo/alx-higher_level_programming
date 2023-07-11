#!/usr/bin/python3
'''
module call 6-load_from_json_file
'''
import json


def load_from_json_file(filename):
    '''
    load json from file
    args:
        filename: name of file
    '''
    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
