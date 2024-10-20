#!/usr/bin/env python3

"""
Program prompts the user to insert a coin, one at a time, each time informing
the user of the amount due.

Once the user has inputted at least 50 cents, output how many cents in change
the user is owed.

Assume that the user will only input integers, and ignore any integer that isn’t
an accepted denomination.

Accepted denominations are: 5, 10, 25.

"""

def coke() -> None:
    """
    Prompt the user to insert a coin, one at a time, each time informing the
    user of the amount due.

    Once the user has inputted at least 50 cents, output how many cents in change
    the user is owed.
    """

    total = 0

    while total < 50:
        print(f"Amount Due: {50 - total}")

        coin = int(input("Insert coin: "))

        if coin in [5, 10, 25]:
            total += coin

    print(f"Change Owed: {total - 50}")


if __name__ == "__main__":
    coke()
