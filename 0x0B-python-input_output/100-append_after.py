#!/usr/bin/python3
"""A module with append_after(filename="", search_string=""
new_string="")
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file"""
    with open(filename, 'r+') as f:
        s = f.readlines()
        i = 0
        for line in s:
            i += len(line)
            if search_string in line:
                f.seek(i)
                f.write(new_string)
