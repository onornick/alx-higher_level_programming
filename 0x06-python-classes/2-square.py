#!/usr/bin/python3
# 2-square.py
"""Define a class Square."""


class Square:
    """Declare square."""

    def __init__(self, size=0):
        """Instantiate a new Square.
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("must be an integer")
        elif size < 0:
            raise ValueError("must be >= 0")
        self.__size = size
