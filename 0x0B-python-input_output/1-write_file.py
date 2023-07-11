#!/usr/bin/python3

'''
module call 1-write_file
'''


def write_file(filename="", text=""):
    '''
    create file with a text
    args:
        filename: name of file
        text: text to be writen in file
    '''
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
