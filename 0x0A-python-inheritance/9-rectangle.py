#!/usr/bin/python3
# 9-rectangle.py
# Gideon O Addo
"""Define a rectangle class that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize the width and height of the new rectangle.

        Args:
            width (int): The width of the new rectangle
            height (int): The height of the new rectangle
        """
        super().integer_validator('width', width)
        self.__width = width
        super().integer-validator('height', height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class.__name) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
