#!/usr/bin/env python3


"""
Accepts a sequence of comma-separated numbers from the user and generates a
list and a tuple of those numbers
"""

numbers = input("Enter a sequence of comma-separated numbers: ")

# Split the input string into a list/tuple of numbers
print("Tuple: ", tuple(numbers.split(",")))
print("List: ", numbers.split(","))
