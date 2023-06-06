#!/usr/bin/python3
def remove_char_at(str, n):
    str1 = str[0:n]
    str2 = str[n + 1:]
    return (str1[0:] + str2[0:])
