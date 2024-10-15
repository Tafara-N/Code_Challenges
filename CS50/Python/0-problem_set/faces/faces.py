#!/usr/bin/env python3

"""
Function called convert that accepts a `str` as input and returns that same
input with any `:)` converted to 🙂 and any `:(` converted to 🙁 .

All other text should be returned unchanged.

"""


def convert(text: str) -> str:
    """
    Convert :) to 🙂 and :( to 🙁

    Arguments:
        text: The text to convert

    Returns:
        str
            The converted text
    """

    return text.replace(":)", "🙂").replace(":(", "🙁")


def main() -> None:
    """
    Main function to run the program
    """

    text = input(">>> ")

    print(convert(text))


if __name__ == "__main__":
    main()
