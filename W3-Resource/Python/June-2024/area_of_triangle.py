#!/usr/bin/env python3

"""
Program that will accept the base and height of a triangle and compute its area
"""

def area_of_triangle(base, height):
    return f"{(base * height) / 2:.2f}"


if __name__ == "__main__":
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    print(f"Area is: {area_of_triangle(base, height)}")
