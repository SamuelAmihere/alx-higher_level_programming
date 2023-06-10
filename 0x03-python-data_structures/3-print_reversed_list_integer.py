#!/usr/bin/python3
def print_reversed_lisit_integer(my_list=[]):
    """prints reversed form of a list of integers"""
    if my_list:
        my_list.reverse()
        for item in my_list:
            print("{:d}".format(item))
