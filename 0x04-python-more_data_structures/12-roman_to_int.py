#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return (0)

    if not isinstance(roman_string, str):
        return 0

    """ Dictionary to map Roman numerals to the integer values """
    romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    num = 0
    prev_value = 0

    """ Iterate thru the Roman numerals from right to left """
    for i in reversed(range(len(roman_string))):
        current_value = romans[roman_string[i]]

        """ If the current value is less than the previous value,
            subtruct it from the result else add it"""
        if current_value < prev_value:
            num -= current_value
        else:
            num += current_value

        prev_value = current_value

    return (num)
