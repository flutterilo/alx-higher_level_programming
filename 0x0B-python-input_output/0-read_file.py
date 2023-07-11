#!/usr/bin/python3

'''
module call 0-read_file
'''


def read_file(filename=""):
    '''
    read content of file
    args:
        filename: name of file
    '''
    with open(filename) as f:
        print(f.read(), end="")
