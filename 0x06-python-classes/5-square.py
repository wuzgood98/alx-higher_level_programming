#!/usr/bin/python3
# 5-square.py
# Gideon O Addo
"""Define a class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initilize a new square.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the current size of the square"""
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

    def my_print(self):
        """Print in stdout the square with the character #.
        If size is equal to 0, print an empty line.
        """
        for i in range(0, self.__size):
            [print('#', end='') for j in range(self.__size)]
            print('')
        if self.__size == 0:
            print('')
