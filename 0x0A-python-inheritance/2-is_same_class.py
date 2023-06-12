#!usr/bin/python3
"""This module has a function that returns\
        bool depending on instance"""


def is_same_class(obj, a_class):
    """returns True if object is exactly\
            an instance of specified class"""
    return type(obj) == a_class
