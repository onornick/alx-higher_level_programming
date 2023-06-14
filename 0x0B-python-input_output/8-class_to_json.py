#!/usr/bin/python3
"""Module that returns the dictionary description"""


def class_to_json(obj):
    """ Function that retuns the dictionary description of an obj """

    if hasattr(obj, "__dict__"):
        return obj.__dict__
