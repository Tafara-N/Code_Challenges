#!/usr/bin/env python3

"""
Program prompts the user for a greeting.

If the greeting starts with “hello”, output $0.

If the greeting starts with an “h” (but not “hello”), output $20.

Otherwise, output $100

"""

greeting = input("Greeting: ").lower().strip()

if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h") and not greeting.startswith("hello"):
    print("$20")
else:
    print("$100")
