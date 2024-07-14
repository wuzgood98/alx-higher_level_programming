#!/usr/bin/python3
# 11-square.py
# Gideon O Addo
"""Define a Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size):
        """Initialize the size of the new rectangle.

        Args:
            size (int): The size of the new rectangle.
        """
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size
