#!/usr/bin/env python3

"""
Program to create a histogram from a given list of integers
"""

def list_histogram(values):
    histogram = ""
    for value in values:
        histogram += f"{'#' * value}\n"
    return histogram.rstrip()


if __name__ == "__main__":
    values = [1, 5, 8, 3, 1, 5, 8, 3, 1, 5, 8, 3]
    print(list_histogram(values))
