#!/usr/bin/python3

"""
    Finds a peak in a list of unsorted integers
"""


def find_peak(arr):
    """Finds a peak in the given array"""
    size = len(arr)
    if size == 0:
        return None
    start, end = 0, len(arr) - 1
    while start < end:
        mid = (start + end) // 2

        if (arr[mid] < arr[mid + 1]):
            start = mid + 1
        else:
            end = mid

    return arr[start]
