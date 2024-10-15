#!/usr/bin/env python3

"""

"""


def main():
    """
    Calculate the tip for a meal.
    """

    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d: str) -> float:
    """
    Remove the dollar sign from the string and convert it to a float.

    Arguments:
        d: The string to convert to a float.

    Returns:
        float
            The float representation of the string.
    """

    d = d.lstrip("$")

    return float(d)


def percent_to_float(p: str) -> float:
    """
    Remove the percent sign from the string and convert it to a float.

    Arguments:
        p: The string to convert to a float.

    Returns:
        float
            The float representation of the string.
    """

    p = p.rstrip("%")

    return float(p) / 100


main()
