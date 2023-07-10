#!/usr/bin/python3


'''
module call 9-rectangle
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

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        return self.__width * self.__height
