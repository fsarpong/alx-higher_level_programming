#!/usr/bin/python3

def print_reversed_list_integer(mylist=[]):
    for i in range(1,len(mylist)+1):
        print("{:d}".format(mylist[-i]))