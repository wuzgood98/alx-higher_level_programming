#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for item in a_dictionary:
        new[item] = a_dictionary[item] * 2
    return (new)
