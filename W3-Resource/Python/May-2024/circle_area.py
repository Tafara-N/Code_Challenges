#!/usr/bin/env python3

# Calculating area of a circle based on user input

from math import pi

radius = float(input("Enter the radius of the circle: "))
area = pi * (radius ** 2)

print(f"Area of the circle is: {area:.2f}")
