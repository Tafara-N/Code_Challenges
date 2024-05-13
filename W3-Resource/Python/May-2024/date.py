#!/usr/bin/env python3

# Program displays the current date and time

import datetime as dt

date = dt.datetime.now()
date_time = date.strftime("%Y-%m-%d %H:%M:%S")

print("Current date and time:")
print(date_time)
