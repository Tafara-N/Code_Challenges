#!/usr/bin/env python3

"""
Program that returns a string that is n (non-negative integer) copies of a
given string
"""


def copy_string(string, number):
    """
    Function to return a string that is n copies of a given string
    """
    return string * number


if __name__ == "__main__":
    string = input("Enter a string: ")
    number = int(input("Enter a non-negative integer: "))

    print(copy_string(string, number))
