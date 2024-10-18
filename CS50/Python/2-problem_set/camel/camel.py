#!/usr/bin/env python3

"""
Program prompts the user for the name of a variable in camel case and outputs
the corresponding name in snake case.

Assume that the user’s input will indeed be in camel case.

"""


def main() -> None:
    """
    The main function of the program.
    """

    string = input("camelCase: ")

    converted = camel_to_snake(string)

    print(converted)


def camel_to_snake(string: str) -> str:
    """
    Convert a variable name from camel case to snake case.

    Arguments:
        string: The variable name in camel case.

    Returns:
        str
            The variable name in snake case.
    """

    for letter in string:
        if letter.isupper():
            string = string.replace(letter, "_" + letter.lower())

    return string


if __name__ == "__main__":
    main()
