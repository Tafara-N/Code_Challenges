#!/usr/bin/env python3

"""
Program to count the number 4 in a given list
"""


def occurences_in_list(number):
    numbers = [4, 20, 1, 300, 4.4, 4, 35, 20, 4]

    return f"Number occurs {numbers.count(number)} times."


# OR THIS WAY


def occurences_in_list2(numbers):
    count = 0

    for number in numbers:
        if number == 4:
            count += 1
    return f"Number occurs {count} times."

print(occurences_in_list2([4, 20, 1, 300, 4.4, 4, 35, 20, 4]))


if __name__ == '__main__':
    print(occurences_in_list(4))
