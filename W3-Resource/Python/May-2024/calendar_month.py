#!/usr/bin/env python3

from calendar import month


def main():
    """
    Main function to get the year and month from the user.
    """

    year = int(input("Enter the year: "))
    month = int(input("Enter the month: "))

    print_calendar(year, month)


def print_calendar(yyyy, mm):
    """
    Prints the calendar for a given month and year.
    :param yyyy: Year
    :param mm: Month
    """
    print("\n", month(yyyy, mm))


if __name__ == "__main__":
    main()
