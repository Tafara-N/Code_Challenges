#!/usr/bin/env python3

"""
Program to print the documents (syntax, description etc.) of Python
built-in function(s)
"""

import sys

arguments = sys.argv[1:]


def describe_function(function):
    """
    Function to print the documents (syntax, description etc.) of Python
    built-in function(s)
    """

    print(function.__doc__)


if len(arguments) != 1:
    print("USAGE: ./describe_function.py FUNCTION_NAME")
    sys.exit(1)
elif len(arguments) == 0:
    describe_function(eval(arguments[0]))
