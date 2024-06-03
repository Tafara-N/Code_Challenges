#!/usr/bin/env python3

"""
Program to count the number 4 in a given list
"""


def occurences_in_list(number):
    numbers = [4, 20, 1, 300, 4.4, 4, 35, 20, 4]

    return f"Number occurs {numbers.count(number)} times."


if __name__ == '__main__':
    print(occurences_in_list(4))
