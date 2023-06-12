#!/usr/bin/python3
def max_integer(my_list=[]):
    max = 0
    if my_list == []:
        return None
    if isinstance(my_list, list):
        for i in my_list:
            if i > max:
                max = i
        return max
