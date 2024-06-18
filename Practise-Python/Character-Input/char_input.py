#!/usr/bin/env python3

"""
Program asks the user to enter their name and their age.
Prints a message addressed to them that tells them the year that they will turn
100 years old.
"""

from datetime import datetime

year = datetime.now().year

try:
    name = input("Enter name: ")
    age = int(input("Enter age: "))
except ValueError:
    print("Please enter a valid age")
else:
    print(f"{name} will be 100 years old in {year + (100 - age)}")
