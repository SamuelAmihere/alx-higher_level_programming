#!/usr/bin/python3
"""A module that computes metrics
by reading from standard input.

Prints the following metrics after every ten lines or the
input of a keyboard interruption (CTRL + C):
    Total file size up to that point.
    Total Count of read status codes up to that point.
"""


import sys


def print_metrics(total_file_size, status_counts):
    """Prints metrics from the given data."""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


total_file_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0,
                 405: 0, 500: 0}

try:
    for i, line in enumerate(sys.stdin):

        try:
            data = line[:-1].split(" ")
            if len(data) < 2:
                continue
            status_code = int(data[-2])
            total_file_size += int(data[-1])

            if status_code in status_counts:
                status_counts[status_code] =
                status_counts.get(status_code, 0) + 1
        except (IndexError, ValueError):
            pass

        if (i+1) % 10 == 0:
            print_metrics(total_file_size, status_counts)

    print_metrics(total_file_size, status_counts)
except KeyboardInterrupt:
    print_metrics(total_file_size, status_counts)
    raise
