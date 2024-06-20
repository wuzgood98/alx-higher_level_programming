#!/usr/bin/python3
# 100-singly_linked_list.py
# Gideon O Addo
"""Define a class Node"""


class Node:
    """Represent the node of the linked list"""

    def __init__(self, data, next_node=None):
        """Initialize a new node.

        Args:
            data (int): The data of the list.
            next_node (Node): The new node of the list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/Set the current data of the list"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Get/Set the current node of the list"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


"""Define a class SinglyLinkedList"""


class SinglyLinkedList:
    """Represent a Singly-Linked List"""

    def __init__(self):
        """Initialize a new list"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SnglyLinkedList

        The node is inserted into the list at the correct
        ordered numerical position (increasing order).

        Args:
            value (Node): The new Node to insert.
        """

        new_node = Node(value)
        if self.__head is None or self.__head.data >= new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while (current.next_node is not None and
                    current.next_node.data < new_node.data):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Convert the linked list to a string representation
        by iterating through the nodes and joining their 'data'
        values with newline characters.
        """
        current = self.__head
        nodes = []
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)
