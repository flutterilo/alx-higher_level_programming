#!/usr/bin/python3

matrix = [[4, 3, 1], [5, 3.4, 7]]

print(all(isinstance(elm, int) or isinstance(elm, float) for elm in [rb for row in matrix for rb in row]))

