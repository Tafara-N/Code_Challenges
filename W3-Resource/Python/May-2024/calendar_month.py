#!/usr/bin/env python3

import calendar


def main():
    """
    Main function to get the year and month from the user.
    """

    year = int(input("Enter the year: "))
    month = int(input("Enter the month: "))

    print_calendar(year, month)


def print_calendar(yyyy, month):
    """
    Prints the calendar for a given month and year.
    :parameter yyyy: Year
    :parameter month: Month
    """

    print("\n", calendar.month(yyyy, month))


if __name__ == "__main__":
    main()
