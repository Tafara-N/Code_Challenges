#!/usr/bin/env python3

"""
Program that determines whether a given number (accepted from the user) is even
or odd, and prints an appropriate message to the user
"""


def even_or_odd(number):
    """
    Checks whether a number is even or odd
    """

    if number % 2 == 0:
        return f"{number} is even."
    return f"{number} is odd."


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(even_or_odd(number))
