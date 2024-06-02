#!/usr/bin/env python3

"""
Program to calculate the sum of three given numbers
    If the values are equal, return three times their sum
"""

def sum_of_three(first, second, third):
    """
    Function to calculate the sum of three given numbers
    """
    if first == second == third:
        return 3 * (first + second + third)
    return first + second + third

if __name__ == "__main__":
    first = int(input("Enter the first number: "))
    second = int(input("Enter the second number: "))
    third = int(input("Enter the third number: "))
    
    print("Sum of three numbers is: ", sum_of_three(first, second, third))
