#!/usr/bin/env python3

"""
A sphere has a volume equal to 356.82 cu.cm. Find the radius of the sphere

Formula: radius = (3 * volume / (4 * π)) ** (1 / 3)
"""

from math import pi

volume = 356.82

radius = (3 * volume / (4 * pi)) ** (1 / 3)

print(f"The radius of a sphere with volume {volume} is {radius:.2f}")
