#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)
    scores = list(a_dictionary.values())
    highest = scores[0]
    for score in range(len(scores) - 1):
        if scores[score + 1] > highest:
            highest = scores[score + 1]

    for key, val in a_dictionary.items():
        if val == highest:
            return (key)
