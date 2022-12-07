#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """
    Delete an item at a specific position in a list.
    idx: position of element to be deleted (int)
    """

    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        return [x for x in my_list if x != my_list[idx]]