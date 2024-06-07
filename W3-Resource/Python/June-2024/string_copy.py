#!/usr/bin/env python3

"""
Program to get n (positive) copies of the first 2 characters of a given string
    Returns n copies of the whole string if the length is less than 2
"""

def string_copy(string, number):
    if len(string) < 2:
        return f"{string * number}"
    else:
        return string[:2] * number

if __name__ == '__main__':
    string = input("Enter a string: ")
    number = int(input("Enter a number: "))
    print(string_copy(string, number))
