#!/usr/bin/python3

"""Write a class Square that defines a square by: (based on 0-square.py)

-Private instance attribute: size
-Instantiation with size (no type/value verification)
-You are not allowed to import any module
"""



class Square:

    """__init__ method used to initialize variables"""

    def __init__(self, size):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        self.__size = size
