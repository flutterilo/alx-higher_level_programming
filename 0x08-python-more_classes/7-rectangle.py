#!/usr/bin/python3
'''
module call rectangle
'''


class Rectangle:
    '''class Rectangle'''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) == int:
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) == int:
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
        else:
            raise TypeError("height must be an integer")

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        if type(self.print_symbol) != str:
            self.print_symbol = str(self.print_symbol)
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height - 1):
                print(self.print_symbol * self.__width)
            print(self.print_symbol * self.__width, end="")
        return ""

    def print(self):
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                print(print_symbol * self.__width)
            print(print_symbol * self.__width, end="")
        print("")

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
