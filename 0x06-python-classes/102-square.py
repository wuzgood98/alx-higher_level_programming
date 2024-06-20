#!/usr/bin/python3
# 102-square.py
# Gideon O Addo
"""Define a class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/Set the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('size must be a number')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Return the area of the current square"""
        return self.__size ** 2

    def __eq__(self, other):
        """Define the == comparison to a square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= comparison to a square."""
        return self.area() >= other.area()
