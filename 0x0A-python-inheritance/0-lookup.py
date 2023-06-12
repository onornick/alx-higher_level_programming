#!/usr/bin/python3
"""This module contains a function that returns the\
        list of available attributes and methods of an object"""


def lookup(obj):
    """This function returns  the list of all
    attributes and methods of an obj"""
    return dir(obj)
