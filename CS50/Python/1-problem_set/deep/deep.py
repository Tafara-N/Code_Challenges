#!/usr/bin/env python3

"""
Program prompts the user for the answer to the Great Question of Life, the
Universe and Everything, outputting Yes if the user inputs 42 or
(case-insensitively) forty-two or forty two.

Otherwise output No

"""

correct = ["42", "forty-two", "forty two"]

question = (
    "What is the answer to the Great Question of Life, the Universe and Everything? "
)

answer = input(question).lower().strip()

print("Yes" if answer in correct else "No")
