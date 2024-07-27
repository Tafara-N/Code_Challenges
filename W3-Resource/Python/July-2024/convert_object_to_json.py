#!/usr/bin/env python3

"""
Program to convert Python object to JSON data
"""

import json


def obj_to_json(python_object: dict) -> str:
    """
    Function converts Python object to JSON data

    Paramaters
        python_object: Python object to be converted

    Return
        JSON data: str
    """

    try:
        json_data = json.dumps(python_object)
        return json_data
    except TypeError:
        return "Invalid Python object"


if __name__ == "__main__":
    python_object = {"a": 1, "b": 2, "c": 3}
    print(obj_to_json(python_object))
