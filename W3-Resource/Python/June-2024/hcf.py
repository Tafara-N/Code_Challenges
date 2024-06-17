#!/usr/bin/env python3

"""
Program to compute the greatest common divisor (HCF) of two positive integers
"""

def hcf(x, y):
    z = x % y

    while z:
        # Update x to y, y to z, and calculate a new value for z (remainder of x divided by y).
        x = y
        y = z
        z = x % y

    # When z becomes 0, y contains the GCD
    return y


print(hcf(2, 5))
