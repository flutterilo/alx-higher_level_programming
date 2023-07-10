#!/usr/bin/python3


'''
module call 8-rectangle
'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    class that inherten BaseGeometry class
    '''

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator("height", height)
        super().integer_validator("width", width)
