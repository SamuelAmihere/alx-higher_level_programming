#!/usr/bin/python3
def print_reversed_lisit_integer(my_list=[]):
    """prints reversed form of a list of integers"""
    if len(my_list) == 0:
        pass
    else:
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))
