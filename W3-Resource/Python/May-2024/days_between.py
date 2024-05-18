#!/usr/bin/env python3

"""
Program to calculate the number of days between two dates

Formula: days = (yyyy, mm, dd) - (yyyy, mm, dd)
"""

from datetime import date

date1 = date(2014, 7, 2)

date2 = date(2014, 7, 11)

days = date2 - date1

print(f"The number of days between {date1} and {date2} is {days.days} days.")
