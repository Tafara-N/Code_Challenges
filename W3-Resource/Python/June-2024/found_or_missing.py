#!/usr/bin/env python3

"""
Program checks whether a specified value is contained within a group of values
"""

def found_or_missing(values, value):
    if value in values:
        return True
    else:
        return False


if __name__ == '__main__':
    values = [1, 5, 8, 3]
    value = int(input("Enter a value: "))
    print(found_or_missing(values, value))
