#!/usr/bin/env python3

"""
Program to calculate the difference between a given number and 17
    If the number is greater than 17, return twice the absolute difference
"""


def difference_by_17(number):
    if number <= 17:
        return 17 - number
    else:
        return 2 * (number - 17)


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(f"Difference between {number} and 17 is: {difference_by_17(number)}")
