#!/usr/bin/python3
"""writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """
    a function that writes an Object
    to a text file, using a JSON representation

    Args:
        my_obj: object
        filename: filename

    Raises:
        Exception: when the object can't be encoded

    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
