#!/usr/bin/python3
# 100-my_int.py
# Gideon O Addo
"""Define a class MyInt that inherits from 'int'."""


class MyInt(int):
    """Represent a class that inherits from 'int'."""

    def __eq__(self, other):
        """
        Overrides the equality operator (==).
        Returns True if self and other are not equal, False otherwise.

        Parameters:
            other (any): The object to compare with self.

        Returns:
            bool
                True is self and other are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the inequality operator (!=).
        Returns True if self and other are equal, False otherwise.

        Parameters:
            other (any): The object to compare with self.

        Returns:
            bool
                True if self and other are equal, False otherwise.
        """
        return super().__eq__(other)
