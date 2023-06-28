#!/usr/bin/python3

"""
this module define class call square
"""


class Square:
    """Empty class"""
    def __init__(self, size=0, position=(0, 0)):
        if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

        if len(position) == 2 and type(position[0]) == int and type(position[1]) == int:
            if position[0] < 0 or position[1] < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if len(position) == 2 and type(position[0]) == int and type(position[1]) == int:
            if position[0] < 0 or position[1] < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            for i in range(self.__position[0]):
                print("_", end="")
            for i in range(self.__size):
                print("#", end="")
            print("")
