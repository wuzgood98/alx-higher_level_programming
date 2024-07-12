#!/usr/bin/python3
# 1-my_list.py
# Gideon O Addo
"""Define a class MyList"""


class MyList(list):
    """
    Print the list but sorted (ascending sort).
    """
    def print_sorted(self):
        """Print the sorted list."""
        print(sorted(self))
