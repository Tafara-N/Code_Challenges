#!/usr/bin/env python3

# Program to get the volume of a sphere with radius six

from math import pi

radius = float(input("Enter the radius of the sphere: "))

volume = (4 / 3) * pi * radius ** 3

print(f"The volume of a sphere with radius {radius} is {volume:.2f}")
