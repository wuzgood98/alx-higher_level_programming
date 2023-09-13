#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    """scores = list(a_dictionary.values())
    highest = scores[0]
    for score in range(len(scores) - 1):
        if scores[score + 1] > highest:
            highest = scores[score + 1]

    for key, val in a_dictionary.items():
        if val == highest:
            return (key)"""
    person = list(a_dictionary.keys())[0]
    score = a_dictionary[person]
    for key, val in a_dictionary.items():
        if val > score:
            score = val
            person = key
    return (person)
