#!/usr/bin/python3
'''
module call 100-my_int
'''


class MyInt(int):
    '''inverts == or != operators'''

    def __eq__(self, other):
        return int.__ne__(self, other)

    def __ne__(self, other):
        return int.__eq__(self, other)
