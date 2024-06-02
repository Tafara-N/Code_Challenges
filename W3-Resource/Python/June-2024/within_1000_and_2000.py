#!/usr/bin/env python3

"""
Program to test whether a number is within 100 of 1000 or 2000
"""

def within_1000_and_2000(number):
    return abs(1000 - number) <= 100 or abs(2000 - number) <= 100

if __name__ == "__main__":
    number = int(input("Enter a number: "))

    if within_1000_and_2000(number):
        print(f"{number} is within 100 of 1000 or 2000")
    else:
        print(f"{number} is not within 100 of 1000 or 2000")
