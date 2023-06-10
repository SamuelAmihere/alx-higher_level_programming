#!/usr/bin/python3
def print_reversed_lisit_integer(my_list=[]):
    """prints reversed form of a list of integers"""
    i = len(my_list) - 1
    if i < 0:
        pass
    else:
        while(i >= 0):
            print("{:d}".format(my_list[i]))
            i -= 1
