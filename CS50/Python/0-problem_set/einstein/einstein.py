#!/usr/bin/env python3

"""
Program prompts the user for mass as an integer (in kilograms) and then outputs
the equivalent number of Joules as an integer.

- Formula: E = mc^2

Steps:
======
energy = mass (user input) * speed of light (c) squared

speed_of_light = 300_000_000 m/s

"""

try:
    mass = int(input("Mass in kgs: "))
    speed_of_light = 300_000_000

    energy = mass * speed_of_light ** 2
except ValueError:
    print("Please enter a valid number.")
else:
    print(energy)
