#!/usr/bin/env python3

"""
Program to convert JSON data to Python object
"""

import json


def json_to_obj(json_data: str):
    """
    Function converts JSON data to an object

    Paramaters
        json_data: JSON data to be converted

    Return
        Python object: dict
    """

    try:
        python_object = json.loads(json_data)
        return python_object
    except json.JSONDecodeError:
        return "Invalid JSON data"


if __name__ == "__main__":
    json_data = '{"a": 1, "b": 2, "c": 3}'
    print(json_to_obj(json_data))
