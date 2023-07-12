#!/usr/bin/python3
"""A module that computes metrics
by reading from standard input.

Prints the following metrics after every ten lines or the
input of a keyboard interruption (CTRL + C):
    Total file size up to that point.
    Total Count of read status codes up to that point.
"""


import sys

total_file_size = 0
status_counts = {}

try:
    for i, line in enumerate(sys.stdin):
        data = line.split(" ")
        if len(data) < 2:
            continue
        status_code = data[-2]

        try:
            total_file_size += int(data[-1])
        except (IndexError, ValueError):
            pass

        status_counts[status_code] = status_counts.get(status_code, 0) + 1

        if (i+1) % 10 == 0:
            print("File size: {}".format(total_file_size))
            for code in sorted(status_counts):
                print("{}: {}".format(code, status_counts[code]))

    print("File size: {}".format(total_file_size))
    for code in sorted(status_counts):
        print("{}: {}".format(code, status_counts[code]))
except KeyboardInterrupt:
    print("File size: {}".format(total_file_size))
    for code in sorted(status_counts):
        print("{}: {}".format(code, status_counts[code]))
    raise
