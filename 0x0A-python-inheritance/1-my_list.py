#!/usr/bin/python3
"""This module inherits from the list"""


class MyList(list):
    """This class inherits from list"""
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
