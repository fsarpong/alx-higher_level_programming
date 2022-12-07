#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    Find all multiples of 2 in a list.
    """
    multiples = []
    for num in my_list:
        if num % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)

    return multiples