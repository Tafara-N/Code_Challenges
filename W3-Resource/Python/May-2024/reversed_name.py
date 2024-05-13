#!/usr/bin/env python3

"""
Accepts the user's first and last name and prints them in reverse order with
a space between them
"""

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print(first_name[::-1] + " " + last_name[::-1])
