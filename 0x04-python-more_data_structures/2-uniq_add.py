#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = list(map(lambda x: x, set(my_list)))
    result = 0
    for i in uniq_list:
        result = result + i
    return result
