#!/usr/bin/python3
'''
module call 9-student
'''


class Student:
    '''
    class call Student
    attributes:
        first_name
        last_name
        age
    '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        convert class to json
        '''
        if type(attrs) is list and all(type(elm) is str for elm in attrs):
            return {el: getattr(self, el) for el in attrs if hasattr(self, el)}
        else:
            return self.__dict__
