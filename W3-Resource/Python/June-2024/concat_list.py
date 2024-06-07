#!/usr/bin/env python3

"""
Program that concatenates all elements in a list into a string and returns it
"""

def concat_list(values):
    return "".join(str(value) for value in values)


if __name__ == "__main__":
    values = [1, 5, 8, 3, 34.5, 1, 5, 8, "Tafara", 3, 1, 5, 8, 3]
    print(concat_list(values))
