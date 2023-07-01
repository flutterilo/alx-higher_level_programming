#!/usr/bin/python3
'''only one functions call matrix_divided'''


def matrix_divided(matrix, div):
    '''
    matrix_divided will divide a matrix by div
    args:
    ====
    matrix: list of list
    div: the number division
    return new_matrix
    '''

    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(elm, int) or isinstance(elm, float))
                    for elm in [va for row in matrix for va in row])):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")

    if not all(len(matrix[0]) == len(elm) for elm in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
