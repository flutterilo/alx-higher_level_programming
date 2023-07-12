#!/usr/bin/python3
'''
module call 12-pascal_traingle
'''


def pascal_triangle(n):
    '''
    pascal_triangle
    args:
        n
    '''
    if n <= 0:
        return []

    my_triangles = [[1]]
    while len(my_triangles) != n:
        last = my_triangles[-1]
        next = [1]
        for i in range(0, len(last) - 1):
            next.append(last[i] + last[i + 1])
        next.append(1)
        my_triangles.append(next)
    return my_triangles
