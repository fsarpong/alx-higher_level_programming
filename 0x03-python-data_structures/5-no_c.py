#!/usr/bin/python3

def no_c(my_string):
    string_list = list(my_string)
    the_cs = 'cC'
    new_list = []
    new_string = ""
    for item in string_list:
        if item not in the_cs:
            new_string += item
    
    return new_string