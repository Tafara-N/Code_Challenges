#!/usr/bin/env python3

"""
Program that prompts the user for a str of text and then outputs that same text
but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase
or lowercase.

"""

def main(text: str) -> None:
    """
    Function that takes a string of text and removes all vowels from it.

    Arguments:
        text: The string of text to remove vowels from.
    """

    vowels = "AEIOUaeiou"

    for char in vowels:
        if char in text:
            text = text.replace(char, "")

    print(f"Output: {text}")


if __name__ == "__main__":
    string = input("Input: ")
    main(string)
