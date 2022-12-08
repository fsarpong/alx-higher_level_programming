#!/usr/bin/python3

def weight_average(my_list=[]):
    """
    Return the weighted average of all integers in a list of tuples.
    """
    numerator = 0
    denom = 0
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)
    else:
        for tup in my_list:
            numerator += tup[0] * tup[1]
            denom += tup[1]
    return numerator/denom