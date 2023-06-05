#!/usr/bin/python3
"""
This module defines a class Rectangle that defines a rectangle
"""


class Rectangle:
    """
    class Rectangle defines a rectangular shape
    """
    def __init__(self, width=0, height=0):
        """
        Instantiation with optional width and height

        Args:
            width - width of rectangle
            height - height of rectangle
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """
        returns the width of the rectangle
        """
        return self._width

    @width.setter
    def width(self, value):
        """
        This method sets the value of width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """
        Getter that returns the height of the rectangle
        """
        return self._height

    @height.setter
    def height(self, value):
        """setter validates the value of value before assigning
        it to the height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
