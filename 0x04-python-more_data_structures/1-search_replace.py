#!/usr/bin/python3

def search_replace(my_list, search, replace):
    for i, num in enumerate(my_list):
        if num == search:
            my_list[i] = replace
    return my_list