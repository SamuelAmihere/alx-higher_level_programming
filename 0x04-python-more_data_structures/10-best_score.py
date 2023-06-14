#!/usr/bin/python3
def best_score(a_dictionary):
    temp = [(v, k) for k, v in a_dictionary.items()]
    temp.sort(reverse=True)
    return tem[0][1]
