#!/usr/bin/python3
"""
This module defines a rectangle
and its functionalities
"""


class Rectangle:
    """
    Defines a rectangle class
    Args:
        number_of_instances(int) : number of instances
        print_symbol(string) : symbol for string representation
        width(int) : width of rect.
        height(height) : height of rect.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialises the instance of a class"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

    @property
    def width(self):
        """returns the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """validates and sets value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """validates and sets value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """return the value of the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        s = "\n".join([f"{self.print_symbol}" * self.__width
                       for rows in range(self.__height)])
        return s

    def __repr__(self):
        """String representation to recreate new instance"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        Rectangle.number_of_instances =
        Rectangle.number_of_instances - 1
        print("Bye rectangle...")
