#!/usr/bin/python3
import json
import csv
"""
This module defines the base class
that all other classes inherit from
"""


class Base:
    """
    This is the base class

    Args:
        __nb_objects: int - represents instances
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        constructor

        Args:
            id: int - rep the id of instance
        """
        if id is not None:
            self.id = Base.__nb_objects

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs

        Args:
            list_objs: list - list of instances
        """
        if list_objs is None:
            list_objs = []
        json_string = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs])
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding="utf-8") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Returns Python obj of JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns instance with attributes already set"""
        if cls.__name__ == "Square":
            rect = cls(1)
        if cls.__name__ == "Rectangle":
            rect = cls(1, 1)
        rect.update(**dictionary)
        return rect

    @classmethod
    def load_from_file(cls):
        """Returns list of instances"""
        filenamee = cls.__name__ + ".json"
        mylist = []
        try:
            with open(filenamee, "r") as f:
                instances = cls.from_json_string(f.read())
            for i, dic in enumerate(instances):
                mylist.append(cls.create(**instances[i]))
        except:
            pass
        return mylist
