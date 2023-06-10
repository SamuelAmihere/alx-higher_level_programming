#!/usr/bin/python3
def print_reversed_lisit_integer(my_list=[]):
    my_list1 = my_list[:]
    my_list1.reverse()
    for i in my_list1:
        print("{:d}".format(i))
