#!/usr/bin/python3
import json
"""
Module 3-to_json_string
Contains function that returns JSON representation of obj (string)
"""


def to_json_string(my_obj):
    """returns json string representation"""
    return json.dumps(my_obj)
