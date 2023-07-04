#!/usr/bin/python3
'''
module call rectangle
'''


class Rectangle:
    '''class Rectangle'''
    def __init__(self, width=0, height=0):
        self.__width__ = width
        self.__height__ = height

    @property
    def width(self):
        return self.__width__

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width__ = value

    @property
    def height(self):
        return self.__height__

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be an integer")
        self.__height__ = value
