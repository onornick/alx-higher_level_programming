#!/usr/bin/python3
"""
Module 3-to_json_string
Contains function that returns JSON representation of obj (string)
"""


def to_json_string(my_obj):
    import json
    """returns json string representation"""
    return json.dumps(my_obj)
