#!/usr/bin/python3
# 7-base_geometry.py
# Gideon O Addo
"""Define a base Geometry class"""


class BaseGeometry:
    """Base Geometry"""

    def area(self):
        """ Raise an exception. """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validate integer value.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
