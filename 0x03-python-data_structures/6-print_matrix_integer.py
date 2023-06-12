#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
        return
    if isinstance(matrix, list):
        for row in matrix:
            if isinstance(row, list):
                for i in row:
                    if i == row[len(row) - 1]:
                        print("{:d}".format(i))
                        continue
                    print("{:d}".format(i), end=' ')
