#!/usr/bin/python3

'''
module call 2-append_write
'''


def append_write(filename="", text=""):
    '''
    append and write a text in file
    args:
        filename: name of file
        text: text to be appeneded
    '''
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
