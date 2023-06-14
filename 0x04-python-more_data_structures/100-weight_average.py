#!/usr/bin/python3
def weight_average(my_list=[]):
    weight_sum = 0
    new_list = []
    for i in my_list:
        new_list.append(i[0] * i[1])
        weight_sum += i[1]
    return sum(new_list) / weight_sum
