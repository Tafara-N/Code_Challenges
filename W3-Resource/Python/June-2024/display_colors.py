#!/usr/bin/env python3

"""
Program that prints out all colors from color_list_1 that are not present in
color_list_2
"""

def display_colors(color_list_1, color_list_2):
    """
    Function that prints out all colors from color_list_1 that are not present
    in color_list_2.
    """

    print(color_list_1.difference(color_list_2))


if __name__ == "__main__":
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])

    display_colors(color_list_1, color_list_2)
    print("\nDone...")
