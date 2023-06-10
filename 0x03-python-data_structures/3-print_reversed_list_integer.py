#!/usr/bin/python3
def print_reversed_lisit_integer(my_list=[]):
    """prints reversed form of a list of integers"""
    if not my_list:
        pass
    else:
        my_list.reverse()
        for i in range(len(my_list)):
            print("{:d}".format(my_list[i]))
