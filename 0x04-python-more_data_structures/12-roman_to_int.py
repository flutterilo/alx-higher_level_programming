#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or
            roman_string is None):
        return 0
    num = 0
    roman_chars = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                   'C': 100, 'D': 500, 'M': 1000}
    for i in range(0, len(roman_string)):
        if roman_chars.get(roman_string[i]) is None:
            return 0
        if (i - 1 >= 0 and
            roman_chars[roman_string[i]] >
                roman_chars[roman_string[i - 1]]):
            num += roman_chars[roman_string[i]] - roman_chars[
                roman_string[i - 1]] * 2
        else:
            num += roman_chars[roman_string[i]]
    return num
