#!/usr/bin/python3
# 8-rectangle.py
# Gideon O Addo
"""Define a Rectangle class that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize the width and height of the new rectangle

        Args:
            width: (int): The width of the new rectangle
            height: (int): The height of the new rectangle
        """
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
