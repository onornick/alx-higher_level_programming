#!/usr/bin/python3
"""This module defines a class Student"""


class Student:
    """This class defines to_json function"""

    def __init__(self, first_name, last_name, age):
        """
        This function returns a dict representation of
        object instance

        Args:
            first_name: str
            last_name: str
            age: int

        Method:
            to_json: returns a dict rep of the instance

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        value = {}
        if attrs is None:
            return self.__dict__
        for k, v in self.__dict__.items():
            if k in attrs:
                value[k] = self.__dict__[k]
        return value
