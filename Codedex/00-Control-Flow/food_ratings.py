#!/usr/bin/env python3

"""
Program to review food based on ratings from 1-5, 5 being excellent and
1 being poor
"""

rating = 5.0

# Function to rate food
def rate_food(food_rating):
    if food_rating > 4.5:
        print("Extraordinary")
    elif food_rating > 4:
        print("Excellent")
    elif food_rating > 3:
        print("Good")
    elif food_rating > 2:
        print("Fair")
    else:
        print("Poor")


rate_food(rating)