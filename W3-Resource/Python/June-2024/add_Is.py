#!/usr/bin/env python3

"""
Program to get a newly-generated string from a given string where "Is" has been
added to the front
Return the string unchanged if the given string already begins with "Is"
"""


def add_Is(string):
    """
    Function to add "Is" to the front of a given string
    """
    if string[:2] == "Is":
        return f"Already prefixed with 'Is': {string}"
    return f"Is {string}"


if __name__ == "__main__":
    string = input("Enter a string: ")
    print(add_Is(string))
