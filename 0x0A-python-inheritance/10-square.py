#!/usr/bin/python3
'''
module call 10-square
'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''return area of square'''
        return self.__size ** 2
