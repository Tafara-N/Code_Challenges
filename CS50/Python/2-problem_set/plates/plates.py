#!/usr/bin/env python3

"""
Program prompts the user for a vanity plate and then output 'Valid' if meets all
of the requirements or 'Invalid' if it does not.

Assume that any letters in the user’s input will be uppercase.

is_valid returns True if 's' meets all requirements and False if it does not.
"""

def main() -> None:
    """
    Main function for the program.
    """

    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s: str) -> bool:
    """
    Check if the input string is a valid license plate.

    Arguments:
        s: The input string to check.

    Returns:
        bool
            True if the input string is a valid license plate, False otherwise.
    """

    raise NotImplementedError


main()
