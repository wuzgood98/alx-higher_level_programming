#!/usr/bin/python3
# 4-square.py
# Gideon O Addo
"""Define a class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initiliaze a new square.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get/Set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return (self.__size * self.__size)
