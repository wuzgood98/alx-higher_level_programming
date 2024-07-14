#!/usr/bin/python3
# 10-square.py
# Gideon O Addo
"""Define a class Square that inherits from Rectangle (class)"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square that inherits from Rectangle"""

    def __init__(self, size):
        """Initilize the size of the new Square.

        Args:
            size (int): The size of the new Square.
        """
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size
